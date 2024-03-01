import cozy
import claripy
import angr

BUFFER_SIZE = 18

proj_prepatched = cozy.project.Project('test_programs/GridIDPS/build/amp_challenge_arm.ino_unstripped.elf')

buffer_position_sym = claripy.BVS('bufferPosition', 32)
available_sym = claripy.BVS('SerialAvailable', 32)
read_sym = claripy.BVS('ReadSym', 32)
inputBuffer_sym = [claripy.BVS('buffer_sym_{}'.format(i), 8) for i in range(BUFFER_SIZE)]

class usb_serial_available(angr.SimProcedure):
    # pylint: disable=arguments-differ
    def run(self):
        return available_sym

class usb_serial_getchar(angr.SimProcedure):
    # pylint: disable=arguments-differ
    def run(self):
        return read_sym & 0xff

class usb_serial_write(angr.SimProcedure):
    # pylint: disable=arguments-differ
    def run(self, str, str_len):
        pass

class println(angr.SimProcedure):
    def run(self, arg):
        pass

def run(proj: cozy.project.Project):
    proj.hook_symbol('usb_serial_available', usb_serial_available)
    proj.hook_symbol('usb_serial_getchar', usb_serial_getchar)
    proj.hook_symbol('usb_serial_write', usb_serial_write)
    proj.hook_symbol('_ZN5Print7printlnEv', println)

    sess = proj.session('loop')

    command_log_addr = sess.malloc(3 * BUFFER_SIZE)
    class process_command(angr.SimProcedure):
        def run(self, cmd_str):
            # Instead of doing the code to process the string, just store it in the command_log buffer
            strncpy = angr.SIM_PROCEDURES["libc"]["strncpy"]
            self.inline_call(strncpy, command_log_addr, cmd_str, 3 * BUFFER_SIZE)
    proj.hook_symbol('process_command', process_command)

    buffer_position_addr = proj.find_symbol_addr('bufferPosition')
    sess.mem[buffer_position_addr].int = buffer_position_sym

    inputBuffer_addr = proj.find_symbol_addr('inputBuffer')
    for i in range(BUFFER_SIZE):
        sess.mem[inputBuffer_addr + i].char = inputBuffer_sym[i]

    loop_arguments = []

    return sess.run(loop_arguments)

run(proj_prepatched)
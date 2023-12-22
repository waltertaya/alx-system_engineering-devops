# 0x05-processes_and_signals

## PID Definition

- A PID(process identification number) is an id number that is automatically assigned to each process when it is created on a Unix-like OS.
- The process is an executing instance of a program.
- The process init is the only process that will always have same PID an any session and on any system, and that PID is 1. Because init is always the first process that PIDs are not immediately reused, inorder to prevent possible errors.
- The default maximum value of PIDs is 32,767.This maximum is important because it is essentially the maximum number of processes that can exist simultenously on a system.
- The file pid_max specifies the value at which PIDs wrap around. It has a default of 32,768.

1. `ps` or `pstree` - Command show PIDs for the processes currently on the system.
2. `top` command also shows PIDs of currently processes along with other informationabout them
3. `pidof` command provides the PID of a program whose name is passed to it as an argument.
4. `kill` To terminate frozen or otherwise misbehaving program using PID.
5. Information on current processes is stored in the `/proc` file system. This filesystem consists of kernel data that changes in real time `ls /proc | less` for listing the contents of the `/proc`

.text
.global _start
_start:
bl main
mov x8, #0x5d
svc #0
main:
    sub sp, sp, #0
    mov x9, #1
    mov x0, x9
    ret
    mov x0, #0
    ret

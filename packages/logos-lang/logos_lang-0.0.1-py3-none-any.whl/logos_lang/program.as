.text
.global _start
_start:
bl main
mov x8, #0x5d
svc #0
main:
    sub sp, sp, #16
    sub x10, sp, #0
    mov x9, #10
    str x9, [x10]
    ldr x9, [x10]
    mov x9, x9
    mov x0, x9
    ret
    mov x0, #0
    ret

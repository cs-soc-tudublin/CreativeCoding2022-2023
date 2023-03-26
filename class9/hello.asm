BITS 64

%define SYS_WRITE 1
%define SYS_EXIT 60
%define STDOUT 1

segment .text
global _start
_start:
	mov rax, SYS_WRITE
	mov rdi, STDOUT
	mov rsi, hello
	mov rdx, hlen
	syscall

	mov rax, SYS_EXIT
	mov rdi, 0
	syscall

segment .data
hello : db "Hello world", 10
hlen : equ $-hello


.intel_syntax noprefix

.global _start
.global most_common_byte

_start:
	call most_common_byte
	jmp end

most_common_byte:
	xor rax, rax
	xor rbx, rbx
	xor rcx, rcx

loop:
	cmp rax, rsi
	jg end_loop

	mov bl, [rdi + rax]

	mov rbp, rsp

	mov rcx, 0xff
	sub rsp, rcx
	sub rbp, rbx
	mov rcx, [rbp]
	inc rcx
	mov [rbp], rcx
	add rbp, rbx
	mov rsp, rbp

	inc rax

	jmp loop

end_loop:
	xor rax, rax
	xor rbx, rbx
	xor rcx, rcx

loop_2:
	cmp al, 0xff
	jg end_loop_2
	sub rbp, rax
	cmp [rbp], rbx
	jle skip_if

	mov rbx, [rbp]
	mov rcx, rax

skip_if:
	add rbp, rax
	inc rax

	jmp loop_2

end_loop_2:
	mov rax, rcx

	ret

end:

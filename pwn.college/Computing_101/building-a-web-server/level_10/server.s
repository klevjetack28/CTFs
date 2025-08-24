.intel_syntax noprefix
.globl _start
.globl _getFileName
.globl _getContent
.globl _getRequestType
.globl _getContentLength
.section .text
_start:
    	mov rax, 41
    	mov rdi, 2
    	mov rsi, 1
    	mov rdx, 0
    	syscall

	mov [server], rax

	mov rax, 49
	mov rdi, [server]
	lea rsi, [sockaddr_in]
	mov rdx, 16
	syscall

	mov rax, 50
	mov rdi, [server]
	mov rsi, 0
	syscall

while_accepting:
	mov rax, 43
	mov rdi, [server]
	xor rsi, rsi
	xor rdx, rdx
	syscall

	mov [accept], rax

	mov rax, 57
	syscall

	cmp rax, 0
	je child_process

	mov rax, 3
	mov rdi, [accept]
	syscall
	jmp while_accepting

child_process:
	mov rax, 3
	mov rdi, [server]
	syscall

	mov rax, 0
	mov rdi, [accept]
	lea rsi, [read_buffer]
	mov rdx, 512
	syscall

	mov [request_length], rax

	call _getFileName
	call _getRequestType
	cmp rax, 0
	je post
	cmp rax, 1
	je get
	jmp exit

post:
	call _getContent
	call _getContentLength

	mov rax, 2
	lea rdi, [file_path]
	mov rsi, 0x41
	mov rdx, 0x1ff
	syscall

	mov [fileid], rax

	mov rax, 1
	mov rdi, [fileid]
	lea rsi, [content]
	mov rdx, [content_length]
	syscall

	mov [file_size], rax

	mov rax, 3
	mov rdi, [fileid]
	syscall

	mov rax, 1
	mov rdi, [accept]
	lea rsi, [Response_200]
	mov rdx, 19
	syscall

	mov rdi, 0
	mov rax, 60
	syscall

get:
	mov rax, 2
	lea rdi, [file_path]
	mov rsi, 0
	mov rdx, 0
	syscall

	mov [fileid], rax

	mov rax, 0
	mov rdi, [fileid]
	lea rsi, [read_buffer_file]
	mov rdx, 512
	syscall

	mov [file_size], rax

	mov rax, 3
	mov rdi, [fileid]
	syscall

	mov rax, 1
	mov rdi, [accept]
	lea rsi, [Response_200]
	mov rdx, 19
	syscall

	mov rax, 1
	mov rdi, [accept]
	lea rsi, [read_buffer_file]
	mov rdx, [file_size]
	syscall

	mov rdi, 0
	mov rax, 60
	syscall

exit:
	mov rax, 3
	mov rdi, [server]
	syscall

	mov rdi, 0
        mov rax, 60
	syscall

_getRequestType:
	mov rdi, 0
	lea rsi, [read_buffer]

parse_type:
	cmp byte ptr [rsi], 0x47
	jne post_request
	mov rax, 1
	ret

post_request:
	mov rax, 0
	ret

_getFileName:
	mov rdi, 0
	lea rsi, [read_buffer]

parse_request:
	cmp byte ptr [rsi + rdi], 0x20
	je found_start
	inc rdi
	jmp parse_request

found_start:
	inc rdi
	mov rbx, rdi

find_end:
	cmp byte ptr [rsi + rdi], 0x20
	je end_request
	cmp byte ptr [rsi + rdi], 0x00
	je end_request
	inc rdi
	jmp find_end

end_request:
	mov byte ptr [rsi + rdi], 0
	mov rcx, rdi
	lea rsi, [read_buffer + rbx]
	lea rdi, [file_path]
	sub rcx, rbx
	rep movsb
	ret

_getContent:
	lea rsi, [read_buffer]
	mov rdi, 0

parse_content:
	cmp dword ptr [rsi + rdi], 0x0a0d0a0d
	je end_headers
	inc rdi
	jmp parse_content

end_headers:
	add rdi, 4
	mov rbx, rdi

find_end_content:
	cmp byte ptr [rsi + rdi], 0x00
	je end_content
	inc rdi
	jmp find_end_content

end_content:
	mov byte ptr [rsi + rdi], 0
	mov rcx, rdi
	lea rsi, [read_buffer + rbx]
	lea rdi, [content]
	sub rcx, rbx
	rep movsb
	ret

_getContentLength:
	mov rdi, 0
	lea rsi, [content]

content_length_loop:
	cmp byte ptr [rsi + rdi], 0x00
	je end_content_length
	inc rdi
	jmp content_length_loop

end_content_length:
	mov [content_length], rdi
	ret
.section .data
sockaddr_in:
	sin_family: 	.word 2
	sin_port:	.word 20480
	sin_addr:	.long 0x00000000
	sin_pad:	.quad 0
Response_200: .asciz "HTTP/1.0 200 OK\r\n\r\n"
Content_Length_Header: .asciz "Content-Length:"
content_length: .quad 0
.section .bss
server: .skip 4
accept: .skip 4
fileid: .skip 4
request_length: .skip 4
file_path: .skip 64
file_size: .skip 4
upeer_sockaddr:
	upeer_family:	.skip 2
	upeer_data:	.skip 14
upeer_addrlen: .skip 4
read_buffer: .skip 512
read_buffer_file: .skip 512
content: .skip 256

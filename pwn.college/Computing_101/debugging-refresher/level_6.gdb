run
set $random_value = 0
catch syscall read
commands
	silent
	if $rdi == 3
		set $random_value = *(long long *)($rsp+0x30)
		p/x $random_value
	end
	if $rdi == 0
		set *(long long *)$rsi = $random_value
		p/x $rsi
	end
	continue

end
continue

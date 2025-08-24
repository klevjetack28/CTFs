run
run
break *main+721
commands
	silent
	set $local_value = *(unsigned long long)($rsp-0x32)
	printf "Current Value: %llx\n", $local_value
	x/16gx $rsp
	continue
end
continue

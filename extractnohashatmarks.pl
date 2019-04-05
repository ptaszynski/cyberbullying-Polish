#!/usr/bin/perl -s
use utf8;
binmode(STDOUT, ":utf8");
binmode(STDIN, ":utf8");

while (<>) {
	utf8::decode($_);
	my $input = $_;
	chomp $input;
	my @inputarray = split(/ /, $input);
	my $i = 0;
	foreach my $word (@inputarray){	
		if ($word !~ /^(\#|\@)/g){
			$i++;
		}
	}
	if ($i>4){
		print "$input\n";
	}

}
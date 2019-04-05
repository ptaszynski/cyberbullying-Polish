#!/usr/bin/perl -s
use Text::Guess::Language;
use utf8;
binmode(STDOUT, ":utf8");
binmode(STDIN, ":utf8");

while (<>) {
	utf8::decode($_);
	my $input = $_;
	chomp $input;

	my $guessed_language = Text::Guess::Language->guess($input);
   	if ($guessed_language ne "en"){
   		print "$input\n";
   	}
}



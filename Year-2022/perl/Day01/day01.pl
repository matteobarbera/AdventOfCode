use strict;
use warnings;
use autodie;

use feature 'say';

# Part 1
open(my $file, '<', 'Day01/day01.txt') or die "Couldn't open file!";
my $max_calories = 0;
my $calories = 0;
while (my $line = <$file>) {
    chomp($line);
    if ($line eq "") {
        if ($calories > $max_calories) {
            $max_calories = $calories;
        }
        $calories = 0;
    } else {
        $calories += $line;
    }
}

say $max_calories;
close($file);

# Part 2
open($file, '<', 'Day01/day01.txt') or die "Couldn't open file!";
my @max_elf_arr = (0, 0, 0);
my $elf = 0;
while (my $line = <$file>) {
    chomp($line);
    if ($line eq "") {
        # if larger than lowest number then add it to array,
        # sort it, and pop lowest number
        if ($elf > $max_elf_arr[0]) {
            push(@max_elf_arr, $elf);
            @max_elf_arr = sort {$a <=> $b} @max_elf_arr;
            shift(@max_elf_arr);
        }
        $elf = 0;
    } else {
        $elf += $line;
    }
}
my $sum = 0;
foreach my $e (@max_elf_arr) {
    $sum += $e;
}
say $sum;
close($file);

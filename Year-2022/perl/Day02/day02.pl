use strict;
use warnings;
use autodie;

use feature 'say';

# A X - Rock 1
# B Y - Paper 2
# C Z - Scissors 3
# Win 3

my $file;

open($file, '<', 'Day02/day02.txt') or die "Couldn't open file!";
my %score_hash = ('X' => 1, 'Y' => 2, 'Z' => 3, 'A' => 1, 'B' => 2, 'C' => 3);
my %win_hash = ('X' => 'C', 'Y' => 'A', 'Z' => 'B');
my $score = 0;
my $opp_move;
my $my_move;
while (my $line = <$file>) {
    chomp $line;
    ($opp_move, $my_move) = split(' ', $line);
    $score += $score_hash{$my_move};
    if ($score_hash{$my_move} eq $score_hash{$opp_move}) {
        $score += 3;
    } elsif ($opp_move eq $win_hash{$my_move}) {
        $score += 6;
    }
}
say $score;
close($file);

open($file, '<', 'Day02/day02.txt') or die "Couldn't open file!";
my %cheat_hash = ('X' => 0, 'Y' => 3, 'Z' => 6);
$score = 0;
while (my $line = <$file>) {
    chomp $line;
    ($opp_move, $my_move) = split(' ', $line);
    $score += $cheat_hash{$my_move};
    if ($my_move eq 'X') {
        $score += 1 + (($score_hash{$opp_move} - 2) % 3)
    } elsif ($my_move eq 'Y') {
        $score += $score_hash{$opp_move};
    } else {
        $score += 1 + $score_hash{$opp_move} % 3;
    }
}
say $score;
close($file);

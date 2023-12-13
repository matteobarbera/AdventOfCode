use strict;
use warnings;
use autodie;

use feature 'say';

sub get_priority {
    my $item = @_;
    if (ord($item) >= 97) {
        return (ord($item) - 96);
    }
    else {
        return (ord($item) - 64);
    }
}

sub split_rucksack {
    my $rucksack = @_;
    my $rucksack_size = length($rucksack);
    my $compartment_size = $rucksack_size / 2;
    return (
        substr($rucksack, 0, $compartment_size),
        substr($rucksack_size, $compartment_size, $compartment_size)
    );
}

sub common_item {
    (my $first_compartment, my $second_compartment) = @_;

}

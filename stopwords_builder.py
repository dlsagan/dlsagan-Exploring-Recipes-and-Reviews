from nltk.corpus import stopwords
from collections import defaultdict
import pickle

base_stopwords = stopwords.words('english')

long_str_stopwords = """a
able
about
above
abst
accordance
according
accordingly
across
act
actually
added
adj
affected
affecting
affects
after
afterwards
again
against
ah
all
almost
alone
along
already
also
although
always
am
among
amongst
an
and
announce
another
any
anybody
anyhow
anymore
anyone
anything
anyway
anyways
anywhere
apparently
approximately
are
aren
arent
arise
around
as
aside
ask
asking
at
auth
available
away
awfully
b
back
be
became
because
become
becomes
becoming
been
before
beforehand
begin
beginning
beginnings
begins
behind
being
believe
below
beside
besides
between
beyond
biol
both
brief
briefly
but
by
c
ca
came
can
cannot
can't
cause
causes
certain
certainly
co
com
come
comes
contain
containing
contains
could
couldnt
d
date
did
didn't
different
do
does
doesn't
doing
done
don't
down
downwards
due
during
e
each
ed
edu
effect
eg
eight
eighty
either
else
elsewhere
end
ending
enough
especially
et
et-al
etc
even
ever
every
everybody
everyone
everything
everywhere
ex
except
f
far
few
ff
fifth
first
five
fix
followed
following
follows
for
former
formerly
forth
found
four
from
further
furthermore
g
gave
get
gets
getting
give
given
gives
giving
go
goes
gone
got
gotten
h
had
happens
hardly
has
hasn't
have
haven't
having
he
hed
hence
her
here
hereafter
hereby
herein
heres
hereupon
hers
herself
hes
hi
hid
him
himself
his
hither
home
how
howbeit
however
hundred
i
id
ie
if
i'll
im
immediate
immediately
importance
important
in
inc
indeed
index
information
instead
into
invention
inward
is
isn't
it
itd
it'll
its
itself
i've
j
just
k
keep    keeps
kept
kg
km
know
known
knows
l
largely
last
lately
later
latter
latterly
least
less
lest
let
lets
like
liked
likely
line
little
'll
look
looking
looks
ltd
m
made
mainly
make
makes
many
may
maybe
me
mean
means
meantime
meanwhile
merely
mg
might
million
miss
ml
more
moreover
most
mostly
mr
mrs
much
mug
must
my
myself
n
na
name
namely
nay
nd
near
nearly
necessarily
necessary
need
needs
neither
never
nevertheless
new
next
nine
ninety
no
nobody
non
none
nonetheless
noone
nor
normally
nos
not
noted
nothing
now
nowhere
o
obtain
obtained
obviously
of
off
often
oh
ok
okay
old
omitted
on
once
one
ones
only
onto
or
ord
other
others
otherwise
ought
our
ours
ourselves
out
outside
over
overall
owing
own
p
page
pages
part
particular
particularly
past
per
perhaps
placed
please
plus
poorly
possible
possibly
potentially
pp
predominantly
present
previously
primarily
probably
promptly
proud
provides
put
q
que
quickly
quite
qv
r
ran
rather
rd
re
readily
really
recent
recently
ref
refs
regarding
regardless
regards
related
relatively
research
respectively
resulted
resulting
results
right
run
s
said
same
saw
say
saying
says
sec
section
see
seeing
seem
seemed
seeming
seems
seen
self
selves
sent
seven
several
shall
she
shed
she'll
shes
should
shouldn't
show
showed
shown
showns
shows
significant
significantly
similar
similarly
since
six
slightly
so
some
somebody
somehow
someone
somethan
something
sometime
sometimes
somewhat
somewhere
soon
sorry
specifically
specified
specify
specifying
still
stop
strongly
sub
substantially
successfully
such
sufficiently
suggest
sup
sure    t
take
taken
taking
tell
tends
th
than
thank
thanks
thanx
that
that'll
thats
that've
the
their
theirs
them
themselves
then
thence
there
thereafter
thereby
thered
therefore
therein
there'll
thereof
therere
theres
thereto
thereupon
there've
these
they
theyd
they'll
theyre
they've
think
this
those
thou
though
thoughh
thousand
throug
through
throughout
thru
thus
til
tip
to
together
too
took
toward
towards
tried
tries
truly
try
trying
ts
twice
two
u
un
under
unfortunately
unless
unlike
unlikely
until
unto
up
upon
ups
us
use
used
useful
usefully
usefulness
uses
using
usually
v
value
various
've
very
via
viz
vol
vols
vs
w
want
wants
was
wasnt
way
we
wed
welcome
we'll
went
were
werent
we've
what
whatever
what'll
whats
when
whence
whenever
where
whereafter
whereas
whereby
wherein
wheres
whereupon
wherever
whether
which
while
whim
whither
who
whod
whoever
whole
who'll
whom
whomever
whos
whose
why
widely
willing
wish
with
within
without
wont
words
world
would
wouldnt
www
x
y
yes
yet
you
youd
you'll
your
youre
yours
yourself
yourselves
you've
z
zero
"""

long_str_sql_stopwords =  """a's    able    about   above   according
accordingly across  actually    after   afterwards
again   against ain't   all allow
allows  almost  alone   along   already
also    although    always  am  among
amongst an  and another any
anybody anyhow  anyone  anything    anyway
anyways anywhere    apart   appear  appreciate
appropriate are aren't  around  as
aside   ask asking  associated  at
available   away    awfully be  became
because become  becomes becoming    been
before  beforehand  behind  being   believe
below   beside  besides best    better
between beyond  both    brief   but
by  c'mon   c's came    can
can't   cannot  cant    cause   causes
certain certainly   changes clearly co
com come    comes   concerning  consequently
consider    considering contain containing  contains
corresponding   could   couldn't    course  currently
definitely  described   despite did didn't
different   do  does    doesn't doing
don't   done    down    downwards   during
each    edu eg  eight   either
else    elsewhere   enough  entirely    especially
et  etc even    ever    every
everybody   everyone    everything  everywhere  ex
exactly example except  far few
fifth   first   five    followed    following
follows for former  formerly    forth
four    from    further furthermore get
gets    getting given   gives   go
goes    going   gone    got gotten
greetings   had hadn't  happens hardly
has hasn't  have    haven't having
he  he's    hello   help    hence
her here    here's  hereafter   hereby
herein  hereupon    hers    herself hi
him himself his hither  hopefully
how howbeit however i'd i'll
i'm i've    ie  if  ignored
immediate   in  inasmuch    inc indeed
indicate    indicated   indicates   inner   insofar
instead into    inward  is  isn't
it  it'd    it'll   it's    its
itself  just    keep    keeps   kept
know    known   knows   last    lately
later   latter  latterly    least   less
lest    let let's   like    liked
likely  little  look    looking looks
ltd mainly  many    may maybe
me  mean    meanwhile   merely  might
more    moreover    most    mostly  much
must    my  myself  name    namely
nd  near    nearly  necessary   need
needs   neither never   nevertheless    new
next    nine    no  nobody  non
none    noone   nor normally    not
nothing novel   now nowhere obviously
of  off often   oh  ok
okay    old on  once    one
ones    only    onto    or  other
others  otherwise   ought   our ours
ourselves   out outside over    overall
own particular  particularly    per perhaps
placed  please  plus    possible    presumably
probably    provides    que quite   qv
rather  rd  re  really  reasonably
regarding   regardless  regards relatively  respectively
right   said    same    saw say
saying  says    second  secondly    see
seeing  seem    seemed  seeming seems
seen    self    selves  sensible    sent
serious seriously   seven   several shall
she should  shouldn't   since   six
so  some    somebody    somehow someone
something   sometime    sometimes   somewhat    somewhere
soon    sorry   specified   specify specifying
still   sub such    sup sure
t's take    taken   tell    tends
th  than    thank   thanks  thanx
that    that's  thats   the their
theirs  them    themselves  then    thence
there   there's thereafter  thereby therefore
therein theres  thereupon   these   they
they'd  they'll they're they've think
third   this    thorough    thoroughly  those
though  three   through throughout  thru
thus    to  together    too took
toward  towards tried   tries   truly
try trying  twice   two un
under   unfortunately   unless  unlikely    until
unto    up  upon    us  use
used    useful  uses    using   usually
value   various very    via viz
vs  want    wants   was wasn't
way we  we'd    we'll   we're
we've   welcome well    went    were
weren't what    what's  whatever    when
whence  whenever    where   where's whereafter
whereas whereby wherein whereupon   wherever
whether which   while   whither who
who's   whoever whole   whom    whose
why will    willing wish    with
within  without won't   wonder  would
wouldn't    yes yet you you'd
you'll  you're  you've  your    yours
yourself    yourselves  zero
"""

long_list_stop = long_str_stopwords.replace('\t', ' ').replace('\n', ' ').split()

long_list_sql_stopwords = long_str_sql_stopwords.replace('\t', ' ').replace('\n', ' ').split()

full_stopwords_dict = defaultdict(int)

for word in base_stopwords:

    if "'" in word:
        word1, word2 = word.split("'")

        full_stopwords_dict[word1] += 1
        full_stopwords_dict[word2] += 1

    else: 
        full_stopwords_dict[word] += 1

for word in long_list_stop:

    if "'" in word:
        word1, word2 = word.split("'")

        full_stopwords_dict[word1] += 1
        full_stopwords_dict[word2] += 1

    else: 
        full_stopwords_dict[word] += 1

for word in long_list_sql_stopwords:

    if "'" in word:
        try:
            word1, word2 = word.split("'")

            full_stopwords_dict[word1] += 1
            full_stopwords_dict[word2] += 1
        except ValueError:
            print(word)
    else: 
        full_stopwords_dict[word] += 1

full_stopwords = list(full_stopwords_dict.keys())

for word in full_stopwords:

    if word == '':
        full_stopwords.remove(word)

    if type(word) != str:
        full_stopwords.remove(word)

full_stopwords.sort()

full_stopwords.append('br')
full_stopwords.append('recipe')
full_stopwords.append('recipes')
full_stopwords.append('good')
full_stopwords.append('great')
full_stopwords.append('family')
full_stopwords.append('absolutely')
full_stopwords.append('abit')
full_stopwords.append('abm')
full_stopwords.append('abolutely')
full_stopwords.append('abc')
full_stopwords.append('zwizzle')
full_stopwords.append('zwt')
full_stopwords.append('aboout')
full_stopwords.append('add')
full_stopwords.append('easy')
full_stopwords.append('love')
full_stopwords.append('delicious')
full_stopwords.append('time')
full_stopwords.append('taste')
full_stopwords.append('post')
full_stopwords.append('aa')
full_stopwords.append('zwtiii')
full_stopwords.append('zwtii')
full_stopwords.append('zwthot')
full_stopwords.append('cooky')
full_stopwords.append('machine')
full_stopwords.append('serve')
full_stopwords.append('flavor')
full_stopwords.append('moist')
full_stopwords.append('pan')
full_stopwords.append('bake')
full_stopwords.append('cook')
full_stopwords.append('cup')
full_stopwords.append('ingredient')
full_stopwords.append('preparation')
full_stopwords.append('number')
full_stopwords.append('servings')
full_stopwords.append('minutes')
full_stopwords.append('hour')

with open("stopwords_list.pkl", "wb") as pfile:
    pickle.dump(full_stopwords, pfile)

C O D E

a n d o t h e r l a w s

o f c y b e r s p a c e

L A W R E N C E L E S S I G

A M E M B E R O F T H E P E R S E U S B O O K S G R O U P

Copyright © 1999 by Lawrence Lessig

Published by Basic Books,
A Member of the Perseus Books Group

All rights reserved. Printed in the United States of America. No part of
this book may be reproduced in any manner whatsoever without written
permission except in the case o f brief quotations embodied in critical
articles and reviews. For information, address Basic Books,10 E. 53rd
Street, New York, NY 10022-5299.

Book design by Victoria Kuskowski

A CIP catalog record for this book is available
from the Library of Congress

ISBN 0-465-03912-X

99 00 01 02 / 10 9 8 7 6 5 4 3 2 1

F O R C H A R L I E N E S S O N , W H O S E E V E R Y I D E A

S E E M S C R A Z Y — F O R A B O U T A Y E A R .

C O N T E N T S

Preface

P AR T 1 : R EG U LAB I L IT Y

Chapter 1
Chapter 2
Chapter 3
Chapter 4
Chapter 5

Code Is Law
Four Puzzles from Cyberspace
Is-Ism
Architectures of Control
Regulating Code

PA R T 2 : C OD E A N D O TH ER R E G UL AT O RS

Chapter 6
Chapter 7
Chapter 8

Cyberspaces
What Things Regulate
The Limits in Open Code

PA R T 3 : A P PLI C AT I ON S

Chapter 9
Chapter 10
Chapter 11
Chapter 12
Chapter 13
Chapter 14

Translation
Intellectual Property
Privacy
Free Speech
Interlude
Sovereignty

P AR T 4 : R ES P ON SE S

The Problems We Face
Responses
What Declan Doesn't Get

Chapter 15
Chapter 16
Chapter 17

Appendix
Notes
Index

ix

P R E F A C E

In the spring of 1996,at an annual conference organized under the name "Computers, Freedom, and Privacy"(CFP), two science-fiction writers told stories about cybers p ace's futu re . Vern or Vi n ge spo ke abo ut "u bi qu i tous law en forcem en t ," m ade
po s s i ble by "fin e - gra i n ed distri buted sys tem s" ; t h ro u gh com p uter chips linked by
the Net to every part of social life, a portion dedicated to the government's use. This
a rch i tectu re was alre ady being built—it was the In tern et—and tech n o l ogists were
a l re ady de s c ri bing its ex ten s i on s . As this net work of con trol became woven into
every part of social life, it would be just a matter of time, Vinge said, before the govern m ent cl a i m ed its fair share of con tro l . E ach new gen era ti on of code would increase this power of government. The future would be a world of perfect regulation,
and the architecture of distributed computing—the Internet and its attachments—
would make that perfection possible.

Tom Maddox followed Vinge. His vision was very similar, though the source of
con tro l , d i f feren t . The govern m en t's power would not come just from ch i p s . Th e
real source of power, Mad dox argued , was an all i a n ce bet ween govern m ent and
com m erce . Com m erce , l i ke govern m en t , f a res bet ter in a bet ter reg u l a ted worl d .
Property is more secure, data are more easily captured, and disruption is less of a
risk. The future would be a pact between these two forces of social order.

Code and commerce.
Wh en these two aut h ors spo ke , the futu re they de s c ri bed was not yet pre s en t .
Cybers p ace was incre a s i n gly every wh ere , but it was hard to imagine it tamed to
serve the ends of government. And commerce was certainly interested,though credit
card companies were still warning customers to stay far away from the Net. The Net
was an exploding social space of something. But it was hard to see it as an exploding
space of social control.

I didn't see either speech.I listened to them through my computer, three years after they spoke. Their words had been recorded; they now sit archived on a server at
MIT.1 It takes a second to tune in and launch a replay of their speeches about a perfectly ordered network of control. The very act o f listening to these lectures given
s everal ye a rs before — s erved on a rel i a ble and indexed platform that no do u bt
recorded the fact that I had listen ed , ac ross high - s peed , com m ercial In tern et lines
that feed my apartm ent both the Net and ABC News — con f i rm ed som ething of
their account. One can hear in the audience's reaction a recognition both that these
a ut h ors were talking ficti on — t h ey were scien ce - ficti on wri ters , a f ter all—and that
the fiction they spoke terrified.

x

p r e f a c e

Three years later it is no longer fiction. It is not hard to understand how the Net
could become the perfect space of regulation or how commerce would play a role in
that regulation. The current battle o ver MP3—a technology for compressing audio
files for simple distribution across the Net—is a perfect example.Last year MP3 was
quite the rage: CDs were copied and e-mailed, and web sites w ere built with thousands of songs archived and ready for anyone to take."Free music" joined the list of
free stuff that the Internet would serve.

But this year the story has changed. The recording industry is pushing a standard
that would make it easier to con trol the distri buti on of these files; Con gress has
passed a statute that makes it a felony to produce software that evades this control;
and one company that produces Sony Walkman–like machines to play MP3 files has
a l re ady announced plans to en a ble its machine to com p ly with these standards of
control. Control will be coded, by commerce, with the backing of the government.

Vinge and Maddox were first-generation theorists of cyberspace. They could tell
their stories about perfect control because they lived in a world that couldn't be controlled. They could connect with their audience because it wanted to resist the future
they described.Envisioning this impossible world was sport.

Now the impo s s i ble has been made re a l . Mu ch of the con trol in Vi n ge's and Maddox 's stories that stru ck many of t h eir listen ers as Orwellian now seems qu i te re a s ona bl e . It is po s s i ble to imagine the sys tem of perfect reg u l a ti on that Vi n ge de s c ri bed ,
and many even like what they see . It is inevi t a ble that an incre a s i n gly large part of t h e
In tern et wi ll be fed by com m erce , and most don't see anything wrong with that eit h er. In deed , we live in a time (again) wh en it is com m on p l ace to say: l et business take
c a re of t h i n gs . Let business sel f - reg u l a te the Net . Net com m erce is the new hero.

This book continues Vinge's and Maddox's stories. I share their view of the Net's
future; much of this book is about the expanding architecture of regulation that the
Internet will become. But I don't share the complacency of the self-congratulatory
ch cheers ech oing in the back ground of that 1996 record i n g. It was obvious in 1996
who "the enemy"was; nothing is obvious now.

The futu re is Vi n ge's and Mad dox 's accounts toget h er, not ei t h er alon e . If we
were on ly in for the dys topia de s c ri bed by Vi n ge , we would have an obvious and
powerful response: Orwell gave us the tools, and Stalin g ave us the resolve, to resist
the totalitarian state.A spying and invasive Net controlled by Washington is not our
future. 1984 is in our past.

And if we were only in for the future that Maddox described, many of our citizens would believe this utopia, not science fiction.A world where "the market" runs
free and the evil we call government, defeated, would, for them, be a world of perfect freedom.

But neither story alone describes what the Internet will be. Not Vinge alone, not
Maddox alone, but Vinge and Maddox together: a future of control in large part exercised by technologies of commerce, backed by the rule of law.

The challenge of our generation is to reconcile these two forces. How do we protect liberty when the architectures of control are managed as much by the government r e f a c e

x i

ment as by the private sector? How do we assure privacy when the ether perpetually
spies? How do we guarantee free thought when the push is to propertize every idea?
How do we guarantee self-determination when the architectures of control are perpetually determined elsewhere? How, in other words, do we build a world of liberty
when the threats are as Vinge and Maddox together described them?

The answer is not in the knee-jerk antigovernment rhetoric of our past. Reality
is harder than fiction; governments are necessary to protect liberty, even if also sufficient to destroy it. But neither does the answer lie in a return to Roosevelt's New
Deal. Statism has failed. Liberty is not to be found in some new D.C. alphabet soup
(WPA, FCC, FDA . . . ) of bureaucracy.

A second gen era ti on takes the ideals of the first and works them out against a
different background. It knows the old debates; it has mapped the dead-end arguments of the preceding thirty years. The objective of a second generation is to ask
questions that avoid dead-ends and move beyond them.

Th ere is great work out there from both gen era ti on s . E s t h er Dys on and Jo h n
Perry Ba rl ow sti ll inspire , and sti ll move on (Dys on is now the tem pora ry chair of
an or ga n i z a ti on some think wi ll become the govern m ent of the In tern et ; Ba rl ow
n ow spends time at Ha rva rd ) . And in the second gen era ti on , the work of An d rew
S h a p i ro, D avid Shen k , and Steven Jo h n s on is becoming well known and is compell i n g.

My aim is this second generation. As fits my profession (I'm a lawyer), my contri buti on is more lon g - wi n ded , m ore ob s c u re , m ore tech n i c a l , and more obtuse s e
than the best of either generation. But as fits my profession, I'll offer it anyway. In
the debates that rage right now, what I have to say will not please anyone very much.
And as I peck these last words before e-mailing the manuscript off to the publisher,
I can already hear the reactions: "Can't you tell the difference between the power of
the sheriff and the power of Walt Disney?""Do you really think we need a government agency regulating software code?" And from the other side:"How can you argue for an arch i tectu re of c ybers p ace (open source sof t w a re) that disabl e s
government's ability to do good?"

But I am also a te ach er. If my wri ting produ ces angry re acti on s , t h en it migh t
also effect a more balanced reflection. These are hard times to get it right, but the
easy answers to yesterday's debate won't get it right.

I have learn ed an ex tra ord i n a ry amount from the te ach ers and cri tics who have
h el ped me wri te this boo k . Hal Abel s on , Bru ce Ackerman a n , James Boyl e , Jack Golds m i t h , and Ri ch a rd Po s n er gave pati ent and excell ent advi ce on earl i er dra f t s . I am
gra teful for their pati en ce and ex trem ely fortu n a te to have had their advi ce . L a rry
Vale and Sa rah Wh i ting guided my re ading in the field of a rch i tectu re , t h o u gh no
do u bt I was not as pati ent a stu dent as I should have been . Sonya Me ad hel ped me
p ut into pictu res what it would take a law yer ten thousand words to say.

An army of students did most of the battle on earlier drafts of this book. Carolyn
Bane, Rachel Barber, Enoch Chang, Ben Edelman, Timothy Ehrlich, Dawn Far ber,

x i i

p r e f a c e

Melanie Glickson, Bethany Glover, Nerlyn Gonzalez,Shannon Johnson, Karen King,
Al ex Mac gi ll ivray, Ma Marcus Ma h er, D avid Mel a u gh , Teresa Ou, L a u ra Pirri , a n d
Wen dy Sel t zer provi ded ex ten s ive , i f re s respectful u l , c ri ti c i s m . And my assistants, Lee
Hopkins and Catherine Cho, were crucial in keeping this army in line (and at bay).
Th ree stu dents in particular have influ en ced my argumen t , t h o u gh none are
fairly called "students." Harold Reeves takes the lead in chapter 8. Tim Wu forced me
to rethink much of part 1. And Andrew Shapiro showed me the hopefulness in a future that I have described in very dark terms.

I am especially indebted to Catherine Marguerite Manley, whose extraordinary
talent, both as a writer and a researcher, made it possible to finish this work long before it othe rwise could have been finished. Thanks also to Tawen Chang and James
Stahir for their careful review of the notes, and work to keep them honest.

This is a not a field where one learns by living in libraries. I have learned everything I know from the conversations I have had, or watched, with an extraordinary
community of academics and activists, who have been struggling over the last five
years both to understand what cyberspace is and to make it better. This community
includes the scholars and writers I discuss in the text, especially the lawyers Yochai
Benkler, James Boyle, Mark Lemley, David Post, and Pam Samuelson. I've also benef i ted gre a t ly from convers a ti ons with non l aw yers , e s pec i a lly Hal Abel s on , Jo h n
Perry Barlow, Joseph Reagle, Paul Resnick, and Danny Weitzner. But perhaps more
importantly, I've benefited from discussions with the activists,in particular the Center for Dem oc racy and Tech n o l ogy, the Electronic Fron ti er Fo u n d a ti on , and the
American Civil Liberties Union. They have made the issues real,and they have done
much to defend at least some of the values that I think imp ortant.

This book would not have been wri t ten , h owever, but for a story by Ju l i a n
Dibbell,a conference organized by Henry J. Perritt,and many arguments with David
Johnson. I am grateful to all three for what they have taught.

I began this project as a fellow at Harvard's Program on Ethics and the Professions. I am grateful to Dennis Thompson for his skeptical encouragement that year.
The Berkman Cen ter for In tern et and Soc i ety at Ha rva rd Law Sch ool has made
much of my research possible.I am grateful in particular to Lillian and Myles Berkman for that support,and especially to the center's executive director and my sometime co-teacher, Jonathan Zittrain, for his support and, more important, friendship.
I've dedicated this book to the director of the Berkman Center, Charlie Nesson, who
has given me the space and support to do this work and a certain inspiration to push
it differently.

But more significant than any of that support has been the patience, and love, of
the pers on to wh om I've ded i c a ted my life , Bet tina Neu efei n d . Her love wi ll seem
crazy, and wonderful, for much more than a year.

P A R T O N E

r e g u l a b i l i t y

O N E

c o d e i s l a w

A dec ade ago, in t h e spr ing of 1 9 8 9 , com munism in Eur ope died — co l l a p s ed , as
a tent would fall if its main post were removed. No war or revolution brought communism to its end. Exhaustion did. Born in its place across Central and Eastern Europe was a new political regime, the beginnings of a new political society.

For constitutionalists (as I am), this was a heady time.I had just graduated from
l aw sch ool in 1989, and in 1991 I began te aching at the Un ivers i ty of Ch i c a go.
Chicago had a center devoted to the study of the emerging democracies in Central
and Eastern Europe.I was a part of that center. Over the next five years I spent more
hours on airplanes, and more mornings drinking bad coffee, than I care to remember.

Eastern and Central Europe were filled with Americans telling former Communists how they should govern. The advice was endless and silly. Some of these visitors literally sold constitutions to the emerging constitutional republics; the balance
had innumerable half-baked ideas about how the new nations should be governed.
These Americans came from a nation where constitutionalism had worked, yet apparently had no clue why.

The cen ter 's mission , h owever, was not to advi s e . We knew too little to guide .
Our aim was to watch and ga t h er data abo ut the tra n s i ti ons and how they progressed. We wanted to understand the change, not direct it.

What we saw was striking, if understandable. Those first moments after communism's collapse were filled with antigovernmental passion—with a surge of anger directed against the state and against state reg u l a ti on . Le ave us alon e , the peop l e
s eem ed to say. Let the market and non govern m ental or ga n i z a ti ons—a new soc iety — t a ke govern m en t's place . Af ter gen era ti ons of com mu n i s m , this re acti on was
completely understandable. What compromise could there be with the instrument
of your repression?

A certain American rhetoric supported much in this reaction. A rhetoric of libertarianism. Just let the market reign and keep the government out of the way, and

f reedom and pro s peri ty would inevi t a bly grow. Th i n gs would take care of t h ems elve s . Th ere was no need , and could be no place , for ex ten s ive reg u l a ti on by the
state.

But things didn't take care of themselves. Markets didn't flourish. Governments
were crippled,and crippled governments are no elixir of freedom. Power didn't disappear—it simply shifted from the state to mafiosi, themselves often created by the
state. The need for traditional state functions—police, courts,schools,health care—
d i d n't magi c a lly go aw ay. Priva te interests didn't em er ge to fill the need . In s te ad ,
needs were unmet. Security evaporated.A modern if plodding anarchy replaced the
bland communism of the previous three generations: neon lights flashed advertisements ents for Ni ke ; pen s i on ers were swi n dl ed out of t h eir life savings n gs by fra u du l en t
stock deals; bankers were murdered in broad daylight on Moscow streets. One system of control had been replaced by another, but neither system was what Western
libertarians would call freedom.

At just about the time when this post-communist euphoria was waning—in the
mid-1990s—there emerged in the West another "new society," to many just as exciting as the new societies promised in post-communist Europe. This was cy berspace.
F i rst in univers i ties and cen ters of re s e a rch , and then within soc i ety gen era lly, c yberspace became the new target of libertarian utopianism. Here freedom from the
state would reign. If not in Moscow or Tblisi,then here in cyberspace would we find
the ideal libertarian society.

The catalyst for this change was likewise unplanned. Born in a research project
in the Defense Department,cyberspace too arose from the displacement of a certain
a rch i tectu re of con tro l . The to ll ed , s i n gl e - p u rpose net work of tel eph ones was displaced by the untold and multipurpose network of packet-switched data. And thus
the old on e - to - m a ny arch i tectu res of p u blishing (tel evi s i on , rad i o, n ews p a pers ,
books) were supplemented by a world where everyone could be a publisher. People
could com mu n i c a te and assoc i a te in ways that they had never done before . Th e
space promised a kind of society that real space could never allow—freedom without anarchy, control without government, consensus without power. In the words of
a manifesto that will define our generation: "We reject: kings, presidents and voting.
We believe in: rough consensus and running code."1

As in post-Communist Europe, first thoughts about cyberspace tied freedom to
the disappearance of the state. But here the bond was even stronger than in post-
Communist Europe. The claim now was that government could not regulate cybers p ace , that cybers p ace was essen ti a lly, and unavoidably d a bly, f ree . G overn m ents co u l d
threaten, but behavior could not be controlled;laws could be passed, but they would
be meaningless e s s . Th ere was no ch oi ce abo ut wh i ch govern m ent to install — n on e
could reign. Cyberspace would be a society of a very different sort. There would be
definition and direction, but built from the bottom up, and ne ver through the directi on of a state . The soc i ety of this space would be a fully sel f - ordering en ti ty,
cleansed of governors and free from political hacks.

c o d e i s l a w

I taught in Central Europe during the summers of the early 1990s; I witnessed
the tra n s form a ti on in atti tu des abo ut com munism that I de s c ri bed at the start of
this chapter. And so I felt a bit of déjà vu when in the spring of 1995,I began to teach
the law of c ybers p ace , and saw in my stu dents these very same po s t - com mu n i s t
thoughts about freedom and government. Even at Yale—not known for libertarian
p a s s i ons—the stu dents seem ed drunk with what James Boyle would later call the
"libertarian gotcha":2 no government could survive without the Internet's riches, yet
no govern m ent could con trol what went on there . Re a l - s p ace govern m ents wo u l d
become as pathetic as the last Communist regimes. It was the withering of the state
that Ma rx had prom i s ed , j o l ted out of ex i s ten ce by tri ll i ons of gi ga bytes flashing
across the ether of cyberspace. Cyberspace, the story went, could only be free. Freedom was its nature.

But why was never made cl e a r. That c y bers pa ce was a place that govern m en t s
could not control was an idea that I never quite got. The word itself speaks not of
f reedom but of con tro l . Its etym o l ogy re aches beyond a novel by Wi lliam Gibson
(Neuromancer, published in 1984) to the world of "cybernetics," the study of control
at a distance.3 Cybernetics had a vision of perfect regulation. Its very motivation was
finding a better way to direct. Thus,it was doubly odd to see this celebration of noncontrol over architectures born from the very ideal of control.

As I said,I am a constitutionalist.I teach and write about constitutional law. I bel i eve that these first thoughts abo ut govern m ent and cybers p ace are just as misguided u i ded as the first thoughts abo ut govern m ent after com mu n i s m . L i berty in
cyberspace will not come from the absence of the state. Liberty there, as anywhere,
will come from a state of a certain kind.4 We build a world where freedom can flourish not by removing from society any self-conscious control; we build a world where
freedom can flourish by setting it in a place where a particular kind of self-conscious
con trol su rvive s . We build liberty, that is, as our fo u n ders did, by set ting soc i ety
upon a certain constitution.

But by "constitution" I don't mean a legal text. Unlike my countrymen in Eastern
Europe, I am not trying to sell a document that our framers wrote in 1787. Rather,
as the British understand when they speak of their constitution, I mean an architec -
ture—not just a legal text but a way of life—that structures and constrains social and
legal power, to the end of protecting fundamental values—principles and ideals that
reach beyond the compromises of ordinary politics.

Con s ti tuti ons in this sense are bu i l t , t h ey are not fo u n d . Fo u n d a ti ons get laid,
they don't magically appear. Just as the founders of our nation learned from the anarchy that followed the revolution (remember: our first constitution, the Articles of
Confederation, was a miserable failure of do-nothingness),so too are we beginning
to see in cyberspace that this building, or laying, is not the work of an invisible hand.
There is no reason to believe that the grounding for liberty in cyberspace will simp ly em er ge . In fact , as I wi ll argue, qu i te the oppo s i te is the case. As our fra m ers
learned,and as the Russians saw, we have every reason to believe that cyberspace,left

to itself, will not fulfill the promise of freedom. Left to itself,cyberspace will become
a perfect tool of control.5

Co n trol . Not nece s s a ri ly con trol by govern m en t , and not nece s s a ri ly con trol to
s ome evi l , fascist en d . But the argument of this book is that the invi s i ble hand of
c ybers p ace is building an arch i tectu re that is qu i te the oppo s i te of what it was at
c ybers p ace's bi rt h . The invi s i ble hand, t h ro u gh com m erce , is con s tru cting an arch i tectu re that perfects con trol—an arch i tectu re that makes po s s i ble high ly ef f ic i ent reg u l a ti on . As Vern or Vi n ge warn ed in 1996, a distri buted arch i tectu re of
reg u l a tory con tro l ; as Tom Mad dox ad ded , an axis bet ween com m erce and the
s t a te .6

This book is about that change,and about how we might prevent it. When we see
the path that cyberspace is on—an evolution I describe in part 1—we see that much
of the "liberty" present at cyberspace's founding will vanish in its future. Values that
we now con s i der fundamental wi ll not nece s s a ri ly rem a i n . Freedoms that were
foundational will slowly disappear.

If the original cyberspace is to survive, and if values that we knew in that world
are to remain, we must understand how this change happens,and what we can do in
re s pon s e . That is the aim of p a rt 2. Cybers p ace pre s ents som ething new for those
who think about regulation and freedom. It demands a new understanding of how
regulation works and of what regulates life there. It compels us to look beyond the
traditional lawyer's scope—beyond laws, regulations, and norms. It requires an account of a newly salient regulator.

That regulator is the obscurity in the book's title—Code. In real space we recogn i ze how laws reg u l a te — t h ro u gh con s ti tuti on s , s t a tute s , and other legal code s . In
c ybers p ace we must understand how code reg u l a te s — h ow the sof t w a re and hardware that make cyberspace what it is regulate cyberspace as it is. As William Mitchell
puts it, this code is cyberspace's "law."7 Code is law.

This code pre s ents the gre a test threat to liberal or libert a rian ide a l s , as well as
their greatest promise. We can build, or architect, or code cyberspace to protect values that we bel i eve are fundamen t a l , or we can bu i l d , or arch i tect , or code cybers p ace to all ow those va lues to disappear a r. Th ere is no middle gro u n d . Th ere is no
choice that d oes not include some kind of building. Code is never found; it is only
ever made, and only ever made by us. As Mark Stefik puts it,"Different versions of
[cyberspace] support different kinds of dreams. We choose, wisely or not."8

My argument is not for some top - down form of con tro l ; my claim is not that
regulators must occupy Microsoft. A constitution envisions an environment; as Justice Holmes said, it "call[s] into life a being the development of which [can not be]
fore s een ."9 Thu s , to speak of a con s ti tuti on is not to de s c ri be a on e - hu n d red - d ay
plan. It is instead to identify the values that a space should guarantee. It is not to describe a "government";it is not even to select (as if a single choice must be made) between bottom-up or top-down control. In speaking of a constitution in cyberspace
we are simply asking: What va lues are pro tected there? What va lues wi ll we bu i l d
into the space to encourage certain forms of life?

c o d e i s l a w

The "values" here are of two sorts—substantive and structural. In the American
trad i ti on , we worried ed abo ut the second firs t . The fra m ers of the Con s ti tuti on of
1787 (enacted without a Bill of Rights) were focused on structures of government.
Their aim was to ensure that a particular government (the federal government) did
not become too powerful. And so they built into its design checks on the power of
the federal government and limits on its rea ch over the states.

Opponents of that Constitution insisted that more checks were needed, that the
Constitution needed to impose substantive limits on government's power as well as
structural limits. And thus the Bill of Rights was born. Ratified in 1791, the Bill of
Rights promised that the federal government will not remove certain protections—
of speech, privacy, and due process. And it guaranteed that the commitment to these
su b s t a n tive va lues wi ll remain de s p i te the passing fancy of n ormal govern m en t .
These values were to be entrenched, or embedded,in our constitutional design;they
can be changed, but only by changing the Constitution's design.

These two kinds of protection go together in our constitutional tradition. One
would have been meaningless without the other. An unchecked structure could easily have overturned the substantive protections expressed in the Bill of Rights, and
wi t h o ut su b s t a n tive pro tecti on s , even a balanced and reflective govern m ent co u l d
have violated values that our framers thought fundamental.

We face the same questions in constituting cyberspace, but we have approached
them from an opposite direction. Already we are struggling with substance: Will cyberspace promise privacy or access? Will it preserve a space for free speech? Will it
facilitate free and open t rade? These are choices of substantive value, and they are
the subject of much of this book.

But structure matters as well. What checks on arbitrary regulatory power can we
build into the design of the space? What "checks and balances" are possible? How do
we sep a ra te powers? How do we en su re that one reg u l a tor, or one govern m en t ,
doesn't become too powerful?

Theorists of cyberspace have been talking about these questions since its birth. 10
But as a culture, we are just beginning to get it. We are just beginning to see why the
architecture of the space matters—in particular, why the ownership of that architecture matters. If the code of cyberspace is owned (in a sense that I describe in this
book), it can be controlled; if it is not owned, control is much more difficult. The
lack of ownership, the absence of property, the inability to direct how ideas will be
used—in a word, the presence of a commons—is key to limiting, or checking, certain forms of governmental control.

One part of this question of ownership is at the core of the current debate between open and closed source software. In a way that the American founders would
have instinctively understood, "free software" or "open source software"—or "open
code," to (cowardly) avoid taking sides in a debate I describe later—is itself a check
on arbitrary power. A structural guarantee of constitutionalized liberty, it functions
as a type of separation of powers in the American constitutional tradition. It stands
a l on gs i de su b s t a n tive pro tecti on s , l i ke freedom of s peech or of the pre s s , but its

stand is more fundamental. As I argue by the end of this book, the first intuition of
our founders was right:structure builds substance. Guarantee the structural (a space
in cyberspace for open code), and (much of) the substance will take care o f itself.

In part 3, I bring these questions back down to the ground. I consider four areas
of con trovers y — i n tell ectual property, privac y, f ree speech , and soverei gn ty — a n d
i den tify va lues within each that are now at ri s k . The interacti on bet ween law and
code helps constitute these values. My aim is to show how we might respond to the
risk, using the tools from part 2.

That's the hopeful part. My final part is not.I end by asking whether we—meaning Americans—are up to the challenge that these choices present. Given our pres ent trad i ti on in con s ti tuti onal law and our pre s ent faith in repre s en t a tive
government,are we able to respond collectively to the changes I will have described?
My strong sense is that we are not. We are at a stage in our history when we urgently need to make fundamental choices about values, but we trust no institution
of government to make such choices. Courts cannot do it, because as a legal culture
we don't want co u rts ch choosing among con te s ted matters of va lu e s , and Con gre s s
should not do it because, as a political culture, we so deeply question the products
of ordinary government.

Change is possible.I don't doubt that revolutions remain in our future; the open
code movement is just such a revolution. But I fear that it is too easy for the government to dislodge these revolutions, and that too much will be at stake for it to allow
the revo luti on a ries to su cceed . Our govern m ent has alre ady cri m i n a l i zed the core
ethic of this movement, transforming the meaning of hacker into something quite
alien to its original sense. This, I argue, is only the start.

Things could be different. They are different elsewhere. But I don't see how they
could be different for us just now. This no doubt is a simple confession of the limits
of my own imagination.I would be grateful to be proven wrong. I would be grateful
to watch as we rel e a rn—as the citi zens of the form er Com munist rep u republics are
learning—how to escape our disabling ideas about the possibilities for governance.
I begin in the first chapter with four stories about cyberspace, which will set out
four themes to guide the balance of the book. These themes describe what is different here. Even if despair about governance is the same, at least these things are different.

T W O

f o u r p u z z l e s f r o m c y b e r s p a c e

Most peopl e t h ink t h at t o under st and l aw, you need t o under st and a set of
ru l e s . Th a t's a mistake , as Stanley Fish taught us.1 The law is best unders tood
through stories—stories that teach what is later summarized in a catalog of rules.

So it is with stories that I begin. Each (there are four) captures a theme that recurs throughout the book.Each is meant both to orient and to disorient—that is, to
show ways in which cyberspace is both like and unlike real space. At the end of this
chapter, I come clean about the themes and provide a map. For now, just focus on
the stories.

B O R D E R S

It was a very ordinary dispute, this argument between Martha Jones and her neighbors .2 It was the sort of d i s p ute that people have had since the start of n ei gh borh ood s . It didn't begi n , this particular dispute ,
in anger. It began with a
misunderstanding. In this world, misunderstandings like this are far too common.
Ma rtha thought abo ut that as she won dered wh et h er she should stay. Th ere were
other places she could go. Leaving would mean abandoning what she had built, but
frustrations like this were beginning to get to her. Maybe,she thought,it was time to
move on.

The argument was about borders—about where her land stopped. It seemed like
a simple idea, one you would have thought the powers-that-be would have worked
out many years before. But here they were,her neighbor Dank and she, still fighting
about borders. Or rather, about something fuzzy at the borders—about something
of Martha's that spilled over into the land of others. This was the fight, and it all related to what Martha did.

Martha grew flowers. Not just any flowers, but flowers with an odd sort of power.
They were beautiful flowers,and their scent entranced. But however beautiful, these

1 0

flowers were also poisonous. For this was Martha's weird idea: to make flowers of extraordinary beauty which,if touched, would kill.Strange no doubt,no one said that
Martha wasn't st range. She was unusual, as was this neighborhood. But sadly, disputes like this were not.

The start of the argument was predictable enough. Martha's neighbor, Dank,had
a dog. Dank's dog died. And of course,the dog died because it had eaten a petal from
one of Martha's flowers. A beautiful petal, and now a dead dog. Dank had his own
ideas about these flowers, and about this neighbor, and he expressed those ideas—
perhaps with a bit too much anger, or perhaps with anger appropriate to the situation.

"Th ere is no re a s on to grow de adly flowers ," Dank yell ed ac ross the fen ce .
"There's no reason to get so upset about a few dead dogs," Martha replied. "A dog
can always be replaced. And anyway, why have a dog that suffers when dying? Ge t
yourself a pain-free dog, and my petals will cause no harm."

I came into the argument at about this time. I was walking by, in the way one
walks in this space. (Some would say I was teleporting, but we needn't complicate
the story with jargon. Let's just say I was walking.) I saw the two neighbors getting
increasingly angry with each other. I had heard about the disputed flowers—about
how some petals carried their poison. It seemed to me a simple problem to solve, but
I guess it's simple only if you understand how problems like this get made.

Dank and Martha were angry because in a sense they were stuck. Both had built
a life in the neighborhood, invested many hours there, and come to understand its
limits. This is a common condition: we all build our lives in places with limits. We
all are disappointed at times. What was different about Dank and Martha?

One difference was the nature of the space, or context, where their argument was
h a happening i n g. This was not "real space" but a kind of vi rtual space . It was "Ava t a r
space," and Avatar space is quite different from the space we call real.3

Real space is the place where you are just now: your office, your den, maybe a
pool. It's a world defined by both laws that are man-made and others that are not.
"Limited liability" for corporations is a man-made law. It means that the directors of
a corporation (usually) cannot be held personally liable for the sins of the company.
Limited life for humans is not a man-made law: we all will die. In real space our lives
are subject to both sorts of law, though in principle we could change one sort.

But there are other sorts of l aws in real space as well . You bo u ght this boo k , I
tru s t , or you borrowed it from som eone who did. If you stole it, you are a thief ,
wh et h er you are caught or not. Social norms define our language ; our language
would define you as a thief , and not just because you took som et h i n g. Th ere are
plenty of ways to take something but not be thought of as a thief. If you and a group
of friends come across a pile of money blowing in the wind,taking a few dollars will
not make you a thief; indeed,not taking a few dollars might make you a chump. But
stealing this book from the bookstore (even when there are so many left for others)
marks you as a thief. Social norms make it so, and we live life subject to these norms.

1 1

Some of these norms can be changed collectively, even if not individually. I can
choose to burn my draft card, but I cannot choose whether doing so will make me a
hero or a traitor. I can refuse an invitation to lunch, but I cannot choose whether doing so will make me rude. I have choices in real life, but escaping the consequences
entailed by these laws is not one of my choices. These laws constrain us in ways that
are so familiar as to be all but invisible.

Avatar space is different. It is, first of all,a virtual space—like a cartoon on a television screen. But unlike a cartoon, avatar space enables you to control the characters on the screen in real ti m e . At least, you con trol you r ch a racter — one amon g
many characters controlled by many others in this space. One builds the world one
wi ll inhabit here . As a ch i l d , you grew up learning the physics that govern ed the
world of Roadrunner and Wile E. Coyote (violent but forgiving); your children will
grow up m a k i n g the world of Road ru n n er and Wile E. Coyote te (sti ll vi o l en t , but
maybe not so forgiving). They will define the space and then live out the story. Their
choices will make the laws of that space real.

This is not to say that Avatar space is unreal. There is real life in Avatar space,
con s ti tuted by how people interact . The space is wh ere people interact — mu ch as
they interact in real space no doubt, but with some important differences. In Avatar
space the interaction is in a virtual medium. In 1990s speak,the interaction is in cyberspace. People "jack" into these virtual spaces. They do things there.

The things people do there are highly varied. Some simply get together and gab:
they appear (in a form they select, with qualities they choose and biographies they
h ave wri t ten) in a vi rtual room and type messages to each other. Or they walk
around (again, the ambiguity is not a slight one) and talk to people. My friend Rick
does this as a cat—a male cat, he insists. As a male cat, Ri ck parades around this
space and talks to anyone who's interested. He aims to flush out the cat-loving sorts.
The rest, he reports, he punishes.

Others do much more in Avatar space than gab. Some, for example, homestead.
Depending on the world and its laws, citizens are given plots of undeveloped land,
which they hold as long as they develop them. People spend extraordinary amounts
of time building a life on these plots. ( Is n't it ex tra ord i n a ry the way these peop l e
waste time? While you and I spend up to seventy hours a week working for firms we
don't own and building futures we're not sure we'll enjoy, these people are designing
and building things and making a life, even if only a virtual one.Scandalous.) They
build houses—by de s i gning and then con s tru cting them — h ave family or fri en d s
move in, and pursue hobbies or raise pets. They may grow trees or odd plants—like
Martha's.

Avatar space grew out o f "MUD" or "MOO" space.4 MUDs and MOOs are virtual worlds as well, but they are text-based virtual worlds. There are no pictures or
c a cartoons on a MUD or MOO screen , just tex t , reporting what som eone says and
does. You can construct objects in these spaces and have them do things, but the objects act only through the mediation of text. (Their actions are generally quite sim-

1 2

ple, but even simple can be quite funny. One year, in a MUD that was part of my cyberl aw cl a s s , s om eone built a ch a racter named JPo s n er. If you po ked JPo s n er, h e
mut tered , " Poking is inef f i c i en t ." An o t h er ch a racter was FEasterbroo k . Stand in a
room with FEasterbrook and use the word "f a i r," and FEasterbrook would repe a t
what you said, substituting the word "efficient.""It's not fair" became "You mean,it's
not efficient.")

Al t h o u gh it was easy for people who liked texts or who wro te them to understand the attraction of these text-based realities, and to see how they could constitute a reality, it was not so easy for the many people who didn't have that fondness
for texts. But there is no such limitation in Avatar space. It is the movie version of a
cyberspace novel. You build things here,and they survive your leaving. You can build
a house,and people walking down the street see it. You can let them come in,and in
coming into your house, they see things about you. Or they can see how you construct your world. If the particular Avatar space permits it, they can see how you've
ch a n ged the laws of the real worl d . In real space , for instance , people slip on wet
floors, but in the space you've built that law may not exist.

Here we get back to Martha and Dank. In their exchange—when Martha blamed
Dank for having a dog that died with pain—they reve a l ed what is amazing abo ut
this space. Martha's remarks ("Why do you have a dog that suffers when dying? Get
yourself a pain-free dog, and my petals will cause no harm") may have struck you as
odd. You may have thought,"How weird that someone would think that the fault lay
not in the poison petals but in a dog that died with pain." But in this space Dank did
have a choice about how his dog would die. Maybe not a choice about whether "poison" would "kill" a dog, but a choice about whether the dog would suffer when it
died. He also had a choice about whether a copy of the dog could be made, so that
if it died it could "come back to life." In Avatar space these possibilities are not given
by God. Or rather, if they are defined by God, then we are God. The possibilities in
Avatar space are determined by the code—the software, or architecture, that makes
the Avatar space what it is. "What happens when" is a statement of logic; it asserts a
rel a ti onship that is manifested s ted in code . In real space we don't make mu ch of t h e
code. In Avatar space we do.

So, when Martha said what she said about the dog, Dank made what seemed to
me an obvious re s pon s e . "Why do your flowers have to stay poi s onous on ce they
leave your land? Why not make the petals poisonous only when on your land? When
they leave your land—when, for example, they are blown onto my land—why not
make them harmless?"

It was an idea, but it didn't really help. For Martha made her living selling these
poisonous plants. Others too liked the idea of this art tied to death. So it was not a
solution to make poisonous plants that were poisonous only on Martha's property,
unless Ma rtha was also intere s ted in co ll ecting a lot of very wei rd people on her
land.

But the idea did suggest another. "Okay," said Dank, "why not make the petals
poi s onous on ly wh en in the po s s e s s i on of s om eone who has purch a s ed them? If

1 3

they are stolen, or if they blow away, then let the petals lose their poison. But when
kept by the owner of the plant, let the p petals keep their p oison. Isn't that a solution
to the problem that both of us face?"

The idea was ingenious. Not only did it help Dank; it helped Martha as well. For
the code,as it existed,did allow theft.(People want reality in that virtual space;there
will be time enough for heaven later.) But if Martha could modify the code slightly
so that theft rem oved a plant's va lu e , that ch a n ge would pro tect the profit in her
plants as well as Dank's dogs. Here was a solution that made both neighbors better
off—what economists call a pareto superior move.5 And it was a solution that was as
possible as any other. All it required was a change of code.

Think for a second about what's involved here. "Theft" entails (at minimum) a
change in possession. But in Avatar space "possession" is just a relation defined by
the software that defines the space. That same code must also define the properties
that possession yields. It must distinguish, for example, between having a cake and
eating it. In both cases you "possess" the cake, but in the se cond case what you possess must change over time. With each "bite," you possess less.

So why not the same solution to Martha and Dank's problem? Why not define
ownership to include the quality of poisonousness, and possession without ownership to be po s s e s s i on wi t h o ut poi s on? Ra t h er than re s o lve the dispute bet ween
Ma rtha and Dank by making one of t h em ch a n ge his or her beh avi or, why not
change the laws of nature to eliminate the conflict altogether?

We're a short way into this rel a tively short boo k , and what I'm abo ut to say may
make it a very short book indeed (for you at least). This book is all about the question raised by this simple story, and about the simplicity in this apparently simple
answer. This is not a book about Avatar space; the story about Martha and Dank is
the first and last example that will include Avatars. But it is a book about cyberspace.
My claim is that cyberspace will raise precisely the questions that Martha and Dank
confronted, as well as the questions that their solution raised. What does it mean to
live in a world where problems can be programmed away? And when,in that world,
should we program problems away?

It is not Avatar space that makes these questions interesting problems for law; the
very same probl ems wi ll arise out s i de of Avatar space , and out s i de MUDs and
MOOs. The problems of these spaces are problems of cyberspace generally, and as
more of our life becomes wired, these questions will become more pressing.

But I have learned enough in this business to know that I can't convince you of
this with an argumen t . ( I 've spent the last five ye a rs talking abo ut this su bj ect ; a t
least I know what doesn't work.) If you see the point, good for you. If you don't, I
must show you. So my method for readers of the second sort must be more indirect.
Proof, for them, will come in a string of stories, which aim to introduce and disorient. That, again, is the purpose of this chapter. Out of confusion, something useful
will emerge.

Let me describe a few other places, and the oddities that inhabit them.

1 4

G O V E R N O R S

A state — c a ll it " Bora l " — doe s n't like ga m bl i n g, even though some citi zens like to
gamble. But the state is the boss; the people have voted; the law is as it is. Gambling
in the state of Boral is illegal.

Then comes the Internet. With the Net wired into their phones, some citizens of
Boral decide that Internet gambling is the next "killer app." Someone sets up servers
that provide access to online gambling. The state doesn't like this business; the business e s s m en are just ill egal ga m bl ers . S hut down your servers , the attorn ey gen era l
warns, or we will lock you up.

Wise even if dishonest,the gamblers agree to shut down their servers in the state
of Bora l . But they don't exit the ga m bling bu s i n e s s . In s te ad , t h ey rent space on a
server in an "offshore haven." This offshore web server hums away, once again making gambling available on the Net.

And just as available to people in Boral. For here's the important point: given the
architecture of the Internet (at least as it was), it doesn't matter where in real space
the server is set up. Access doe s n't depend on geogra phy. Nor, depending on how
clever the gambling sorts are, does access require that the user know anything about
who owns or runs the real server. The user 's access can be passed thro u gh
anonymizing sites that make it practically impossible in the end to know what went
where.

The Boral attorn ey gen eral faces a difficult probl em . She may have moved the
gamblers out of her state, but she hasn't succeeded in reducing gambling on the Net.
She once would have had a group of people she could punish, but now she has made
t h em essen ti a lly free from punishmen t . The world for this attorn ey gen eral has
changed. By going online, the gamblers moved into a world where behavior, so the
argument goes, is no longer regulable.

Reg u l a bl e . I am told there is no su ch word , t h o u gh law yers app a ren t ly do not
k n ow that fact . By "reg u l a bl e" I mean simply that a certain beh avi or is capable of
regulation. The term is comparative, not absolute—in some place, at some time, a
certain behavior will be more regulable than at another place and in another time.
My claim abo ut Boral is simply that the Net makes ga m bling less reg u l a ble there
than it was before the Net.

J A K E ' S C O M M U N I T I E S

If you had met Jake at a party in Ann Arbor (were Jake at a party in Ann Arbor), you
would have forgotten him.6 If you didn't forget him, you might have thought, here's
another quiet, dweeby University of Michigan undergraduate, terrified of the world,
or at least of people in the world.

You wouldn't have figured Jake for an author—and quite a famous short-story
author, within his circle at least. Jake was a char acter in his own stories, yet who he

1 5

was in his stories was quite different from who he was in "real" life. If, that is, after
reading his stories you still thought this distinction between "real life" and "not real
life" made much sense.

Jake wrote stories about violence—about sex as well, but mainly about violence.

They seethed with hatred, especially of women.

In real space Jake had quite successfully hidden this propensity. He was one of a
million boys: unremarkable, indistinguishable, harmless. Yet however inoffensive in
real space , his harmfulness in cybers p ace was incre a s i n gly well known . His stori e s
were published in USENET, in a group called alt.sex.stories.

U S E N E T is a part of most spaces on the Net . It isn't a net work , except in the
sense that the personal ads of a national newspaper are a network. It is a protocol—
a set of rules named the net news transfer protocol (NNTP)—for exchanging messages intended for public viewing. These messages are organized into "newsgroups,"
and the newsgroups are organized into subjects. Most of the subjects are quite technical. Many are related to hobbies. Some are related to sex. Some messages in the sex
n newsgroups come with attach ed files that can be converted to pictu re s . But som e ,
like Jake's, are simply stories.

There are thousands of newsgroups, each carrying hundreds of messages. Anyone with access to a USENET server can get access to the messages (or at least to the
ones his administrator wants him to read), and anyone with access can post a mess a ge or re s pond to one alre ady po s ted . Im a gine a public bu ll etin boa rd on wh i ch
people post questions or comments. Anyone can read the board and add his or her
own though t s . Now imagine fifteen thousand boa rd s , e ach with hu n d reds of
"t h re ad s" ( s tri n gs of a r g u m en t s , e ach ti ed to the nex t ) . Th a t , in any one place , i s
U S E N E T. Now imagine these fifteen thousand boa rd s , with hu n d reds of t h re ad s
each, on millions of computers across the world. Post a message in one group, and it
is added to that group's board everywhere. That, for the world, is USENET.

Jake, as I said, posted to a group called alt.sex.stories. "Alt" in that name refers to
the hierarchy that the group sits within. There were seven primary hierarchies.7 Alt
was created in reaction to the initial se ven: groups are added to the seven through a
formal voting process among participants in the groups, but groups are added to alt
based solely on whether administrators choose to carry them. Usually, administrators will carry them if they are popular.

Am ong these groups that are carri ed on ly on dem a n d , a l t . s ex . s tories is qu i te
pop u l a r. As with any wri ting space , i f s tories are "good " by the standards of t h e
s p ace — i f t h ey are stories that users of the space dem a n d — t h ey are fo ll owed and
their authors become well known. Lots of trash is sputtered out on USENET, but if
a writer is known to write valuable stuff,his or her trash will be sifted out.

Jake's stuff was valuable in this sense. His stories, about kidnapping, torturing,
raping and killing wom en , were as gra phic and rep u l s ive as any su ch story co u l d
be—which is w hy Jake was so famous among like-minded sorts. He was a supplier
to these people, a constant and consistent fix. They needed these accounts of innocent women being violated. Jake supplied them for free.

1 6

One night in Moscow, a sixteen-year-old girl read a story by Jake. She showed it
to her father, who showed it in turn to Richard DuVal,a Michigan alum. DuVal was
shocked at the story, and angry that it bore the tag "umich.edu" on the account. He
called his alma mater and complained. They took the complaint seriously.8

The university contacted the police;the police contacted Jake with handcuffs and
a jail cell. A slew of doctors examined Baker. Some concluded that he was a threat.
The government agreed with them, especially after it seized his computer and discovered e-mails between Jake and a Canadian fan who was planning to execute in
real space one of the stories published in cyberspace. At least,that's what the e-mails
said. No one could tell for certain what the two men intended. Jake said it was all
pure fiction, and indeed, there was no evidence that the words had ever described
something that was not purely fictional.

Federal charges were brought against Jake, for the transmission of a threat. Jake
said that his stories were only words, protected by the First Amendment to the U.S.
Con s ti tuti on . A month and a half l a ter a co u rt agreed , and the ch a r ges were
dropped.9

I don't care so mu ch just now abo ut wh et h er Ja ke Ba ker 's words should have
been pro tected by the Con s ti tuti on .1 0 My con cern is Ja ke Ba ker himsel f , a pers on
normed into apparent harmlessness by real-space society but set free in cyberspace
to become the aut h or of this vi o l en ce . People said Ja ke was brave , but he wasn't
"brave" in real space. He didn't express his hatred in classes, among friends, or in the
school newspaper. He slithered away to cyberspace, and only there did his deviancy
flourish. He could do that because of something about him, and because of something about cyberspace.

Ja ke was in ef fect an aut h or and publ i s h er in on e . He wro te stori e s , and as
quickly as he finished them he published them—to some thirty million computers
across the world within a few days. His potential audience was larger than twice that
for the top fifteen best-selling novels combined, and though he made nothing from
his work, the demand for it was high. Jake had discovered a way to mainline his depravity into the veins of a public for whom this stuff was otherwise quite difficult to
find.(Even Hustler wouldn't publish the likes of this.)

Of course, there were other ways Jake could have published. He could have offered his work to Hustler, or worse. But no real-world publication would have given
Ja ke a com p a ra ble audien ce . Ja Jake's re adership was po ten ti a lly mill i on s , s stretching i n g
across country and continent, across culture and taste.

This re ach was made po s s i ble by the power in the net work :a nyone any wh ere co u l d
p u publish to everyon e , every wh ere . The net work all owed publ i c a ti on wi t h o ut fil teri n g,
ed i ti n g, or re s pon s i bi l i ty. One could wri te what one wanted , s i gn it or not, post it to
m achines ac ross the worl d , and within hours the words would be every wh ere . Th e
n et work rem oved the most important con s traint on speech in real space—the sep a rati on of p u bl i s h er from aut h or. Th ere is va n i ty publishing in real space , but on ly
the ri ch can use it to re ach a broad audien ce . For the rest of u s , real space affords
on ly the access that the publ i s h ers want to give us.

1 7

But the most significant feature of this story about Jake is how cyberspace perm i t ted him to escape the con s traints of real space . Cybers p ace is not, of co u rs e , a
place; you don't go anywhere when you are there. But it is also quite true that the
world Jake lived in when w riting was a spa ce quite different from the space he lived
in here. He was free there of real-life constraints. He was free of the norms and understandings that had successfully formed him into a member of a college commun i ty. Maybe he wasn't perfect ly at hom e ; m aybe he wasn't the happiest i e s t . But the
world of the University of Michigan had succeeded in steering him away from the
life of a psychopath—except when it g ave him access to the Net. On the Net he was
someone else.

W O R M S T H A T S N I F F

A "worm" is a bit of computer code that is spit out on the Net and works its way into
the systems of vulnerable computers. It is not a "virus" because it doesn't attach itself to other programs and interfere with their operation. It is just a bit of extra code
that does what the code writer says. The code could be harmless, simply sitting on
someone's machine. Or it could be harmful, corrupting files or doing other damage
that its author commands.

Imagine a worm designed to do good (at least in the minds of some). Imagine
that the code writer is the FBI and that the FBI is looking for a particular document
bel on ging to the Na ti onal Sec u ri ty Agency (NSA). Su suppose that this doc u m ent is
classified and illegal to possess without the proper clearance. Imagine that the worm
propagates itself on the Net, finding its way onto hard disks wherever it can; once on
a computer's hard disk,it scans the entire disk. If it finds the NSA document,it sends
a message back to the FBI saying as much. If it doesn't,it erases itself.Finally, assume
that it can do all this without "interfering"11 with the operation of the machine. No
one would know it was there;it would report back nothing except that the NSA document was on the hard disk. 12

Is the worm unconstitutional? This is a hard question that at first seems to have
an easy answer. The worm is engaging in a government-initiated search of citizens'
disks. There is no reasonable suspicion (as the law ordinarily requires) that the disk
holds the document for which the government is searching. It is instead a generalized, suspicionless search of private spaces by the government.

From the standpoint of the Constitution—the Fourth Amendment in particular—you don't get any worse than that. The Fourth Amendment was written against
the background of just this sort of abuse. Kings George II and George III would give
officers a "general warrant" authorizing them to search through private homes looking for evidence of a crime.13 No suspicion was needed before the officer ransacked
your house, but because he had a warrant, you were not able to sue the officer for
tre s p a s s . The aim of the amen d m ent was to requ i re at least su s p i c i on , so that the
burden of the search fell on a reasonably chosen class.14

1 8

But is the worm real ly the same as the King's general search? There is one important difference: unlike the victims of the general searches that the framers of our
Constitution were concerned about, the computer user never knows that his or her
disk is being searched by the worm. With the general search, the police were breaking into a house and rummaging through private stuff. With the worm,it is a bit of
computer code that does the breaking, and (I've assumed) it can see only one thing.
The code can't read private letters; it doesn't break down doors; it doesn't interfere
with ordinary life. And the innocent have nothing to fear.

The worm is silent in a way that King George's troops were not. It searches perfectly and invisibly, discovering only the guilty. It does not burden the innocent; it
does not trouble the ordinary citizen; it captures only what is outside the protection
of the law.

This difference complicates the constitutional question. The worm's behavior is
like a generalized search in that it is a search without suspicion, but it is unlike the
paradigm case of a generalized search in that it creates no disruption of ordinary life
and finds only contraband. In this way, the worm is like a dog sniff—which at least
at airports is constitutionally permissible without probable cause15—but better. Unlike the dog sniff, the worm doesn't even let the computer user know when there is
a search (and hence the user suffers no anxiety).

Is the worm,then, constitutional? That depends on your conception of what the
Fourth Amendment protects. On one view, the amendment protects against suspicionless i suspicion govern m ental inva s i on s , wh et h er those inva s i ons are bu rden s ome or not.
On a second view, the amendment protects against invasions that are burdensome,
allowing only those for which there is adequate suspicion that guilt will be uncovered. The paradigm case cited by the framers does not distinguish between these two
very different protections. It is we, instead, who must choose.

Let's take the example one step further. Imagine that the worm does not simply
search every machine it encounters but can be put on a machine only with judicial
authorization—say, a warrant. Now the suspicionless-search part of the problem has
been removed. But imagine a second part:the government requires that networks be
constructed so that a worm, with judicial authorization, could be placed on a machine. Machines in this regime must be worm-ready, even though worms will be deployed only with judicial war rant.

Is there any con s ti tuti onal probl em with this? I ex p l ore this qu e s ti on in mu ch
greater detail in chapter 11, but for now, notice its salient feature. In both cases, we
a re de s c ri bing a regime that all ows the govern m ent to co ll ect data abo ut us in a
highly efficient manner, that is,
inexpensively for both the government and the innocent. This efficiency is made possible by technology, which permits searches that
before would have been far too burdensome and far too invasive. In both cases,then,
the qu e s ti on comes to this: Wh en the abi l i ty to search wi t h o ut bu rden incre a s e s ,
does the government's power to search increase as well? Or more darkly, as James
Boyle puts it:"Is freedom inversely related to the efficiency of the available means of
surveillance? If so, we have much to fear."16

1 9

This question, of course, is not limited to the government. One of the defining
features of modern life is the emergence of technologies that make data collection
and processing extraordinarily efficient. Most of what we do—hence, most of what
we are—is recorded out s i de our hom e s . Wh en you make tel eph one call s , data are
recorded about whom you called, when, how long you spoke, and how frequently
you made su ch call s .1 7 Wh en you use your credit card s , data are recorded abo ut
wh en , wh ere , and from wh om you made purch a s e s . Wh en you take a fli gh t , yo u r
itinerary is recorded and, probably by the time this book reaches print, profiled by
the govern m ent to determine wh et h er you are likely to be a terrorist s t .1 8 No do u bt
Hollywood's image—of a world where one person sitting behind a terminal tracks
the life of another—is wrong. But not terribly wrong. It's not that systems so easil y
track a single individual. But it is easy to imagine an agency sorting through all the
data the system collects to identify those individuals most likely to be committing
crimes. The intrusiveness is slight, and the payoff great.

Both private and public monitoring, then, have the same salient feature: monitoring, or searching, can increase without increasing the burden on the individual
searched. How should we think about this change? How should the protection the
framers gave us be applied?

T H E M E S

Four stori e s , four them e s , e ach a wi n dow on to one aspect of c ybers p ace that wi ll
be cen tral in all that fo ll ows . My aim in the balance of this book is to work
t h ro u gh the issues ra i s ed by these four them e s . So then let me end this ch a pter
with a map of the fo u r, laid out in the order of the boo k . That order begins wi t h
s tory nu m ber two.

R e g u l a b i l i t y

Reg u l a bi l i ty means the capac i ty of a govern m ent to reg u l a te beh avi or within its
proper re ach . In the con text of the In tern et , that means the abi l i ty of the government to regulate the behavior of its citizens (and perhaps others as well) on the Net.
My second story, a bo ut ga m bling in Bora l , was thus abo ut reg u l a bi l i ty, or more
specifically, about the changes in regulability that cyberspace brings. Before the Intern et , it was rel a tively easy for the attorn ey gen eral of Boral to con trol ga m bl i n g
within her jurisdiction; after the Internet, when the servers moved outside of Boral,
regulation became much more difficult.

For the regulator, this story captures the problem that cyberspace presents genera lly. The arch i tectu re of c ybers p ace makes reg u l a ting beh avi or diffic u l t , bec a u s e
those whose behavior you're trying to control could be located in any place (meaning outside of your place) on the Net. Who someone is, where he is,and whether law
can be exercised over him there—all these are questions that government must an-

2 0

swer if it is to impose its will. But these questions are made impossibly difficult by
the architecture of the space—at least as it was.

The balance of part 1 is about this question of regulability. I ask whether "unregulability" is necessary. Can we imagine a more regulable cyberspace? And is this
the cyberspace we are coming to know?

R e g u l a t i o n b y C o d e

The story about Avatar space is a clue to answering the question about regulability.
If in Avatar space we can change the laws of nature—making possible what before
was impo s s i bl e , or making impo s s i ble what before was po s s i bl e — why can't we
change regulability in cyberspace? Why can't we imagine a cyberspace where behavior can be controlled?

For this, importantly, is just what Avatar space was. Avatar space is "regulated,"
though the regulation is special. In Avatar space regulation came through code. The
rules in Avatar space are imposed, not through sanctions, and not by the state, but
by the very arch i tectu re of the particular space . A law is def i n ed , not thro u gh a
statute, but through the code that governs the space.

This is the second theme of this book: there is regulation of behavior in cybers p ace , but that reg u l a ti on is impo s ed pri m a ri ly thro u gh code . What disti n g u i s h e s
different parts of cyberspace are the differences in the regulations effected through
code. In some places life is fairly free, in other places controlled, and the difference
between them is simply a difference in the architectures of control—that is, a difference in code.

If we combine the first two themes, we come to a central argument of the book:
the reg u l a bi l i ty de s c ri bed by the first theme depends on the cod e de s c ri bed in the
second. Some architectures of cyberspace are more regulable than others; some architectures enable b etter control than others. Thus, whether a part of cyberspace—
or cybers p ace gen era lly—can be reg u l a ted tu rns on the natu re of its code . It s
architecture will affect whether behavior can be controlled. To follow Mitch Kapor,
its architecture is its politics. 19

And from this an important point follows: if some architectures are more regulable than others—if some give government more control than others—then govern m ents should favor some arch i tectu res more than others , i f reg u l a bi l i ty is the
government's aim.

This fact is a threat to those who worry about governmental power; it is a reality
for those who would do something about governmental power. Some designs enable
govern m ent more than others ; s ome de s i gns en a ble govern m ent differen t ly; s om e
designs should be chosen over others.

It is here that questions of open source software matter. Among the designs that
enable or disable government's power to regulate, open code will hold an important
place. It will check,as I argue more extensively later, the top-down power of government while enabling an extremely effective scope for bottom-up control.

2 1

To restate theme two: the code is a regulator, and the government has a greater

interest in the code that regulates better than others.

C o m p e t i n g S o v e r e i g n s

But regulation by whom? Boral was just one state. Its problems were not the problems of its neighbors. And the rules we live by while in Boral, or while in a particular Avatar space, need not be the rules that we live by generally.

This was the issue ra i s ed most import a n t ly by Ja ke Ba ker. His story raises the
question of competing authority. Jake lived in Ann Arbor, Michigan. His life there
was subject to the norms of Ann Arbor, and he apparently adapted to these norms
re a s on a bly well . The aut h ori ty of that space govern ed Ja ke , and as far as anyon e
knew, it appeared to govern him exclusively.

But in cyberspace Jake's norms changed. When Jake went to cyberspace, his behavior changed. He was governed there by a set of norms different from the norms
that governed him in Ann Arbor.

The problem was that when he went to cyberspace,he never left Ann Arbor."Going" in cyberspace functions differently from "going" in real space. When you "go"
s om ewh ere in real space , you leave ; wh en you "go" to cybers p ace , you don't leave
anywhere. You are never just in cyberspace; you never just go there. You are always
both in real space and in cyberspace at the same time.

And so too with Jake. While sitting in a dorm at the University of Michigan, he
was able to teleport himself—in the only normatively significant sense—to a different world where the norms of civility and decency that governed outside his dorm
room did not obtain. Cyberspace gave Jake the chance to escape Ann Arbor norms
and to live according to the norms of another place. It created a competing authority
for Ja ke and gave him the ch a n ce to sel ect bet ween these com peting aut h ori ti e s
merely by switching his computer on or off.

Again, my point is not that no similar possibility exists in real space—it plainly
does. There is no doubt a Jake living in Hackensack, New Jersey (a suburban town
with suburban values), who drives every night into lower Manhattan and lives for a
few hours according to the "rules" of lower Manhattan. Those rules are not the rules
of Hackensack; that life is different. Like Ann Arbor Jake, the Hackensack Jake lives
under competing authorities. But between the lives of these two Jakes, there is a difference in degree that ripens into a difference in kind. The Ann Arbor Jake raises a
more significant problem for Ann Arbor than the Hackensack Jake raises for Hackensack. The differences are greater, and the effect more pervasive.

Nor should we think too narrowly about the competing normative communities
into which a Jake might move. The valences here are both positive and negative. It is
escape when a gay teen in Iowa can leave the norms of Iowa through a gay chat room
on America Online;20 it is escape when a child predator escapes the norms of ordinary society and engages a child in online sex.21 Both escapes are enabled by the architecture of cyberspace as we now know it.

2 2

The differen ce bet ween these two escapes is our vi ew abo ut the underlying n g
norm.I call the first escape liberating, and the second criminal. There are some who
would call both escapes cri m i n a l , and some who would call both libera ti n g. Th e
question isn't about name-calling, but about the consequences of living in a world
where we can occupy both sorts of space at the same time. Which sovereign should
govern?

L a t e n t A m b i g u i t y

The worm tells a different story sti ll . Th o u gh it is a tech n o l ogy for search i n g, t h e
worm functi ons differen t ly from searching in the ord i n a ry case. The ord i n a ry or
paradigm case is a search that carries costs: the burdens of the search, the insecurities it might create,the exposure it might make possible to invasions beyond a legiti m a te re ach .2 2 The worm erases those co s t s : the bu rden is gon e , the search is
( practi c a lly) invi s i bl e , and the searching tech n o l ogy is progra m m ed to find on ly
what is illegal. This is a search without the ordinary costs of a search, and it raises a
question about how such a search should, under the Constitution, be understood.

A fair view of the Constitution's protections could go in either of two ways. It
m ay be that we see the worm's inva s i on as incon s i s tent with the dign i ty that the
a m en d m ent was wri t ten to pro tect ,2 3 or it may be that we see the inva s i on of t h e
worm as so unobtrusive s ive as to be re a s on a bl e . The answer could be ei t h er, wh i ch
means that the change reveals a latent ambiguity in the original constitutional value.
Either answer is possible, so now we must choose one or the other.

You may not buy my story of the worm. You may think it is pure science fiction.
By the end of the book, however, I will convince you that there are any number of
cases in which a similar ambiguity troubles our constitutional past. In many of them
our Constitution yields no answer to the question of how it should be applied, because at least two answers are po s s i ble—that is, in light of the ch oi ces that the
framers actually made.

For Am eri c a n s , this ambi g u i ty cre a tes a probl em . If we lived in an era wh en
co u rts felt en ti t l ed to sel ect the answer that in the con text made the most sen s e ,
there would be no problem. Latent ambiguities would be answered by choices made
by judges—the framers could have gone either way, but we choose to go this way.

But we don't live in such an era, and so we don't have a way for courts to resolve
these ambiguities. As a result, we must rely on other institutions. My claim, a dark
one, is that we have no such institutions. If our ways don't change, our constitution
in cyberspace will be a thinner and thinner regime.

Cyberspace will present us with ambiguities over and over again. It will press this
question of how best to go on. We have tools from real space that will help resolve
the interpretive questions by pointing us in one direction or another, at least some
of the time. But in the end the tools will guide us even less than they do in real space
and time. When the gap between their guidance and what we do becomes obvious,

2 3

we will be forced to do something we're not very good at doing—deciding what we
want,and what is right.

My aim is not to lament choice. It is to highlight its nature and effect, as well as
an aspect of the transformation that we can expect this transformation in technology to create—one with which we, uniquely, are unable to reckon.

My aim is to use these four themes to understand cyberspace as it is,and cyberspace
as I believe it is becoming as it moves from a world of relative freedom to a world of
relatively perfect control. These themes will help us to see why and to understand
h ow we might re s pond to this tra n s form a ti on — h ow we might reclaim the va lu e s
that are important in this space, and how we might insist on bringing to it values
that are now absent.

T H R E E

i s - i s m

The ri se of an el e ctronic medium that disregards rds ge o graphical bou n d a ri e s
throws the law into disarray by c reating entirely new phenomena that need
to become the subject of clear legal rules but that cannot be governed, satisfactorily, by any current territorially based sovereign.

David Johnson and David Post,"Law and Borders—The Rise of Law in
Cyberspace," Stanford Law Review 48 (1996): 1367, 1375

Some things never ch a n ge about governing the Web. Most pro m i n ent is its
innate ability to resist governance in almost any form.

Tom Steinert-Threlkeld, "Of Governance and Technology,"
Inter@ctive WeekOnline, October 2,1998

Th er e's a meme about cyber space t h at mar ks nat ives f r om it s fir st g ener a -
tions—an idea that defines first-generation thought about the place. Cyberspace, it
is said, cannot be regulated. It "cannot be governed"; its "innate ability" is to resist
reg u l a ti on . That is its natu re , its essen ce , the way things are . Not that cybers p ace
cannot be broken, or that g overnment cannot shut it down. But if cyberspace exists,
so first-generation thinking goes, government's power over behavior there is quite
limited. In its essence, cyberspace is a space of no control.

Nature. Essence. Innate. The way things are. This kind of rhetoric should raise
su s p i c i ons in any con tex t . It should espec i a lly raise su s p i c i on here . If t h ere is any
place where nature has no rule, it is in cyberspace. If there is any place that is constructed, cyberspace is it. Yet the rhe toric of "essence" hides this constructedness. It
misleads our intuitions in dangerous ways.

i s - i s m

2 5

This is the fallacy of "is-ism"—to confuse how something is with how it must be.
There is certainly a way that cyberspace is. That much is true. But how cyberspace is
is not how cyberspace has to be. There is no single way that the Net has to be; no single architecture defines the nature of the Net. The possible architectures of something that we would call "the Net" are many, and the character of life within those
different architectures is diverse.

The next few chapters extend this point. But the argument can be summarized in
a single line: whether the Net is unregulable depends, and it depends on its architec -
ture.1

With some architectures, behavior on the Net cannot easily be controlled; with
others it can. With some it cannot be controlled through top-down regulation; with
others it can. Among the many possible architectures that the Net might have, the
aim of this part is to argue that it is evolving in a very particular direction: from an
unregulable space to one that is highly regulable. The "nature" of the Net might once
have been its unregulability; that "nature" is about to flip.

To see the flip, you must first see a contrast between two different cyber-places.

The contrast is a clue about how the Net could be made more regulable.

I don't mean the descriptions that follow to be technical; I don't offer them as
complete definitions of types of networks, or types of control. I offer them to illustrate—to sketch enough to see a far more general point.

C Y B E R - P L A C E S :

H A R V A R D V E R S U S

C H I C A G O

The In tern et was born at univers i ties in the Un i ted State s . Its first su b s c ri bers were
re s e a rch ers , but as a form of l i fe , its bi rth was its link to the univers i ty and univers i ty life . It swept stu dents on l i n e , p u lling them aw ay from a very different life
in real space . The Net was a legal intoxicant of co ll ege campuses in the mid-1990s.
As the New Yo rk Times co columnist J. C . Herz wro te in her first book abo ut cybers p ace :

Wh en I look up, i t's fo u r- t h i rty in the morn i n g. " No way." I look from the
cl ock to my watch . Way. I 've been in front of this screen for six hours , and it
s eems like no time at all . I 'm not even rem o tely ti red . D a zed and thirsty ty, but
not ti red . In fact , I 'm eu ph ori c . I stu f f a dishevel ed heap of tex textbooks k s , ph o tocop i ed arti cl e s , h i l i gh ters and notes into my back p ack and run like a madwoman up the con c rete step s , past the sec u ri ty guard , and out s i de into the
pred awn mist. . . .

I stop wh ere a wet walkway meets a dry one and stand for a sec . . . . [I] start
thinking abo ut this t h i n g that bu z zes around the en ti re worl d , t h ro u gh the
ph one lines, a ll day and all night lon g. It's ri ght under our noses and it's invi s-

2 6

i bl e . It's like Na rn i a , or Ma gri t te , or Star Tre k , an en ti re god d a m n ed worl d . Except it doe s n't phys i c a lly ex i s t . It's just the co ll ective consciousness of h owever
m a ny people are on it.

This really is outstandingly weird.2

But not all universities adopted the Net in the same way. The access they granted
was not the same;the rules they imposed were different.One example of this difference comes from two places I know quite well, though many other examples could
make the same point.

At the Un ivers i ty of Ch i c a go, i f you wanted access to the In tern et , you simply
connected your machine to jacks located throughout the university.3 Any machine
with an Et h ern et con n ecti on could be plu gged into these jack s . O n ce con n ected ,
your machine had full access to the In tern et — acce s s , that is, that was com p l ete ,
anonymous, and free.

The re a s on for this freedom was a dec i s i on by an ad m i n i s tra tor—the Provo s t ,
G eof f rey Ston e , a form er dean of the law sch ool and a prom i n ent free speech
s ch o l a r. Wh en the univers i ty was de s i gning its net , the technicians asked Ston e
whether anonymous communication should be permitted. Stone, citing the principle that the rules regulating speech at the university should be as protective of free
speech as the First Amendment, said yes: people should have the right to communicate at the university anonymously, because the First Amendment to the Constituti on guarantees n tees the same ri ght vi s - à - vis govern m en t s .4 From that policy dec i s i on
flowed the architecture of the University of Chicago's net.

At Ha rva rd the rules are differen t . If you plug your machine into an Et h ern et jack at
the Ha rva rd Law Sch oo l , you wi ll not gain access to the Net . You cannot con n ect yo u r
m achine to the net at Ha rva rd unless the machine is regi s tered — l i cen s ed , a pproved ,
veri fied .O n ly mem bers of the univers i ty com mu n i ty can regi s ter their mach i n e s .O n ce
regi s tered ,a ll interacti ons with the net work are mon i tored and iden ti fied to a parti c ular mach i n e ; the user agreem ent carries a warning abo ut this practi ce . An onym o u s
s peech on this net is not perm i t ted—it is against the ru l e s . Access can be con tro ll ed
b a s ed on who you are , and interacti ons can be traced based on what you did.

This de s i gn also arose from the dec i s i on of an ad m i n i s tra tor, one less foc u s ed than
G eof f rey Stone on the pro tecti ons of the First Am en d m en t . Con tro lling access was the
i deal at Ha rva rd ; f ac i l i t a ting access was the ideal at Ch i c a go. Ha rva rd chose tech n o l ogies that make con trol po s s i bl e , while Ch i c a go chose tech n o l ogies that fac i l i t a te acce s s .
These two networks differ in at least two important ways. First and most obviously u s ly, t h ey differ in the va lues they em brace .5 This differen ce is by de s i gn . At the
University of Chicago, First Amendment values determined network design. Different values determined Harvard's design.

But the two networks differ in a second way as well. Because access is controlled
at Harvard and identity is known, actions can be traced back to their root in the network. In the Chicago network the identity and actions of users cannot be known.
Monitoring, tracking, or following behavior at Chicago is harder than it is at Hari s - i s m

2 7

va rd . Beh avi or in the Ha rva rd net work is more con tro ll a ble than beh avi or in the
University of Chicago network.

The networks thus differ in the extent to which they make behavior within each
n et work reg u l a bl e . This differen ce is simply a matter of cod e—a differen ce in the
software. Regulability is not determined by the essential nature of these networks. It
is determined instead by their architecture.

These two networks are just two points on a spectrum of possible network design. At one extreme we might place the Internet—a network defined by a suite of
protocols that are open and nonproprietary and that require no personal identification to be accessed and used. (I describe this architecture more extensively in chapter 4.) At the other extreme are traditional closed, proprietary networks, which grant
access on ly to those with ex press aut h ori z a ti on ; con tro l , t h erefore , is ti gh t . In between are networks that mix elements of both the Harvard network and networks
that are In tern et - open and gen era lly acce s s i ble but that build on top of this open
pro tocol arch i tectu res that en a ble some degree of con tro l . These mixed net work s
add control to the Internet; they layer elements of control on top.

It is the middle kind of network that I focus on here. The network at the University of Chicago is the model of the Internet in, say, 1995—let's call it Net95. The
second is the model of any number of closed networks that both predate the Internet and still exist today—for example, the ATM network, which makes it possible to
get cash at 2:00 A.M. in Bogotá. The third—the middle type, the Harvard architecture—adds something to Net95. It layers on top of the Internet suite code that ena bles more con tro l .6 The code of this net work is not incon s i s tent with the
u n derlying pro tocols of the In tern et . It is sti ll based , in the language of the en engineers, in "TCP/IP," the name for the suite of protocols that define the Internet (see
chapter 4). But it adds to this suite a set of protocols that facilitate further control.
The Harvard network is the Internet-plus, where the "plus" adds the means of control. (Though here the control lies only in knowing who a user is, not in knowing
what content he or she is trafficking.)

All three de s i gns are com mu n i c a ti on net works that are "l i ke" the In tern et .
Th ey raise a qu e s ti on : Wh en we say that the In tern et is "u n reg u l a bl e ," wh i ch network are we de s c ri bing? And if we pick an unreg u l a ble net work , just why is it unreg u l a ble? What fe a tu res abo ut its de s i gn make it so? And could those fe a tu res be
d i f feren t ?

My point in aligning the three should be obvi o u s . If s ome net works are more
regulable than others, this is simply a function of the network's design. The design
of an unregulable network could be changed; it could be transformed into a regulable network. The key is to identify the features of the unregulable space and to imagine them changed to make the space more regulable.

Con s i der three fe a tu res of Net 9 5 's de s i gn that make it hard for a reg u l a tor to
control behavior there. From the perspective of the regulator, these features are "imperfections"—they limit the data that the Net collects, either about the user or about
the material he or she is using.

2 8

The first imperfection is information about users—in a word, credentials. Net95
has no way to verify who someone is, or more important, to verify features or attributes of the "someone" using the Net. Indeed, there is no way to verify that it is a
"someone" at all. In the words of the famous New Yorker cartoon of two dogs sitting
in front of a PC,"On the Internet,nobody knows you're a dog."7 You can use the Net
a n onym o u s ly. You could build a (ro ) bot to use the Net . No one need know yo u r
name, and there is no easy way to verify your age, your sex, or where you live. The
Net knows only as much as you choose to tell, and it cannot even verify that inf ormation.

The second imperfecti on is inform a ti on abo ut the data—the l a bel s or, a s
Nicholas Negroponte put it, the "headers."8 Just as we have no system for obtaining
verifiable information about the attributes of users, we have no system for obtaining
verifiable information about the data on the Net.Data are out there—search engines
report them to us—but there is no con s i s tent or uniform way to know what they
are. Pictures of flesh come across a screen, but the system cannot tell whether the
p i ctu res are medical ph o tos or porn ogra phy. Data abo ut bod i ly functi ons com e
across the wire, but the system cannot tell whether the data are from medical records
or a novel. Nothing puts the bits into context, at least not in a way that a machine
can use. Net95 had no requ i rem ent that data be label ed . " Packet s" of data are labeled, in the sense of having an address. But beyond that, the packets could contain
anything at all.

The final imperfection ties the first two together: because there is no simple way
either to know who someone is or to classify data,there is no simple way to make access to data depend on who the user is and on the data he or she wants access to. In
a word, there is no simple way to zone cyberspace.9 In real space we have all sorts of
zon i n gs . Ch i l d ren cannot en ter bars , m en cannot en ter wom en's bathroom s , t h e
badly dressed cannot enter a trendy club. In countless ways we make access to spaces
depend on who som eone is. But in the cybers p ace of Net 9 5 , because we cannot
know the credentials of the user or the nature of the data, we cannot easily condition access on the credentials or the data.

These imperfections make regulating the Net difficult. But from the perspective
of the anarchist,the libertarian, or the lover of the Net as it was,they are not imperfections at all. They are features. They do not disable something important from the
Net as it was; t h ey en a ble som ething important abo ut the Net as it was—liberty.
They are virtues of a space where control is limited, and they help constitute that
space. The constitution of Net95 is unregulability; these features of its code make it
so.

But Harvard shows the regulator how the "bugs" in Net95 might be eliminated.
The Net could know the credentials of the user and the nature of the data and still
be "the Net." The choice is not only between the Internet and a closed proprietary
network. Harvard suggests a middle way. Control could be layered onto the platform
of the Internet. Architectures of control could be layered on top of the Net to "correct"

i s - i s m

2 9

or el i m i n a te " i m perfecti on s" of con tro l . Arch i tectu res of c reden tials and arch i tectures that label could, in other words, facilitate architectures of control.10

That is the firs t , and very small , claim of this early ch a pter in a story abo ut
emerging control: architectures of control are possible; they could be added to the
Internet that we know.

But nothing yet shows how. What would g et us from the relatively unregulable

libertarian Net to a highly regulable Net of control?

This is the question for the balance of part 1. I move in two steps. In chapter 4,
my claim is that even without the government's help, we will see the Net move to an
a rch i tectu re of con tro l . In ch a pter 5, I sketch how govern m ent might hel p. Th e
trends promise a highly regulable Net—not the libertarian's utopia,not the Net your
father (or more likely your daughter or son) knew, but a Net whose essence is the
character of control.

A Net, in other words, that flips the Internet as it was.

F O U R

a r c h i t e c t u r e s o f c o n t r o l

My aim in t h e l ast ch apt er was t o cr ack one meme about t h e nat ur e of t h e
Net—that the Net has a nature, and that its nature is liberty. I argued instead that
the nature of the Net is set in part by its architectures, and that the possible architectures of cyberspace are many. The values that these architectures embed are differen t , and one type of d i f feren ce is reg u l a bi l i ty —a differen ce in the abi l i ty to
control behavior within a particular cyberspace. Some architectures make behavior
m ore reg u l a bl e ; o t h er arch i tectu res make beh avi or less reg u l a bl e . These arch i tectures are displacing architectures of liberty.

This chapter suggests how and why. In a nutshell: the why is commerce, and the
how is through architectures that enable identification to enable commerce. As the
Net is being remade to fit the demands of commerce, architectures are being added
to make it serve com m erce more ef f i c i en t ly. Reg u l a bi l i ty wi ll be a by - produ ct of
these changes. Or put differently, the changes that make commerce possible are also
changes that will make regulation easy.

I don't pick out commerce to pick on commerce. My argument is not that commerce is the enemy, nor that there is any necessary connection between commerce
and regulability.1 There is no doubt that commerce will flourish in the future of the
Internet, and no doubt that is a good thing. The presence of commerce in the Net's
future,however, does not mean that the Net of the future will be the same as the Net
of the past. Commerce will change the Net,and my aim in this chapter is to help us
understand how.

I D E N T I T Y A N D A U T H E N T I C A T I O N :

R E A L S P A C E

By " i den ti ty " I mean som ething more than just who you are . I mean all the fact s
about you that are true as well. Your identity, in this sense, includes your name, your

3 1

sex, where you live, what your education is, your driver's license number, your social
security number, your purchases on Amazon.com, whether you're a lawyer—and so
on.

"Authentication" is the process by which aspects of your identity become known.
Some become known wh en you reveal them ; o t h ers become known wh et h er yo u
choose to reveal them or not. Perfect authentication would mean that others know
for certain all the facts abo ut yo u ; h a happiness comes from others knowing a good
deal less.

In real space much about your identity is revealed whether you want it revealed
or not. Ma ny of the facts abo ut yo u , that is, a re a u to m a ti c a lly asserted and sel f -
authenticating. This is a fact about real-space life. If I walk into a bank, the teller will
know a lot about me even if I don't say a thing: he will know I'm a puffy, middle-aged ged wh i te guy with glasses and bl ondish hair; he wi ll know I'm not big and not
strong, though I am somewhat tall. He will know all this whether I want to tell him
or not.I could, in principle, try to hide some of these facts—I could put on a mask,
walk on stilts,and try to enter the bank incognito. But ifI did,I would be more likely
to get tackled by a security guard than to hide any feature about myself. Hiding usually does not hide itself very well; usually we reveal that we are hiding.

Other facts about me, however, are not automatically asserted or automatically
self-authenticating. Some facts you can learn only if I tell you ("I broke my leg when
I was six"); some you cannot authenticate without resorting to some other source—
credentials. The police officer wants a driver's license,not your word that you are authorized to drive. A law school wants a copy of your college transcript, not a lett er
from you telling them that you graduated at the top of your class.A bank wants the
deed on your house,not just a promise that you will repay the mortgage. In all these
cases, facts about you must be authenticated by a d document, and hence by an institution that stands behind the document.

Re a l - s p ace life thus carries with it this mix of a ut h en ti c a ting and aut h en ti c a ted
c reden ti a l s . Social life is a constant nego ti a ti on bet ween these different credentials a l s . In a small town , in a qu i eter ti m e , doc u m ents as creden tials were not terri bly
n ece s s a ry. You were known by your face , and your face carri ed with it a referen ce
( h eld in the com m on knowl ed ge of the com mu n i ty) abo ut your ch a racter. As life
becomes more anonym o u s , s ocial insti tuti ons must con s tru ct creden tials to aut h en ti c a te facts abo ut you that in an earl i er ti m e , or in a small er social worl d ,
would have been aut h en ti c a ted by the knowl ed ge of the com mu n i ty abo ut wh o
you are .

The point may be obvi o u s : the reg u l a bi l i ty of re a l - s p ace life depends on these
credentials. The fact that witnesses can identify who committed a crime, either because they know the pers on or because of s el f - a ut h en ti c a ting fe a tu res su ch as "h e
was a white male, six feet tall," enhances the ability of the state to regulate against
that crime. If criminals were invisible or witnesses had no memory, crime would increase. The fact that fingerprints are hard to change and can now be traced to convicted felons increases the likelihood that felons will be caught again. Relying on a

3 2

m ore ch a n ge a ble physical ch a racteri s tic would redu ce the abi l i ty of the po l i ce to
track repeat of fen ders . The fact that cars have license plates and are regi s tered by
their owners increases the likelihood that a hit-and-run driver will be caught. Without licenses,and without systems registering owners, it would be extremely difficult
to track car-related crime. In all these cases,and in many more, features of real-space
life make regulating real-space life possible.

The state, as one regulator, thus depends on these features being as they are. Often the state will intervene, either to ensure that these credentials remain usable as
credentials2 or to substitute new credentials when an earlier credential becomes useless. The state punishes counterfeiters of state documents as a way o f increasing the
reliability of state documents. The state issues other credentials (driver's licenses) to
increase the reliability of its verification.

This, then, is the nature of real-space regulation: much about who we are is revealed, and we have built institutions that can credential what cannot authentically
be revealed. Both social life and state regulation depend on this mix. And both react
as elements within this mix change.

I D E N T I T Y A N D A U T H E N T I C A T I O N :

C Y B E R S P A C E

Iden ti ty and aut h en ti c a ti on in cybers p ace are differen t . The In tern et is built on a
simple suite of protocols—the basic TCP/IP suite. The TCP/IP suite includes protocols for exchanging packets of data between two machines "on" the Net.3 (I explore
this idea in greater detail in chapter 8. For now, think of the packets as small packages of information wrapped in an envelope with an address stamped on the outs i de.) To exch a n ge these packet s , the sys tem needs at least two bits of d a t a — t h e
address of the machine from which the data are being sent, and the address of the
machine to which the data are being sent. These are called Internet protocol (IP) add re s s e s . Th ey look like this: 1 2 8 . 3 4 . 3 5 . 2 0 4 . Si m p l i fied brut a lly, a packet of data is
carried "to" and "from" these addresses as it works its way across the Internet.

These pro toco l s , h owever, reveal nothing abo ut the user of the In tern et , a n d
very little abo ut the data being exch a n ged . Al t h o u gh the IP ad d ress is su f f i c i ent to
m ove the data from one machine to another, it has no nece s s a ry con n ecti on to any
physical unit in the worl d . IP ad d addresses are vi rtual ad d re s s e s ; the vi rtual can
ch a n ge . Nor do the IP pro tocols tell us mu ch abo ut the data being sen t . In parti cu l a r, t h ey do not tell us who sent the data, f rom wh ere the data were sen t , to wh ere
( geogra ph i c a lly) the data are goi n g, for what purpose the data are going there , or
what kind of data they are . None of this is known by the sys tem , or know a ble by
us simply by looking at the data. From the pers pective of the net work , this other
i n form a ti on is unnecessary s s a ry su rp lu s . L i ke a daydreaming reaming postal worker, the network simply moves the data and leaves interpret a ti on of the data to the app l i c ati ons at ei t h er en d .

3 3

This minimalism in de s i gn is inten ti on a l . It ref l ects both a po l i tical dec i s i on
about disabling control and a technological decision about the optimal network design. The designers were not interested in advancing social control; they were concerned with network efficiency. Thus,this design pushes complexity out of the basic
Internet protocols, leaving it to the applications, or ends, to incorporate any sophistication that a par ticular service may require.4

When this basic protocol is translated into Internet access—when, for instance,
you are browsing a web page—this minimal identification means that the server delivering the web page knows nothing about you from the Internet protocol itself. (We
will consider later how it does learn things about you from other applications that
sit on top of the Internet protocol.) The web server simply knows that you are located on the Internet at an IP address, and that you are coming onto the Net with a
TCP/IP-compliant protocol.

It is as if you were in a carnival funhouse, with the lights dimmed to darkness
and voices coming from around you, but from people you do not know and from
places you cannot identify. The system knows that there are entities out there interacting with it, but it knows nothing abo ut who those en ti ties are . Wh ereas in re a l
s p ace—and here is the important poi n t — a n onym i ty has to be cre a ted , in cyberspace anonymity is the g iven.

I D E N T I T Y A N D A U T H E N T I C A T I O N :

R E G U L A B I L I T Y

This difference between the architectures of identity in real space and in cyberspace
has profound consequences for the regulability of behavior in cyberspace. If regulation hangs upon identity—that is, on knowing at least something about the person
being regulated—then in cyberspace, under TCP/IP's design, there is very little that
the regulator would necessarily know. Unlike real space, cyberspace reveals no self authenticating facts about identity. In real space you reveal your sex, your age, how
you look, what language you speak, whether you can see, whether you can hear, how
i n tell i gent you are . In cybers p ace you reveal on ly an ad d re s s , and one that has no
necessary relationship to anything else about you.

The absence of self-authenticating facts in cyberspace reduces its regulability. If
a state, for example, wants to regulate obscenity or control children's access to "indecent" speech, the Internet architecture provides no help. Both data and people are
unidentified in this world, and while it is often possible to make good guesses, it is
also easy to make good guesses impossible. With the Internet architecture of Net95,
it is easy to hide who you are. Perhaps more important, it is difficult to assert facts
about your identity in a credible way. On the Internet it is both easy to hide that you
are a dog and hard to prove that you are not.

All this is true under one architecture of the Internet. Claims about the difference between real space and cyberspace depend on this difference in design. The les-

3 4

son of the last chapter, however, was that architectures could be different. We could
i m a gine different arch i tectu res that would bet ter help us iden tify who indivi du a l s
are and authenticate other facts about them.

In the balance of this chapter, I want to introduce one such architecture. I will
consider questions—about its use or justification, its possible threats to privacy or
a n onym i ty, or the likel i h ood of its becoming a dominant arch i tectu re—in later
ch a pters . My aim here is to convi n ce you that there are su ch arch i tectu res and to
sketch the regulability that such an architecture would permit.

A R C H I T E C T U R E S O F I D E N T I F I C A T I O N

How then could we layer arch i tectu res of i den ti ty on to the ex i s ting iden ti ty -
ignorant architectures of TCP/IP?5

Consider three common techniques used today to id identify someone on the Internet. There are others,and the description of these three will not be complete. But
a sketch of these three reveals two features of a "pass-technology"that will be central
to the architectures of identification that the Net is now building.

The first technique is a password. You have an account on a system; the account
has your account name and password; when you access the system, you must provide both bits of information. The combination is what verifies that you are authorized to use the system.

There are any number of examples of identification of this sort. America Online
(AOL) is a well-known one. You must type in a password associated with a particular "screen name" before you can enter AOL. Lexis—a provider of online legal resources—is a second, though Lexis requires only a single password (not an account
name as well) to enter. Uses of the database are then charged to that password.

A password sys tem has well - k n own adva n t a ges and disadva n t a ge s . The main adva n t a ge is its sec u ri ty—at least as long as the user keeps his or her password sec ret . Th e
d i s adva n t a ge is cost and the inconvenience i en ce of con ti nu a lly using passwords to move
f rom one space to another.6 If every site on the Net requ i red some sort of p a s s word ,
t h en su rfing would be as tedious as crossing Manhattan du ring Fri d ay rush hour.

A second, and much cruder system avoids this inconvenience. This system uses
verification through a "cookie"—a small entry made by your browser to a "cookie
file" on your hard disk that allows a site to know who you are.7 When you first purchase a book from Am a zon . com and establish an acco u n t ,
for ex a m p l e ,
Amazon.com's server places an entry in your cookie file. When you return to that
site, your browser sends the cookie along with the request for the site; the server can
then set your preferences according to your account. Amazon.com can recommend
books for you to buy, given the pattern of purchases you have made before.

The main advantage in this system is its seamless verification. Unless you have
your browser set to notify you of cookie exchanges, you can surf through sites that
deposit and consume cookies with little interruption.

3 5

The disadva n t a ge is the danger that your cookie file could be manipulated or
even copied to other systems.8 It could also provide a key with which providers can
l e a rn abo ut yo u . If a com m on cookie iden ti fies you ac ross a nu m ber of s i tes (because these sites have subscribed, for example, to a common tracking system), then,
in principle,if you have revealed information about yourself in one of those places,
the other places could know it as well.

Cookies are less secure than passwords, though of course they are doing something very different. This difference does not mean they are useless. The security we
need is a function of the risk we are protecting against. Certainly, the NSA should
not use cookies as the system for granting access to databanks of national secrets.
But there is no reason why a portal site like Yahoo should not use cookies to figure
o ut who you are and to give you the news that you have previ o u s ly sel ected . Yo u
have little incentive to lie about this; Yahoo! has little reason to care if you do. With
so little at stake, an unobtrusive if insecure system is perfectly adequate.

A third technology would marry the benefits of the first two. This is the technology of digital signatures, which enables digital certificates, a kind of passport on the
Internet. They would authenticate any t ype of information about a ma chine and, if
u n l ocked by a pass-ph phrase or bi om etric devi ce , a bo ut yo u — your name, your citizenship, your age, whether you are a lawyer. While the details of the architecture are
many, suffice it for now to define them as encr ypted digital objects that can be used
to authenticate facts about someone.

Digital certificates would reside on your computer (under at least some designs);
a server would automatically (and invisibly) check the certificate as you entered the
site. If you held the right certificate, you would be let in,and as you were let in, the
server would then "know"the certified facts about you. It would "know," that is,that
you were a man, or that you came from Canada, or that you were over the age of
twenty-five. And it could do or know all this without ever asking you anything at all.
Certificates could become the kind of self-authenticating credential that we know in
real space, but unlike in real space,there would be no limit to the facts the certificate
could certify.

Di gital certi f i c a tes would make po s s i ble a sec u re sys tem of i den ti f i c a ti on that
could operate as seamlessly as cookies but with much more data certified. They rely,
however, on technologies of cryptography. To see how, we must take a detour into
the workings of cryptography, and then consider again how this technology could
be molded to the form of identification.

C R Y P T O G R A P H Y :

C O N F I D E N T I A L I T Y

V E R S U S A U T H E N T I C A T I O N

Here is something that will sound very extreme but is at most,I think, a slight exaggeration ti on : en c rypti on tech n o l ogies are the most important tech n o l ogical bre a kt h ro u gh in the last one thousand ye a rs . No other tech n o l ogical discovery — f rom

3 6

nuclear weapons (I hope) to the Internet—will have a more significant impact on
social and political life. Cryptography will change everything.

I say this not because I have the space in this book, or ability in any case, to prove
this claim to you.I say this to emphasize. It's not important that you understand the
underlying technologies, though it would be great if more people did. What is important is that you get a hint of the purposes to wh i ch these tech n o l ogies can be
turned,and the consequences of their power.

Cryptography is Janus-faced: it has an ambiguous relationship to freedom on the
Internet. As Stewart Baker and Paul Hurst put it, cryptography "surely is the best of
technologies and the worst of technologies. It will stop crimes and it will create new
crimes. It will undermine dictatorships,and it will drive them to new excesses. It will
make us all anonymous, and it will track our every transaction."9

Cryptogra phy can be all these things , both good and bad , because en c rypti on
can serve two fundamentally different ends. In its "confidentiality"function it can be
"used to keep communications secret." In its "identification" function it can be "used
to provide forgery-proof digital identities."10 It thus enables freedom from regulation (as it enhances confidentiality), but it can also enable regulation (as it enhances
identification).11

Its traditional use is secrets. Encrypt a message, and only those with the proper
key can open and read it. This type of encryption has been around as long as lang u a ge itsel f . But until the mid-1970s it su f fered from an important we a k n e s s : t h e
same key that was used to encrypt a message was also used to decrypt it. So if you
lost that key, all the messages hidden with that key were also rendered vulnerable. If
a large number of messages were encrypted with the same key, losing the key compromised the whole archive of secrets protected by the key. This risk was significant.
You always had to "transport" the key needed to unlock the message,and inherent in
that transport was the risk that the key would be lost.

In the mid-1970s, h owever, a bre a k t h ro u gh in en c rypti on tech n i que was announced by two computer scientists, Whitfield Diffie and Martin Hellman.12 Rather
than relying on a single key, the Diffie-Hellman system used two keys—one public,
the other private. What is encrypted with one can be decrypted only with the other.
Even with one key there is no way to infer the other.

This discovery was the clue to an architecture that could build an extraordinary
range of confidence into any network, whether or not the physical network itself was
secure. Even if the wires are tapped, this type of encryption still achieves its magic.
We can get a hint o f how in a series of cases whose accumulating impact makes the
potential clear.

A. If I want to send a message to you that I know only you will be able to read, I
can take your public key and use it to encrypt that message. Then I can send
that message to you knowing that on ly the holder of the priva te key (presumably you) will be able to read it. But you cannot be sure it is I who sent you
the message. Because anyone can encrypt a message using your public key and

3 7

then send it to you, you have no way to be certain that I was the one who sent
it. Therefore, consider the next example.

B. Before I send the message I have en c rypted with your public key, I can en c rypt
it with my priva te key. Th en wh en you receive the message from me, you can
first dec rypt it with my public key, and then dec rypt it again with your priva te
key. Af ter the first dec rypti on , you can be su re that I (or the holder of my priva te key) was the one who sent you the message ; a f ter the second dec rypti on ,
you can be su re that on ly you (or other holders of your priva te key) actu a lly
re ad the con tent of the message . But how do you know that what I say is the
p u blic key of L a rry Lessig is actu a lly the public key of L a rry Lessig? How can
you be su re , that is, that the public key you are using is actu a lly the public key
it purports to be? Here is wh ere the next example comes in.

C . If t h ere is a tru s t wort hy third party (say, my bank, or the Federal Re s erve
Boa rd , or the AC LU) with a public key (a fact I am able to verify because of
the prom i n en ce of the insti tuti on ) , and that third party verifies that the
p u blic key of L a rry Lessig is actu a lly the public key of L a rry Le s s i g, t h en
a l ong with my message sent to yo u , en c rypted first in your public key and
s second in my priva te key, would be a certi f i c a te , i s su ed by that insti tuti on ,
i t s el f en c rypted with the insti tuti on's priva te key. Wh en you receive the
m e s s a ge , you can use the insti tuti on's public key to dec rypt the certi f i c a te ;
t a ke from the certi f i c a te my public key (wh i ch you now are fairly con f i den t
is my public key ) ; dec rypt the message I sent you with the key held in the
certi f i c a te (after wh i ch you are fairly con f i dent comes from me); and then
dec rypt the message en c rypted with your public key (wh i ch you can be
f a i rly con f i dent no one else has re ad ) . If we did all that, you would know
that I am who I say I am and that the message was sent by me; I would know
that on ly you re ad the message ; and you would know that no one else re ad
the message along the way.

I could add any number of complications (for example,how can I be certain that
you are who you say you are? Clue: the same way you can be certain that I am who
I say I am), and I have hidden a number of important simplifications. For example,
it turns out that it is simpler not to encrypt the whole message with a dual key system but rather to encrypt only a symmetric key13 using a dual key system.14 My aim,
however, is simply to outline the basic elements of this architecture: a system of dual
or asymmetric encryption,and a system of trusted third parties that can certify facts
about you. The world I am describing would have both of these elements automatically and seamlessly executed.

The en c rypti on I've been de s c ri bing is call ed "p u blic key " en c rypti on — a ga i n ,
because it has two keys , one publ i c , one priva te , u n l i ke trad i ti onal single key encryption. As the last step of this encryption process makes clear, the system depends
on an infrastructure—not an infrastructure of special wires or protected pathways,
but an infrastructure of trust, which can provide not perfect confidence but enough

3 8

con fiden ce thro u gh the mu l ti p l i c a ti on of a s s assertions ons abo ut aut h en ti c i ty to make it
certain enough that the fact certified by a particular signature is true.

An infrastructure that supports a public key system is called "PKI" (public key
i n f ra s tru ctu re ) .1 5 The first point to see is the po ten tial that a well - e s t a bl i s h ed PKI
creates. With a robust PKI, the possibilities for identification become extraordinary.
In d ivi duals could carry certi f i c a tes that aut h en ti c a te any nu m ber of f acts abo ut
themselves—who they are; personal attributes (age, citizenship, sex, marital status,
sexual orientation, HIV status); professional credentials (college degrees, bar certification, and so on). These certificates could reside on their personal computers, and
when they attempted to enter an Internet site, that site would check the certificate
and let them pass if they held the proper certificate. It would deny access if they did
not.A world with a robust PKI would enable an unlimited range of cheap authentication, and hence an unlimited range of zoning—of conditioning access to Internet
sites based on the credentials held by the user.

But only if. Whether such architectures will come to exist is a different question.
Systems close to these are already being developed,though none operate as generally
as I've just described. The dominant model of certificates today is id identification—
certificates that verify that you are who you say you are. As described by Verisign,the
current leader issuing digital certificates:

Think of Digital IDs as the electronic e quivalent of driver licenses or passports
that reside in your Internet browser and e-mail software. They contain informati on that uniquely ely iden ti fies yo u , and all ow you to : Di gi t a lly sign a message so
your recipient knows that a message really came from you.Encrypt a message so
your intended recipient can decrypt and read its contents and attachments.

By digitally signing and encrypting your e-mail you can ensure that your conf i den tial messages and attach m ents are pro tected from tampering n g, i m pers impersonation and eavesdropping.16

But verifying a user's identity is only the first part of the architecture I am describing; any model limited to identity will have limited appeal. Businesses do not
re a lly care that I am able to certify that I am Larry Le s s i g, and that Larry Le s s i g
works for Harvard. What they want to know is whether I have the authority to purchase fifty thousand computers for Harvard if they receive from me an order for fifty
thousand computers.Or whether a certain loan officer is authorized to commit to a
certain size loan. Or they want to know whether a representative is actually authorized to make a specific commitment.

In short, what is desired is a more flexible system of certification—a system,that
is,that allows people to certify any sort of fact or statement that they would want to
make. So, for example,if I am authorized to purchase computer equipment for Harvard Law School, Harvard Law School would give me a certificate that authenticates
that fact; someone would in turn certify that the certificate I hold from Harvard Law
School is in fact a certificate from Harvard Law School; and when MicroWarehouse

3 9

receives an e-mail with an order for fifty thousand computers, it would automatically work through the system of certifications to confirm the order.

This more flexible system is the kernel of an architecture of identity that would
render cyberspace regulable. The architecture would allow you to certify any fact or
statement about yourself to which you could get a third party to attest.17 In p principle i p l e , you could hold a creden tial for every aspect of your " i den ti ty " — every fact
about yourself that you wanted to authenticate—from your age all the way down to
the grade you got in spelling in the second grade. (As Michael Froomkin suggests,
Lily Tomlin's joke,"It will be a mark on your permanent record that will follow you
for the rest of your life," is no longer a joke.)18 Depending on how much you trust
the third party, that certification would allow you (as the skeptical user) to believe
the person making the assertions.

But again, why would we expect this system to develop? What b benefit would it
produce,and who stands to gain from this benefit? I've laid responsibility at the foot
of In tern et com m erce . What needs of In tern et com m erce would push us to a
certificate-rich architecture?

T H E C O N T R O L S F O R C O M M E R C E

The Internet was built for research,not commerce. (Indeed,until 1991 the National
S c i en ce Fo u n d a ti on forbade ade its use for com m erce .)1 9 Its pro tocols were open and
unsecured;it was not designed to hide.Data transmitted over this net could easily be
intercepted and stolen; confidential data could not easily be protected.

E a rly users did not seem to mind this drawback ack . If s ec recy was import a n t , t h ey
were qu i te capable of en c rypting a message . And for most com mu n i c a ti on , s ec u ri ty
was not import a n t . In this world the ethic was open n e s s , and openness was afford a bl e .
But commerce is not so laid-back. At first, vendors were quite anxious about online transactions;credit card companies initially did not want their numbers used in
c ybers p ace—at least, not until cybers p ace ch a n ged . From the start com m erce has
pushed for changes in the architectures of the Net to enable more secure and safer
commerce.

Of course, there is nothing new about this or about commerce on the wires. As
Jane Winn puts it, electronic commerce is "arguably as old as the telegraph."20 The
1970s saw a vast increase in closed architecture systems that used the wires (either
proprietary or not) to exchange data to facilitate commerce. The significance of the
recent birth of e-commerce is that it takes place on an open, unsecured network.21
The ch a ll en ge for com m erce on the early Net was to devel op arch i tectu res that,
while sharing in the network advantages of the Internet,22 would restore some of the
security that commerce requires.

A kind of "open-system" security was needed, and the most successful early example was Netscape's secure socket layer (SSL) protocol.23 Beginning with Netscape
Enterprise Server 2.0, secure servers could exchange encrypted transactional infor-

4 0

mation with Internet browser clients. For example, you could send your credit card
number across the Net, and neither you nor Visa would have to worry that it would
be intercepted and republished.

The great advantage of SSL was its simplicity and economy, benefits it gained by
mixing the best of two different encr yption key techniques, symmetric and asymmetric etric en c rypti on algorithms t h m s . The adva n t a ge of s ym m etric en c rypti on is ef f ic i ency—it is easier for the com p uter to dec rypt using a sym m etric key. Th e
d i s adva n t a ge is sec u ri ty — you have to pass the sym m etric key aro u n d , and som etimes it gets lost. The a dvantage of asymmetric, or public key, encryption is security—you do not have to pass around a private key and risk the loss of the key. The
disadvantage is efficiency—it takes a lot of computing power to decrypt an asymmetrically encrypted message.

SSL mixes these two tech n i ques by en c rypting the sym m etric key asym m etri c a lly.
O n ce en c rypted , the sym m etric key is safe to use on an insec u re net work . But bec a u s e
a key is rel a tively small , it is not a terri ble com p ut a ti onal bu rden to dec rypt it on the
o t h er side . By using asym m etric en c rypti on to pro tect the key, t h ere is no danger that
the key wi ll be reve a l ed in tra n s m i s s i on , but by using a sym m etric key to en c rypt all
o t h er data exch a n ged , the com p ut a ti onal bu rden on both sides is redu ced .

The trouble with SSL, however, is that it is trustworthy only if you can trust the
merchant on the other side. Your information is not likely to leak in the transmission from client to server. But if the owner of the server is not to be trusted,then the
risk you should worry about is not a leaky pipeline.

Ot h er pro tocols have been propo s ed to deal with the probl em of the untrustworthy s tworthy merchant, the most prominent of which is the secure electronic transaction
(SET) protocol.24 SET is a standard adopted by a consortium of credit card companies for exch a n ging credit card data to fac i l i t a te gre a ter sec u ri ty, using a pro toco l
that sti ll simply sits on top of the basic In tern et pro toco l .2 5 With SET, you can be
confident that your credit card number will not be overheard and that the merchant
cannot misuse your number.

These two protocols are just the first steps in constructing an architecture of security for e-commerce. (Though SET may be a misstep: developed by committee,it
is a standard that has proven too complicated to implement effectively.)26 They are
significant improvements, but they do not represent the real change to come. For ecom m erce to devel op fully, the Net wi ll need a far more gen eral arch i tectu re of
trust—an architecture that makes possible secure and private transactions.

The elements of any such architecture are summarized well by Gail L. Grant.27
This architecture would have to provide (1) authentication, to ensure the identity of
the person you are dealing with;(2) authorization, to ensure that the person is sanctioned for a particular function; (3) privacy, to ensure that others cannot see what
exchanges there are; (4) integrity, to ensure that the transmission is not altered en
route; and (5) nonrepudiation, to ensure that the sender of a message cannot deny
that he sent it.

4 1

In real space we achieve each of these elements through familiar real-space architectures of trust. So familiar have these become that we are likely not only to forget the efforts originally made to erect some of them, but also to ignore the features
of real space that make these architectures possible. It is usually obvious if an envelope has been opened. If a signature has been changed, we can usually tell. People we
know self-authenticate,since we recognize them when they come into a store. If we
do not know them, we can check a driver's license or the validity of their credit card.
(Possessing a valid credit card is another kind of self-authentication, though obviously an imperfect one.) We check authorization with structures such as purchase
orders or letters of introduction. We protect privacy by using secure envelopes, and
we protect integrity by checking for evidence of tampering on a letter that has been
received. We use systems of certified exchange (certified mail, guaranteed delivery)
to avoid the problem of repudiation of receipt or sending.

These architectures in real space become invisible to us, but they are obviously
constructs, and just as obviously they are expensive to construct. (This is the difficulty Russia faces now.) If e-commerce is to develop, we must erect equivalent architectures in cyberspace. Commerce will have to develop ways to provide vendors
with sufficient security in online transactions while minimizing the burden of that
security.

Aga i n , the core of a ny su ch arch i tectu re wi ll be tools of en c rypti on and PKI. Th e
core would permit the aut h en ti c a ti on of a digital certi fic a te that veri fies facts abo ut
yo u — your iden ti ty, c i ti zen s h i p, s ex , a ge , or the aut h ori ty you hold. And while we
could erect an arch i tectu re of certi fic a ti on tod ay — t h ere are priva te certi fic a te servers
that we could use to issue certi f i c a tes covering any con conceivable ble fact—the sys tem
would not su pport e-com m erce until these certi fic a tes were part of a gen eral publ i c
key infra s tru ctu re that perm i t ted sec u re and tru s t wort hy com mu n i c a ti on with anyone on the Net . An arch i tectu re that con t a i n ed all these el em ents would provi de ecom m erce with a sec u ri ty gre a ter than the best sec u ri ty in real space . My vi ew is that
online com m erce wi ll not fully devel op until su ch an arch i tectu re is establ i s h ed .

There are many plans for deploying this architecture.28 Some imagine the government as the certifying authority; others imagine trusted third parties (like banks)
in that role. Any number of paths are possible. 29 The key to all of these, however, is
not that a government requires people to hold such IDs.30 The key instead is incen -
tives: systems that build the incentives for individuals voluntarily to hold IDs. When
architectures accommodate users who come with an ID installed and make life difficult for users who refuse to bear an ID, certification will spread quickly.

Cookies have spread in just this way. Because many people are concerned with
the privacy implications of cookies, browsers have enabled users to choose whether
to accept them. With one click, you can disable the deposit of cookies and so prevent
the owner of a web site from selling information about you.

But this privacy comes at a cost. Users who choose this option are either unable
to use areas of the Net wh ere cookies are requ i red or forced con s t a n t ly to ch oo s e

4 2

whether a cookie will be deposited. Most find the hassle too great and simply accept
cookies on their machine.

We will see a similar development with digital IDs. Life will be easier for those
who car ry ID than for those who do not. Servers will make exchanges cheaper, or
simpler, if data can be authenticated. Just as it is easier to accept cookies automatically, so too will it be easier to authenticate facts about yourself. Life in an authenticating world will be simpler for those who authenticate.

If the system spreads with incentives, then we can see why commerce is so good
at spreading the system. Commerce has an incentive itself to increase the authentication and certification of transactions in cyberspace. And it is in a good position to
give incentives to consumers. Incentives are commerce's best tool of regulation, and
commerce is fairly good at deploying them.

Non et h el e s s , t h ere is room for skepti c i s m . No do u bt there wi ll be sign i f i c a n t
hurdles for the community to overcome as competitors fix on standards that provide a sufficiently robust yet flexible exchange. No doubt there are lots of reasons to
wonder whether this infrastructure of security can develop on its own. In my view,
we can see en o u gh to be con fident that it is alre ady devel op i n g : tech n o l ogies that
build en c rypti on into the back ground of an app l i c a ti on are becoming com m on ;
networks are rapidly integrating digital signatures; and a host of companies (called
"certificate authorities") now provide digital certificates.31

You do not have to believe in the invisible hand to be convinced that this infrastructure tru ctu re of trust is com i n g. Even if you do u bt that priva te interests alone co u l d
ach i eve this coord i n a ti on , a n o t h er factor su ggests that the ch a racter of the Net is
about to flip. If commerce alone cannot succeed in establishing these architectures,
government is in a strong position to bring about just the changes that commerce
needs.

The government can help commerce. How it does so is the subject of the chapter that follows.

F I V E

r e g u l a t i n g c o d e

I've ar gued t h at as t h e Net ch anges t o enabl e commer ce, one by-pr oduct of
this change will be to enable regulation. But let's say you don't buy it. Let's say that
you don't believe that the invisible hand acting alone will erect the infrastructure of
trust (and in turn regulation) that I said commerce needed. Let's say you think the
coordination needed is too great and that market incentives will create more confusion than guidance. If you are right, if commerce on its own does not flip the Net,
will the Net remain unregulable?

The answer is no. Commerce does not act alone, and it is not morally opposed to
partnerships with government. If commerce needs help constructing this architecture of trust, or (more likely) if the government begins to understand the value of an
a rch i tectu re of trust for its own reg u l a tory obj ective , t h en govern m ent wi ll hel p
push the code along.

But how? So far I have left standing the assumption that it is impossible for the
government to regulate the Net,that there is something in the nature of the Net that
makes such regulation unworkable. So how is it possible for government to help? If
the Net is unregulable,how could government regulate it to make the Net more regulable?

R E G U L A T I N G A R C H I T E C T U R E

To see how, we must distinguish bet ween two cl a i m s . One is that, given the arch i -
te ctu re of the Net as it is, it is difficult for govern m ent to reg u l a te beh avi or on the
Net . The other is that, given the arch i tectu re of the Net , it is difficult for the govern m ent to reg u l a te the arch i te ctu re of the Net . The first cl a i m , I bel i eve , is tru e .
The second is not. Even if it is hard to reg u l a te beh avi or given the Net as it is, it is
not hard for the govern m ent to take steps to alter, or su pp l em en t , the arch i tectu re

4 4

of the Net . And it is those steps in tu rn that could make beh avi or on the Net more
reg u l a bl e .

This is a regulatory two-step: the Net cannot be regulated now, but if the govern m ent reg u l a tes the arch i tectu re of the Net , it could be reg u l a ted in the futu re .
And wh en govern m ent reg u l a ti on of the arch i tectu re of the Net is ti ed to the
changes that commerce is already introducing, I argue, the government will need to
do very little to make behavior on the Net highly regulable.

This strategy of regulation is nothing new. From the beginning of the modern
state, government has been regulating to make its regulations work better. My point
is on ly to app ly this com m on p l ace to cybers p ace . I want you to see how this old
strategy works here.

I begin the chapter with some examples of regulation working, or not working,
in spaces close to cyberspace. Once you see the pattern, you will see how the pattern
might be applied elsewhere.

T e l e p h o n e s

The architecture of the telephone network1 has undergone a radical shift as it has
m oved from a circ u i t - s wi tch ed to a packet - s wi tch ed net work . Th ere is a cert a i n
irony in this change: digital networks were the original design of the Internet. When
the first arch i tects of what would become the In tern et went to AT&T in the early
1960s for help in building this digital net work , AT&T told them that a packet -
switched network could not work.2 Indeed, AT&T at first refused to give the designers any help at all, so convinced were they that the design was a waste of time. But
however convinced they were, eventually they changed their minds. Now we have a
telephone system that is increasingly like the Internet.

Digital telephone networks work in the same way as the Net. Packets of information are spewed across the system. As with the Internet,nothing ensures that they
will travel in the same way, or along the same path.They take the most efficient path,
which depends on the demand at any one time.

But this cre a tes the probl em that the Com mu n i c a ti ons As s i s t a n ce for Law Enforcement Act of 1994 (CALEA) was designed to solve.3 As telephone networks have
moved from analog to digital, and as switching technologies have moved from central switching to distributed, this change (in the code regulating networks) has had
an important con s equ en ce for law en forcem en t . Because there is no lon ger a predictable path through which a telephone call will pass, it is no longer an easy matter
to tap a ph on e . Wh ereas tapping tel eph ones was on ce rel a tively simple, it is now
quite difficult.

This is the case at least with one version of the architecture of a digitally switched
telephone network. Other versions would be less difficult to tap. The question that
reg u l a tors faced was wh i ch vers i on the tel eph one net work should adopt . And the
difference between versions is just a choice of code. Some codes cost more than others, and some codes protect privacy better than others. So the choice among codes

4 5

becomes a ch oi ce among va lu e s . Con gress asked wh et h er this ch oi ce should be
solely private (made by telephone engineers) or partially public (influenced by Congress). It chose the latter.

Of course, regulating the network code is not the only means of regulation that
Congress had. Congress could have compensated for any loss in crime prevention
re su l ting from the ch a n ge in the net work code by ch a n ging the punishmen t s . If a
change in network architecture made it more difficult to catch criminals, Congress
could simply increase the thre a ten ed punishment or devo te more re s o u rces to investigation.

This is just what happen ed , Seventh Ci rcuit Co u rt of Appeals Ch i ef Ju d ge
Richard Posner argues, when the Warren Court constitutionalized criminal procedure. To compensate for the increased difficulty in convicting a criminal, Congress
rad i c a lly incre a s ed criminal punishmen t s .4 Profe s s or Wi lliam Stuntz has made a
similar point.5 The Constitution, in this story, acted as an exogenous constraint to
which Congress could adjust. If the protections of the Constitution increased, then
Congress could compensate by increasing punishments.

When the constraint is imposed by code, however, Congress has a more direct
way to respond: it can legislate to change the code. Congress can require that telephone one companies adopt a code arch i tectu re that makes the net work wi ret a p -
accessible.

This is just what CALEA did. No doubt CALEA's ultimate aim in requiring this
architecture is to reduce crime, but it pursues this aim indirectly, by modifying the
code to constrain individuals who might want to engage in crime. Because the govern m ent can on ce again tap wh en it has aut h ori ty to tap, d i gital net works are no
longer as helpful for criminals. Hence, the payoff from crime is reduced.

This is law regulating code. Its indirect effect is to improve law enforcement, but
it does so by modifying code-based constraints on law enforcement. It selects an architecture that distributes the burdens of code in a collectively valued way.6

Regulation like this works because telephone companies are few. It is relatively
easy for the government to verify that the telephone company is complying with its
rules; it would be hard to establish a rogue telephone company (outside the context
of Internet telephony at least). Thus, indirect regulation depends on there b eing a
useful target for regulation. But if there is such a target, and that target can control
the code of the network, then the government can regulate the code.

T e l e p h o n e s : P a r t 2

Four years after Congress enacted CALEA, the FBI petitioned the Federal Communications Commission (FCC) to enhance even further government's power to regulate. Among the amendments the FBI proposed was a regulation designed to require
disclosure of the locations of individuals using cellular phones.7

The idea was this. Cellular phone systems, to ensure seamless switching between
transmitters, collect information about the location of a user when she is using a cel-

4 6

lular phone. Beyond billing, the phone companies do not need this information for
any other purpose. But the FBI has interests beyond those of the phone service. The
FBI would like that data made available to it whenever it has a "legitimate law enforcement reason" for requesting it. The amendment to CALEA would require the
cellular company to provide this information, which is a way of indirectly requiring
that it write its code to make the information retrievable.8

The ori ginal motiva ti on for this requ i rem ent was simple en o u gh . E m er gen c y
s ervi ce provi ders needed a simple way to determine wh ere an em er gency cellular l a r
ph one call was coming from . But of co u rs e , i f that were the on ly purpose of t h e
change, the system could be designed to report location information only when an
emergency call is made. Instead, the push is to require the collection of this information whenever a call is made.

If it succeeds, then the FBI succeeds by getting Congress to legislate a different
code for cellular ph on e s . If Con gress reg u l a tes the code , tracking indivi duals becomes easier, and thus the regulability of those tracked increases.

T a p e s

A compact disc (CD) recording is a digital recording. Like any digital recording, it
can,in principle, be copied perfectly. But before the advent of digital tapes, and then
computers,there was no medium onto which a digital CD could be perfectly copied.
To copy it on to an audiotape was to make an analog recording of the digital fil e .
Quality would be lost in the copy.

This imperfection in copying ability was a type of protection for CD producers.
Real-space code, as it were, constrained the ability of copyright thieves to copy CDs
onto tape and sell them as pirated editions. The inferiority of such tapes kept most
of the public in the legitimate CD market.

Digital audio technology (DAT) threatened to change this balance. DAT was the
application of digital technology to tape: a digital recording on a CD could be digitally, and hence perfectly, copied onto a tape. You could buy one CD and make many
copies of it onto DAT tape,each copy having the same fidelity as the first. The code
governing the copying of audio recordings thus changed, eliminating the old code's
implicit protections.

Congress could have responded to this change in any number of ways. It could
have used law to regulate behavior directly, by increasing the penalty for illegal copyi n g. It could have funded a public ad campaign against ill egal copying or funded
programs in schools to discourage students from buying pirated editions of popular
recordings. Or Congress could have taxed blank tapes and then transferred the revenue to owners of copyrighted material.

Instead, Congress chose to regulate the code of digital reproduction.9 It required
producers of digital recording devices to install in their systems a chip that implem ents a code - b a s ed sys tem to mon i tor the copies of a ny copy made on that mach i n e .1 0 The chip would all ow a limited nu m ber of pers onal cop i e s . On copies of

4 7

copies,the quality of the recording would be degraded. Congress in essence required
that the code of digital copying be modified to restore the imperfections that were
"natural"in the earlier code.

This again is Congress regulating code as a means of regulating behavior—mandating that multiple copies be imperfect as a way to minimize illegal copying. Like
the tel eph one reg u l a ti on , this reg u l a ti on su cceeds because there are rel a tively few
m a nu f actu rers of DAT tech n o l ogy. Aga i n , given a limited target , the govern m en t's
regulation can be effective.

T e l e v i s i o n s

A fo u rth example is mu ch cl o s er to cybers p ace . The Tel ecom mu n i c a ti ons Act of
1996 required the television industry to develop and implement the "V-chip."11 The
V- chip would fac i l i t a te the autom a tic bl ocking of tel evi s i on broadc a s t s , b a s ed on
criteria of content that have not yet been completely determined. The crudest proposals involve something like the Motion Picture Association's movie rating system;
the more sophisticated envision selections based on a much richer set of factors.

The legislation was passed in response to the perception that violence on television had increased dramatically, and that this increase was harmful to kids. People
were con cern ed that TV vi o l en ce would affect beh avi or. S tudies had su gge s ted as
much; less reflective evidence had confirmed it. Congress sought to discourage the
violence by providing a way to filter it out.12

Given the state of First Amendment law, it would have been difficult for Congress to restrict violence on TV directly. (Though the regulation of broadcasting has
been subject to special First Amendment rules,13 and the life of these doctrines now
seems limited.)14 Even if applied only to children's television, such regulation would
raise difficult constitutional questions—difficult enough, that is, to motivate Congress to seek a different way.

Thus Con gress chose code . It requ i red tel evi s i on manu f actu rers and med i a
produ cers to devel op a tech n o l ogy to ra te what is broadcast on tel evi s i on so that
p a rents could bl ock what they do not want their ch i l d ren to see . It requ i res that
tel evi s i ons be built with a code that fac i l i t a tes discri m i n a ti on by con su m ers of
tel evi s i on broadc a s ti n g. And it does this to adva n ce a social aim of the governm en t : to em power paren t s . By giving parents more power to discri m i n a te , Congress indirect ly disco u ra ges an ill (ex po su re to vi o l en ce) that it is con s ti tuti on a lly
u n a ble to reg u l a te direct ly.1 5

E n c r y p t i o n

The examples so far have invo lved reg u l a ti ons directed against code wri ters . But
sometimes the government tries to act indirectly by using the market to regulate the
code. An example is the government's failed attempt to secure Clipper as the standard for encryption technology.16

4 8

I have already sketched the Janus-faced nature of encryption: the same technology en a bles both con fiden ti a l i ty and iden ti fic a ti on . The govern m ent is con cern ed
with the confidentiality part. Encryption allows individuals to make their conversations or data exchanges untranslatable except by someone with a key. How untranslatable is a matter of debate,17 but we can put that debate aside for the moment: it is
too untranslatable for the government's liking. So the government sought to control
the use of encryption technology by getting the Clipper chip accepted as a standard
for encryption.

The mechanics of the Clipper chip are not easily summarized, but its aim is to
permit encryption that keeps open a back door for the government.18 A conversation could be encr ypted so that others could not understand it but the government
would have the ability (in most cases with a court order) to decrypt the conversation
using a special key.

The Clinton administration first thought that the best way to ensure the creation
of this technology was through direct regulation—by banning all other encryption
tech n o l ogy. This stra tegy proved con trovers i a l , so the govern m ent then fixed on a
different technique.19 It subsidized the development and deployment of the Clipper
chip.

The thinking was obvious: if the government could get industry to use Clipper
by making Clipper the cheapest technology, then it could indirectly regulate the use
of encryption. The market would do the regulation for the government.20

The su b s i dy plan failed . Skepticism abo ut the qu a l i ty of the code itsel f , a n d
about the secrecy with which it had been developed, as well as strong opposition to
a ny govern m en t a lly directed en c rypti on regime (espec i a lly a U. S . - s pon s ored
regime), led most to reject the technology. This forced the government to take another path.

That altern a tive is for our purposes the more intere s ti n g. In the govern m en t's
most recent proposals,the authors of encryption code would be regulated directly—
with a requirement that they build into their code a back door through which the
government could gain access.21 While the proposals have been various, they all aim
at ensuring that the government has a way to crack whatever encryption code a user
selects.

Compared with other strategies—banning the use of encryption or flooding the
market with an alternative encr yption standard—this mode presents a number of
advantages.

First,unlike banning the use of encryption, this mode of regulation does not directly interfere with the rights of use by individuals. It therefore is not vulnerable to
a strong, if yet unproven constitutional claim that an individual has a right "to speak
t h ro u gh en c rypti on ."2 2 It aims on ly to ch a n ge the mix of en c rypti on tech n o l ogi e s
available,not to control directly any particular use by an individual.State regulation
of the writing of encryption code is just like state regulation of the design of automobiles: individual use is not regulated. Second, unlike the technique of subsidizing
one market solution,this solution allows the market to compete to provide the best

4 9

encryption system, given this regulatory constraint. Finally, unlike both other solutions, this solution involves the regulation of only a relatively small number of actors , s i n ce manu f actu rers of en c rypti on tech n o l ogy are far fewer in nu m ber than
users or buyers of encryption systems.

Like the other examples in this section, then, this solution is an example of the
government regulating code directly so as to better regulate behavior indirectly. As
in other examples, the government uses the architecture of the code to reach a particular substantive end. Here the end, as with digital telephony, is to ensure that the
govern m en t's abi l i ty to search certain convers a ti ons is not bl ocked by em er gi n g
technology.

C i r c u m v e n t i o n

My final example is the most recent. As I discuss in some d detail in chapter 10, many
businesses are developing systems for protecting intellectual property in cyberspace.
The problem is the same as with digital audio technology. Copies in cyberspace are
digital and free; digital copies are perfect; free copies are cheap. The fear is that cyberspace will become the place where copyright can be defeated. Using MP3 techn o l ogi e s , for ex a m p l e , a CD recording can be com pre s s ed to a file the size of t h e
Word file containing this book and in seconds e-mailed to one hu n d red fri en d s
around the world.

The systems being developed in response will make it hard to copy without permission. How hard,and how they will work,are questions we can postpone for now.
Suffice it to say that the systems are designed to give holders of intellectual property
more power over the distribution of that property.

These protections are built into the systems through code. But code can also be
u s ed to circ u circumvent su ch pro tecti on s . ( Rem em ber the copy pro tecti on sys tems for
s of t w a re com m on in the early 1980s, and the cracking sof t w a re used to defe a t
t h em.) Using circ u mven ti on sof t w a re , t h en , u s ers could defeat the pro tecti on that
code creates.

Congress responded to this threat.23 In the 1998 Digital Millennium Copyright
Act, Congress made it a felony to write and sell software that circumvents copyright
management schemes.24 In the judgment of Congress, regulating users alone would
be difficult but regulating the code that users use would not be as difficult.

C E R T I F I C A T I O N A N D R E G U L A B I L I T Y

All six of these examples describe a behavior that the government wants to regulate,
but which it cannot (easily) regulate directly. So government regulates behavior ind i rect ly by reg u l a ting arch i tectu re s , wh i ch in tu rn influ en ce or con s train beh avi or
differently. This indirect regulation,at times quite effective, suggests a way of thinking about the example that started us down this road—certification.

5 0

At the start of this chapter we asked: What steps could government take, not to
regulate a particular behavior, but to increase the regulability of behavior in cyberspace generally? My claim was that this goal could be achieved by increasing the capacity of sites on the Net to identify whom they are dealing with—to know either
who the user is or what credentials, or features, he or she possesses.

Reg u l a bi l i ty then depends in part on iden ti fic a ti on—not perfect iden ti fic a ti on
(the po l i ce do not need to know my name to tell me to slow my car down ) , but
en o u gh for the govern m ent to know what reg u l a ti ons the user is su bj ect to, a n d
when he has violated them.

How can the government facilitate this identification—assuming, of course,that

commerce has not by itself created a sufficient demand for credentials?

It seems clear from the six examples above that the best target of su ch reg u l a ti on
wi ll not be the indivi du a l . If the govern m ent requ i red all indivi duals to carry a digital ID, t h ere would no do u bt be a revo luti on . Am ericans are antsy en o u gh abo ut a nati onal iden ti ty card .2 5 Th ey are not likely to be intere s ted in an In tern et iden ti ty card .
But it does not fo ll ow that govern m ent cannot cre a te incen tives for people to
adopt iden ti fic a ti on tech n o l ogi e s , even wi t h o ut direct ly mandating them . Th ere is
no requ i rem ent that all citi zens have a driver 's licen s e , but you would find it very
hard to get around without one, even if you do not drive. The government does not
require that you keep state-issued identification on your p erson, but if you want to
fly to another city, you must show at least one form of such identification. The lesson is simple: make the incentive to carry ID so strong that no government requirement is necessary.

In the same way, the govern m ent could cre a te incen tives to en a ble digital IDs,
not by regulating individuals directly but by regulating intermediaries. Intermediaries are fewer, their interests are usually commercial, and they are ordinarily pliant
targets of regulation.

Consider some of the means that the government could employ to achieve this

end:

•

Sites on the Net have the ability to condition access based on whether someone car ries the proper credential. The government has the power to require
sites to impose a condition that users carry the proper credentials. For example, the state could require that gambling sites check the age and residency of
anyone trying to use the site. Many sites could be required to check the citizenship of potential users, or any number of other credentials. As more and
more sites complied with this requirement, individuals would have a g reater
and gre a ter incen tive to carry the proper creden ti a l s . The more creden ti a l s
they carried,the easier it would be to impose regulations on them.26

• The government could give a $50 tax break to anyone who filed his or her income tax sign ed by a properly certi fied aut h ori ty; it could certify these authorities based on whether they coded certificates in the way the government

5 1

wanted, and whether they permitted the certificates to be used for purposes
beyond the government's limited use.

• The govern m ent could impose a 10 percent In tern et sales tax and then exempt anyone who purchased goods with a certificate that authenticated their
state of residence; the state would then be able to collect whatever local tax
applied when it was informed of the purchase.27

• The government could charge users for government publications unless they

gained access to the site with a properly authenticated certificate.

• As in other Western democracies, the government could mandate voting28—
and then establish In tern et vo ti n g ; vo ters would come to the vi rtual po ll s
with a digital identity that certified them as registered.

All these altern a tives would use the same stra tegy of i n d i rect reg u l a ti on that
marked the original six examples. The state would regulate intermediate providers,
enabling those providers to regulate users, who would find their access conditioned
on providing creden ti a l s , wh i ch make it easier for the state to reg u l a te . The state
would be using the market to regulate individuals, and to make the Net itself more
regulable.

We can extend this model of regulation to the regulation of code itself. The govern m ent could requ i re In tern et servi ce provi ders (ISPs ) , for ex a m p l e , to em p l oy
s of t w a re that fac i l i t a tes trace a bi l i ty by con d i ti oning access on the user 's provi d i n g
some minimal level of identification. Call this a "traceability regulation." Many ISPs
would resist it, but the government could then require that major commercial institutions (including credit institutions) be prohibited from dealing with any ISP not
certi fied to be in com p l i a n ce with the trace a bi l i ty reg u l a ti on . Some major insti tutions,in turn, might resist this requirement, but not many. For major institutions in
a competitive market, the threat of governmental prosecution far outweighs any incen tive to vi o l a te the law. These two steps would cre a te a great incen tive for loc a l
ISPs to facilitate traceability.

Such a rule, of course, raises serious constitutional questions.I consider some of
them in the chapters that follow. My aim here is simply to sketch the techniques that
could enable an effective ID requirement in cyberspace. The point is that within an
i n tegra ted com m ercial and non com m ercial net work the govern m en t's power over
com m ercial en ti ties leverages ges into a power over non com m ercial en ti ti e s . Bri n gi n g
commerce to the Net was the first, essential, and perhaps sufficient step in making
the Net reg u l a bl e . More active interven ti on by the govern m ent wi ll make it even
more so.

So far, however, governments have not been good at encouraging an architecture
of identification. Not only have they been slow, but through clumsy legislation they
h ave inhibited ted its growt h .2 9 In my vi ew, h owever, these errors are short - term . We
cannot count on the govern m ent making errors forever, e s pec i a lly wh en so mu ch
hangs on the construction of an effective PKI architecture.

5 2

A crucial assumption is built into all these examples. I've assumed that there are entities responsible for the code that individuals use, and that these entities can be effectively regulated. And as the open code software movement grows, it is important
to ask whether this assumption is really true. The government can regulate the telephone companies (they are few in number, well known,and loaded with tangible assets), but how can it regulate code w riters? In particular, how can the government
regulate code writers who are committed to resisting precisely such regulation?

This is the topic of the last chapter in part 2—the effect of the open code movement on government's power to regulate. But we can make a few points here.

In a world where the code writers were the sort of people who governed the Internet Engineering Task Force30 of a few years ago, government's power to regulate
code would be slight. The underpaid heroes who built the Net have ideological reasons to resist government's mandate. They are not likely to yield to its threats. And
unlike some commercial interests, they do not have millions riding on a single architecture winning out in the end. Thus, they would provide an important check on
the government's power over the architectures of cyberspace.

But as code wri ting becomes com m ercial—as it becomes the produ ct of a
s m a ll er nu m ber of l a r ge companies—the govern m en t's abi l i ty to reg u l a te it inc re a s e s . The more mon ey there is at stake , the less incl i n ed businesses (and thei r
backers) are to bear the costs of promoting an ideology.

The best example is the history of encryption. From the very start of the debate
over the government's control of encryption, techies have argued that such regulations are silly. Code can always be exported; bits know no borders. So the idea that a
law of Congress would control the flow of code was, these people argued, absurd.

The fact is, h owever, that the reg u l a ti ons had a su b s t a n tial ef fect . Not on the
tech i e s — who could easily get en c rypti on tech n o l ogies from any nu m ber of p l ace s
on the Net — but on the businesses wri ting sof t w a re that would incorpora te su ch
tech n o l ogy. Net s c a pe or IBM was not abo ut to build and sell sof t w a re in vi o l a ti on
of U. S . reg u l a ti on s . The Un i ted States has a fairly powerful threat against these two
com p a n i e s . As the techies pred i cted , reg u l a ti on did not con trol the flow of bi t s . But
it did qu i te su b s t a n ti a lly inhibit the devel opm ent of s of t w a re that would use these
bi t s .3 1

The effect has been profound. Companies that were once bastions of unregulability are now becoming producers of technologies that facilitate regulation. For example, Network Associates,inheritor of the encryption program PGP, was originally
a strong opponent of regulation of encryption; now it offers products that facilitate
corpora te con trol of en c rypti on and recovery of keys .3 2 Key recovery fac i l i t a tes a
corpora te back door, wh i ch in many con texts is far less re s tri cted than a governmental back door.

Ci s co is a second ex a m p l e .3 3 In 1998 Ci s co announced a ro uter produ ct that
would enable an ISP to encr ypt Internet traffic at the link le vel—between gateways,
that is.34 But this router would also have a switch that would disable the encr yption
of the router data and facilitate the collection of unencrypted Internet traffic. This

5 3

s wi tch could be flipped at the govern m en t's com m a n d ; in other word s , the data
would be encrypted only so long as the government allowed it to be.

The point in both cases is that the government is a player in the market for software. It affects the market both by creating rules and by purchasing product. Either
way, it influences the supply of commercial software providers who exist to provide
what the market demands.

Veterans of the early days of the Net might ask these suppliers,"How could you?"
"It's just business," is the obvious reply.

E A S T C O A S T A N D W E S T C O A S T C O D E

Throughout this section, I've been speaking of two sorts of code. One is the "code"
that Congress enacts (as in the tax code or "the U.S. Code"). Congress passes an endless array of statutes that say in words how to behave. Some statutes direct people;
o t h ers direct com p a n i e s ; s ome direct bu re a u c ra t s . The tech n i que is as old as govern m ent itsel f : using commands to con tro l . In our co u n try, it is a pri m a ri ly East
Coast (Washington, D.C.) activity. Call it "East Coast Code."

The other is the code that code w riters "enact"—the instructions imbedded in
the sof t w a re and hardw a re that make cybers p ace work . This is code in its modern
sense. It regulates in the ways I've begun to describe. The code of Net95, for example, regulated to disable centralized control; code that encrypts regulates to protect
privacy. In our country (MIT excepted), this kind of code writing is increasingly a
West Coast (Silicon Valley, Redmond) activity. We can call it "West Coast Code."

West Coast and East Coast Code can get along perfectly fine not paying much attention to the other. Each, that is, can regulate within its own domain. But the story
of this chapter is "East meets West": what happens when East Coast Code recognizes
how West Coast Code is regulating, and when East Coast Code sees how it might interact with West Coast Code to induce it to regulate differently.

This interacti on has ch a n ged . The power of East Coast Code over West Coa s t
Code has increased. When software was the product of hackers and individuals located outside of any institution of effective control (for example, the University of
Illinois or MIT), East Coast Code could do little to control West Coast Code.35 But
as code has become the product of companies, the power of East Coast Code has inc re a s ed . Wh en com m erce wri tes code , t h en code can be con tro ll ed , because comm ercial en ti ties can be con tro ll ed . Thu s , the power of East over West increases as
West Coast Code becomes increasingly commercial.

There is a long history of power moving west. It tells of the clash of ways between
the old and the new. The pattern is familiar. The East re aches out to con trol the
West; the West, partially, resists.

We are seeing in cybers p ace a shift that history has seen many times before . But
we are not yet done with the East's con trol of the We s t . Th ere is one final step to
t a ke before the power of the state to make cybers p ace reg u l a ble is com p l etely cl e a r.

5 4

This final step links this ch a pter 's argument with the last ch a pter 's account of
i den ti f i c a ti on .

R E G U L A T I N G T H E I D - E N A B L E D W O R L D

In my story so far, I've described a certain kind of cooperation between East Coast
code and West Coast Code. I've argued that commerce alone has an interest in crea ting an arch i tectu re of i den ti fic a ti on , and I've laid out just how the govern m en t
might influence the architecture of the Net to create the requirement of some sort of
identification, or traceability. The final step in this argument is to make explicit what
has been implicit throughout—that an ID-enabled world facilitates regulation.

How wi ll the internal passports of d i gital ID en a ble reg u l a ti on? The proof
comes in two step s . In the firs t , I lay out how an ID-en a bl ed world would en a bl e
reg u l a ti on for a particular probl em of reg u l a ti on—in this case, ga m bl i n g. In the
s econ d , I show how this tech n i que gen era l i ze s . Al t h o u gh not every govern m en t
m ay want to solve the probl em of ga m bl i n g, every govern m ent does have som e
probl em that it wants to solve . The ID-en a bl ed world can help each govern m en t
s o lve its own reg u l a tory probl em . Thu s , govern m ents share an interest in an IDen a bl ed worl d , even if t h ey do not share an interest in the particular reg u l a ti on s
su ch a world makes po s s i bl e .

Let's return to the problem of Internet gambling and consider it both with and
without digital IDs. My claim is that a certificate-rich Internet solves the problem of
regulability. Once you see this point with respect to this single example, you will see
the point more generally.

Gambling is one of the stock examples given by cyberlibertarians to show why
beh avi or in cybers p ace is unreg u l a bl e . Ta ke the case of Mi n n e s o t a , wh i ch has a
s trong state policy against ga m bl i n g.3 6 Its legi s l a tu re has banned its citi zens from
ga m bl i n g, and its attorn ey gen eral has vi goro u s ly en forced this legi s l a tive ju d judgment—both by shutting down gambling sites in the state and by threatening le gal
action against sites outside of the state if they let citizens from Minnesota gamble.

This threat, cyberlibertarians argue, will have no effect on gambling on the Intern et , n or on the ga m bling beh avi or of Minnesota citi zen s .3 7 The proof is fairly
straightforward. Imagine a gambling server located in Minnesota. When Minnesota
makes gambling illegal,that server can move outside of Minnesota. From the standpoint of citizens in Minnesota, the change has (almost) no effect. It is just as easy to
access a server located in Minneapolis as one located in Chicago. So the gambling
site can easily move yet keep all its Minnesota customers.

Suppose that Minnesota then threatens to prosecute the owner of the Chicago
server. It is relatively easy for the attorney general to persuade the courts of Illinois
to prosecute the illegal server in Chicago (assuming it could be shown that the behavior of the server was in fact illegal). So the server simply moves from Chicago to
Cayman, making it one step more difficult for Minnesota to prosecute but still no

5 5

m ore difficult for citi zens of Minnesota to get acce s s . No matter what Mi n n e s o t a
does, it seems the Net helps its citizens beat the government. The Net, oblivious to
geography, makes it practically impossible for geographically limited governments
to enforce their rules over actors on the Net.

Now, however, imagine a world where everyone holds a digital ID, and not necessarily a governmentally issued ID; any ID will do. As you pass onto a site, the site
checks your ID. If you do not hold the proper ID for that type of site—if you are under eighteen and it is an adult site, or if you are from Minnesota and it is a gambling
site—the site does not let you pass. But if you hold a proper ID, the site does let you
pass. This process occurs invisibly, or machine to machine. All the user knows is that
she has gotten in, or if she has not, then why.38

In this story, then,the interests of Minnesota are respected. Its citizens are not allowed to gamble. But Minnesota's desires do not determine the gambling practices
of people from outside the state.Only citizens of Minnesota are disabled by this regulation; other citizens can gamble.

This is regulation at the level of one state, for one problem. But why would other
states cooperate with Minnesota? Why would any other jurisdiction want to carry
out Minnesota's regulation?

The answer is that they would not if this were the only regulation at stake. Minnesota wants to protect its citizens from gambling, but New York may want to protect its citizens against the misuse of private data. The European Union may share
New York's objective; Utah may share Minnesota's.

Each state has its own stake in controlling certain behaviors, and these behaviors
a re differen t . But the key is this: the same arch i tectu re that en a bles Minnesota to
ach i eve its reg u l a tory end can also help other states ach i eve their reg u l a tory en d s .
And this can initiate a kind of quid pro quo between jurisdictions.

The pact would look like this. E ach state would promise to en force on servers
within its ju ri s d i cti on the reg u l a ti ons of o t h er states for citi zens from those other
s t a te s , in exch a n ge for having its own reg u l a ti ons en forced in other ju ri s d i cti on s .
New York would require that servers within New York keep Minnesotans away from
New York gambling servers, in e xchange for Minnesota keeping New York citizens
aw ay from privac y - ex p l oi ting servers . Utah would keep EU citi zens aw ay from
privacy-exploiting servers, in exchange for Europe keeping Utah citizens away from
European gambling sites.Each state would enforce a set of regulations for the other
states, in exchange for the other states enforcing its own set of regulations.

This structure, in effect, is precisely the structure that is already in place for regulating interstate gambling. According to federal law, interstate Internet gambling is
not permitted unless the user is calling from a gambling-permissive state into another gambling-permissive state.39 If the user calls from a gambling-restrictive state
or into a gambling-restrictive state, he or she has committed a federal offense.

The same structure could be used to sup port local regulation of Internet behavior. With a simple way to verify citizenship, a simple way to verify that servers are
d i s c ri m i n a ting on the basis of c i ti zen s h i p, and a federal com m i tm ent to su pport

5 6

such local discrimination, we could easily imagine an architecture that enables local
regulation of Internet behavior.

And if all this could occur within the United States, it could occur between nations generally. There is the same interest internationally in enforcing local laws as
t h ere is nati on a lly — i n deed , the interest is most likely even high er. An ID, or
certificate-rich, Internet would facilitate international zoning and enable this structure of international control.

S top. Don't tu rn aw ay. I know at least some of the thousands of re a s ons you have
for rej ecting the stru ctu re I've just de s c ri bed . Some of those re a s ons are norm a tive —
you hate the world I am de s c ri bi n g. Or you hate the idea that cybers p ace would become like this worl d . I do too. I am not prom o ting an ide a , I am arguing that this is
the world we are moving to. Those who want to resist this worl d , or at least its wors t
fe a tu re s , h ad bet ter understand the evo luti on . Th ere are cri tical arch i tectu ral dec is i ons that need to be made , and we must begin to make those dec i s i ons now.

Ot h ers might not be so oppo s ed to the em er ging ID-en a bl ed world I am describing but may simply believe that it is unlikely to come about. They believe that
the desire of governments to facilitate such discrimination is not terribly strong, and
in any case, the technology to enable it would be too difficult to erect.

These two points, of course, operate together. Some governments, regardless of
the co s t , a re wi lling to adopt tech n o l ogies to bl ock acce s s . ( China is an ex a m p l e . )
But other countries would not go to such great lengths to control access. If the cost
were too high, they would simply leave the regulation aside and move on to other,
more important activities (Taiwan).

This trade - of f — bet ween cost and the wi ll i n gness to reg u l a te—is one we have
seen before. It is a theme that recurs in many contexts. Cost for the government is
liberty for us. The higher the cost of a regulation, the less likely it will be pursued as
a regulation.Liberty depends on the regulation remaining expensive.

When it becomes easy or cheap to regulate,however, this contingent liberty is at
risk. We can expect more regulation. In these cases,if we want to preserve liberty, we
need to develop affirmative arguments for it. We will need these affirmative arguments to prevent identity-based regulation of the Net. As I explain in the balance of
this book, there is both a surprisingly great desire for nations to embrace regimes
that facilitate jurisdiction-specific regulation and a significant reason why the costs
of regulation are likely to fall. We should expect, then, that there will be more such
regulation. Soon.

The proof that this capacity for regulation will emerge is the subject of the next
ch a pters . To end this ch a pter, we need on ly answer one qu e s ti on . As suming that
these architectures for identification will emerge, what follows about the regulability
of cyberspace?

The answer, I tru s t , is obvi o u s : p ut ting to one side the qu e s ti on of i den ti f yi n g
content (which I consider in detail in chapter 12),an architecture for selective certification would dramatically increase the power of local governments to impose rer e g u l a t i n g c o d e

5 7

requirements on their citizens. Sites would be required to condition admission on the
certificates held by users, and the Internet would shift from being an essentially unregulable space locally to a highly regulable space. Rules imposed by local jurisdictions ons could be made ef fective thro u gh their recogn i ti on by other ju ri s d i cti on s .
Servers , for ex a m p l e , would recogn i ze that access is con d i ti on ed on the rules imposed by jurisdictions.

The effect,in short, would be to zone cyberspace based on the qualifications carried by individual users. It would enable a degree of control of cyberspace that few
have ever imagined. Cyberspace would go from being an unregulable space to, depending on the depth of the certificates in the space,the most regulable space imaginable.

One final line of resistance: even if these architectures emerge, and even if they
become com m on , t h ere is nothing to show that they wi ll become univers a l , a n d
nothing to show that at any one time they could not be evaded. Individuals can always work around these technologies of identity. No control that they could effect
would ever be perfect.

Tru e . The con trol of a certi f i c a te - ri ch In tern et would never be com p l ete . But
there is a fallacy lurking in the argument: just because perfect control is not possible
does not mean that effective control is not possible. Locks can be picked, but that
does not mean locks are useless. And in the context of the Internet, even partial control would have powerful effects.

A fundamental principle of bovinity is operating here, and elsewhere. Tiny controls, consistently enforced, are enough to direct very large animals. The controls of
a certificate-rich Internet are tiny, I agree. But we are large animals. I think it is as
likely that the majo rity of people would resist these small but efficient regulators of
the Net as it is that cows would resist wire fences. This is who we are,and this is why
these regulations work.

One final twist to this bovine account. So far I've been discussing a relatively cumbersome technology for identification—certificates. These are cumbersome because
to tie the certificate to a person (as opposed to a machine), we still need some sort
of link—through, for example, a pass-phrase. These phrases can be a hassle; if they
change, they can be easy to forget.

There is an easier way. Already computer manufacturers are exploring biometric
devi ces that would make it simple to tie a pers on to a mach i n e . Com p a q , for example, is considering a thumbprint reader: when you sit at your keyboard, it would
verify that you are who you say you are . Who needs a password wh en you have a
thumb?40

So what will happen when these technologies become cheap and easy? When you
can choose between remembering a pass-phrase, typing it every time you want access to your computer, and simply using your thumb to authenticate who you are?
Or if not your thu m b, t h en your reti n a , or wh a tever body part tu rns out to be

5 8

cheapest to certify? When it is easiest simply to give identity up, will anyone resist
giving it up?

For if this is selling your soul, then trust that there are truly wonderful benefits
to be had. Imagine a world where all your documents exist on the Internet in a "virtual private network," accessible by you from any machine on the Net and perfectly
secured by a biometric key.41 You could sit at any machine,call up your documents,
do your work, answer your e-mail, and move on—everything perfectly secure and
safe, locked up by a key certified by the markings in your eye.

This is the easiest and most ef f i c i ent arch i tectu re to imagi n e . And it comes at
(what some think) is a very low price—authentication. Just say who you are, plug
into an architecture that certifies facts about you, give your identity away, and all this
could be yours.

Th ere was an awful movie rel e a s ed in 1996 call ed In d Independence d en ce Day. The story is
about an invasion by aliens. When the aliens first appear, many earthlings are eager
to welcome them. For these idealists,there is no reason to assume hostility, and so a
general joy spreads among the hopeful across the globe in reaction to what before
had seemed just a dream: really cool alien life.

Soon after the aliens appe a r, h owever, and well into the cel celebration ti on , the mood
changes. Quite suddenly, Earth leaders realize that the intentions of these aliens are
not friendly. Indeed, their intentions are quite hostile. Within a very short time of
this realization, Earth is captured. (Only Jeff Goldblum realizes what's going on beforehand, but he always gets it first.)

My story here is similar (though I hope not as awful). We have been as welcoming and joyous about the Net as the earthlings were about the aliens in Independence
Day; we have accepted its growth in our lives without questioning its final effect. But
at some point, we too will come to see a potential threat. We will see that cyberspace
does not guarantee its own freedom but instead carries an extraordinary potential
for control. And then we will ask: How should we respond?

I have spent many pages making a point that some may find obvious. But I have
found that, for some reason, the people for whom this point should be most important do not get it. Too many take this freedom as nature. Too many believe liberty
will take care of itself. Too many miss how different architectures embed different
va lu e s , and that on ly by sel ecting these different arch i tectu res—these differen t
codes—can we establish and promote our values.

Now it should be apparent why I began this book with an account of the rediscovery of the role for self-government, or control, that has marked recent history in
post-Communist Europe. Market forces encourage architectures of identity to facili t a te online com m erce . G overn m ent needs to do very little—indeed , nothing at
all—to induce just this sort of development. The market forces are too powerful; the
potential here is too great. If anything is certain, it is that an architecture of identity
will develop on the Net—and thereby fundamentally transform its regulability.

5 9

But isn't it clear that govern m ent should do som ething to make this arch i tectu re con s i s tent with important public va lues? If com m erce is going to define the
em er ging arch i tectu res of c ybers p ace , i s n't the role of govern m ent to en su re that
those public va lues that are not in com m erce's interest are also built into the arch i tectu re ?

Arch i tectu re is a kind of l aw: it determines what people can and cannot do. Wh en
com m ercial interests determine the arch i tectu re ,t h ey cre a te a kind of priva ti zed law. I
am not against priva te en terpri s e ; my strong pre su m pti on in most cases is to let the
m a rket produ ce . But isn't it absolutely clear that there must be limits to this pre su m pti on? That public va lues are not ex h a u s ted by the sum of what IBM might de s i re? Th a t
what is good for Am erica Online is not nece s s a ri ly good for Am eri c a ?

O rd i n a ri ly, wh en we de s c ri be com peting co ll ecti ons of va lu e s , and the ch oi ce s
we make among them, we call these choices "political." They are choices about how
the world will be ordered and about which values will be given precedence.

Ch oi ces among va lu e s , ch oi ces abo ut reg u l a ti on , a bo ut con tro l , ch oi ces abo ut
the definition of spaces of freedom—all this is the stuff of politics. Code codifies values,and yet, oddly, most people speak as if code were just a question of engineering.
Or as if code is best left to the market.Or best left unaddressed by government.

But these attitudes must be mistaken. Politics is that process by which we collectively decide how we should live. That is not to say a space where we collectivize—a
co ll ective can ch oose a libert a rian form of govern m en t . The point is not the su bs t a n ce of the ch oi ce . The point abo ut po l i tics is proce s s . Po l i tics is the process by
which we reason about how things ought to be.

A decade ago, in a powerful trilogy drawing together a movement in legal theory,
Roberto Unger preached that "it's all politics."42 That we should not accept the idea
that any part of what defines the world as it is,is removed from politics. That everything should be considered "up for grabs," everything subject to reform.

Many understood Unger to be arguing that we should in fact put everything up
for grabs all the time,that nothing should be certain or fixed,that everything should
be in flux, constantly changing. But that is not what Unger meant.

His meaning was instead just this: That we interrogate the necessities of any particular social order; that we ask whether they are in fact necessities; that we demand
that those necessities justify the powers that they order. As Bruce Ackerman puts it,
we must ask of every exercise of power: Why?43 Perhaps not exactly at the moment
when the power is exercised, but sometime.

"Power," in this account,is just another word for constraints that humans can do
something about. Meteors crashing to earth are not "power" within the domain of
"it's all politics." Where the meteor hits is not politics,though the consequences may
well be. Where it hits, however, is nothing we can do anything about.

But the architecture of cyberspace is power in this sense; how it is could be different. Politics is about how we decide. Politics is how that power is exercised,and by
whom.

6 0

If code is law, then, as William Mitchell writes, "control of code is power": "For
citizens of cyberspace, . . . code . . . is becoming a crucial focus of political contest.
Who shall write that software that increasingly structures our daily lives?"44

As the world is now, code wri ters are incre a s i n gly lawmakers a kers . Th ey determ i n e
what the defaults of the Internet will be; whether privacy will be protected; the degree to which anonymity will be allowed; the extent to which access will be guaranteed . Th ey are the ones who set its natu re . Th eir dec i s i on s , n ow made in the
interstices of how the Net is coded, define what the Net is.

How the code reg u l a te s , who the code wri ters are , and who con trols the code
writers—these are questions that any practice of justice must focus in the age of cyberspace. The answers reveal how cyberspace is regulated. My claim in this part of
the book is that cyberspace is regulated, and that the regulation is changing. Its regulation is its code, and its code is changing.

We are entering an age when the power of regulation will be relocated to a structure whose properties and possibilities are fundamentally different. As I said about
Russia at the start of this book, one form of power may be destroyed, but another is
taking its place.

Our aim must be to understand this power and to ask whether it is properly exercised. As David Brin asks,"If we admire the Net,should not a burden of proof fall
on those who would change the basic assumptions that brought it about in the first
place?"45

These "basic assumptions" were grounded in liberty and openness. An invisible

hand now threatens both. We need to understand how.

P A R T T W O

c o d e a n d o t h e r

r e g u l a t o r s

Pa rt 1 set up the probl em : c ybers p ace wi ll not take care of i t s el f . Its natu re is not
given. Its nature is its code, and its code is changing from a place that disabled control to a place that will enable an extraordinary kind of control. Commerce is making that happen ; govern m ent wi ll hel p. Before this happen s , we should dec i de
whether this is the way we want things to be.

In part 2 we will prepare for that choice. I begin by describing a more complex
sense of the life that code makes possible. That's chapter 6. What makes these places
fe el as they do? What arch i tectu res make po s s i ble the life within each? And how
might that life change as the structures that constitute them—their architectures—
change?

Chapter 7 is about the techniques for that change. Building on the pattern I described in chapter 5, I offer a general mo del of regulation that is applicable to cybers p ace as well as real space . My aim is to convey a sense of the power that
government has here, and a stronger sense of why that power will increase—not decrease—over time.

I then de s c ri be an important limitation on to this power—in terms from the introdu cti on , a stru ctu ral con s traint on govern m en t's power. This is the limit implicit in the
open code movem en t . As I argue in ch a pter 8, the power that govern m ent obt a i n s
t h ro u gh the tech n i ques I sketch ed in ch a pter 5, open code takes aw ay. Th ere is thus a
com peti ti on abo ut reg u l a bi l i ty, m ed i a ted by the own ership of the code .

6 2

The aim in the end is to see what is at stake, what is possible, and what limits
there are on what is possible. The argument is not against regulation; the argument
is against a particularly narrow, and useless, conception of regulation. Once we have
a better view of how regulation works, we will see more clearly how we might choose
the space cyberspace should be.

S I X

c y b e r s p a c e s

C yber s pace is not a p l ace . It is ma ny pl ace s . The ch a r act er of t hese many
places is not identical. They instead differ in ways that are fundamental. These differences come in part from differences in the people who populate these places. But
demographics alone won't explain the variance. Something more is going on.

Here is a test. Read the following passage, and ask yourself whether the description rings true for you:

I bel i eve vi rtual com mu n i ties promise to re s tore to Am ericans at the end of t h e
t wen ti eth cen tu ry what many of us feel was lost in the dec ades at the beginning of
the cen tu ry—a stable sense of com mu n i ty, of p l ace . Ask those wh o've been members of su ch a vi rtual com mu n i ty, and they ' ll tell you that what happens there is
m ore than an exch a n ge of el ectronic impulses in the wi re s . It's not just vi rtu a l
b a rn ra i s i n g. . . . It's also the com fort from others that a man like Phil Ca t a l fo of
the WELL can ex peri en ce wh en he's up late at night caring for a child su f suffering n g
f rom leu kem i a , and he logs on to the WELL and po u rs out his anguish and fe a rs .
People re a lly do care for each other and fall in love over the Net , just as they do in
geogra phic com mu n i ti e s . And that " vi rtu a l " con n ectedness is a real sign of h ope
in a nati on that's incre a s i n gly anxious abo ut the fra gm en t a ti on of p u blic life and
the po l a ri z a ti on of i n terest groups and the alien a ti on of u rban ex i s ten ce .1

There are two sorts of reactions to talk like this. To those who have been in this
place for some time, such talk is extremely familiar. These people have been on nets
from the start. They moved to the Internet from more isolated communities—from
a local BBS (bulletin board service), or as Mike Godwin (the author of the passage)
likes to put it, from a "tony" address like "The WELL." For them the Net is a space
for conversation, connections, and exchange, a wildly promising location for making life in real space different.

6 4

But if you are a recent immigrant to this "space" (the old-timers call you "newbi e s" ) , you are likely to be impatient ent with talk like this. Wh en people talk abo ut
"com mu n i ty," a bo ut special ways to con n ect , or abo ut the amazing power of t h i s
space to alter lives, you are likely to ask, "What is this idea of cyberspace as a place?"
For newbi e s , those who have simply e-mailed or su surfaced the World Wi de Web, t h e
"community" of the Net is an odd sort of mysticism. How can anyone think of these
pages full of advertisements and spinning Mickey Mouse icons as a community, or
even as a space? To the sober newbie, this just sounds like hype high on java.2

Newbies are the silent majority of today's Net.3 However much we romanticize
the old days when the Net was a place for conversation and exchange, this is not its
function for most of its users now. Certainly, the world is into "chat," but even ignoring the large portion of that space devoted to sex, chat is not the stuff the WELL
was made of. Most people do not understand what chat or a MOO really is—maybe
they have heard talk about them, but they do not understand what they are about.
They do not understand what life in the community of the WELL, or a MOO, is really like.

In its feel, cyberspace has changed.4 How it looks, what you can do there, how
you are connected there—all this has changed. Why it has changed is a complicated
question—a complete answer to which I can't provide. Cyberspace has changed in
part because the people—who they are, what their interests are—have changed,and
in part because the capabilities provided by the space have changed.

But part of the change has to do with the space itself. Communities, exchange,
and conversation all flourish in a certain type of space; they are extinguished in a
different type of space.5 My hope is to illuminate the differences between these two
environments.

The next sections describe different cyber-places. The aim is an intuition about
how to think through the differences that we observe. This intuition, in turn, will
help us see something about where cyberspace is moving.

T H E V A L U E S O F A S P A C E

S p aces have va lu e s .6 Th ey ex press these va lues thro u gh the practi ces or lives that
they enable or disable. Differently constituted spaces enable and disable differently.
This is the first idea that we must make plain. Here is an example.

At the start of the In tern et , com mu n i c a ti on was thro u gh tex t . Media su ch as
U S E N E T n ewsgro u p s , In tern et Rel ay Ch a t , and e-mail all con f i n ed exch a n ge to
text—to words on a screen, typed by a person (or so one thought).

The reason for this limitation is fairly obvious: the bandwidth of early Net life
was very thin. In an environment where most users connected at 1,200 baud,if they
were lucky, graphics and streaming video would have taken an unbearably long time
to download, if they downloaded at all. What was needed was an efficient mode of
communication—and text is one of the most efficient.7

6 5

Most think of this fact about the early Net as a limitation. Technically, it was. But
this technical description does not exhaust its normative description as an architecture that made possible a certain kind of life. From this perspective, limitations can
be features; they can enable as well as disable. And this particular limitation enabled
classes of people who were disabled in real-space life.

Think about three such classes—the blind,the deaf,and the "ugly."* In real space
these people face an extraordinary array of constraints on their ability to communicate. The blind person in real space is constantly confronted with architectures that
presume he can see; he bears an extraordinary cost in retrofitting real-space architectures so that this presumption is not totally exclusionary. The deaf person in real
space confronts architectures that presume she can hear; she too bears an extraordinary cost in retrofitting these architectures. The "ugly" person in real space (think of
a bar or a social club) confronts architectures of social norms that make his appearance a barrier to a certain sort of intimacy. He endures extraordinary suffering in
conforming to these architectures.

In real space these three groups are con f ron ted with arch i tectu res that disabl e
them relative to "the rest of us." But in cyberspace, in its first iteration,they did not.
The blind could easily implement speech programs that read the (by definition
m ach i n e - re ad a ble) text and could re s pond by typ i n g. Ot h er people on the Net
would have no way of knowing that the person typing the message was blind, unless
he claimed to be. The blind were equal to the seeing.

The same with the deaf. There was no need to hear anything in this early Internet. For the first time many of the deaf could have conversations, or exchanges, in
which the most salient feature was not that the person was deaf. The deaf were equal
to the hearing.

And the same with the "ugly." Because your appearance was not transmitted with
every exch a n ge , the unattractive could have an inti m a te convers a ti on with others
that was not automatically defined by what they looked like. They could flirt or play
or be sexual without their bodies (in an extremely underappreciated sense) getting
in the way. This first version of the Net made these people equal to "the beautiful."
In a virtual chat room, stunning eyes, a captivating smile or impressive biceps don't
do it. Wit, engagement, and articulateness do.

The arch i tectu re of this ori ginal cybers p ace gave these groups som ething that
they did not have in real space. More generally, it changed the mix of benefits and
burdens that people faced—the literate were enabled and the attractive disabled relative to real space. Architectures produced these enablings and disablings.

*It is an important fact abo ut us that it is awk w a rd even to use su ch a word — "u gly"—as if it describes objective features o f humans. I acknowledge the complexity here, and the importance of the escape from humiliation that some parts of society give and other parts of society do not. But we cannot
assume away the burdens that the unattractive suffer relative to the less unattractive. My claim is not that
these are at the level of starvation, or death; my claim is not about their significance. My only aim is to
link what I believe is a disadvantage to features of a space.

6 6

I've told this story as if it matters only to those who in real space are "disabled."
But of course, "disabled"is relative.8 It is more accurate to say that the space changes
the meaning of the enabled. A friend—a strikingly beautiful and powerful woman,
m a rri ed , and su cce s s f u l — de s c ri bed for me why she spends hours in po l i tical ch a t
spaces, arguing with others about all sorts of political topics:

You don't understand what it's like to be me. You have lived your whole life in a
world where your words are taken for their meaning; where what you say is heard
for what it says. I've never had a space, before this space, where my words were
t a ken for what they meant. Alw ays , before , t h ey were words of "this babe ," or
"wife," or "mother." I could never speak as I. But here,I am as I speak.

Clearly, the space is enabling her, even though one would not have said that in

real space she was "disabled."9

Over ti m e , as bandwidth has ex p a n ded , this arch i tectu re has ch a n ged . So has the
mix of ben efits and bu rdens ch a n ged . Wh en gra phics en tered the Net thro u gh the
World Wi de Web, the blind became "bl i n d "a ga i n . As sound files or speech in Ava t a r
s p aces have been cre a ted , the de a f h ave become "de a f" a ga i n . And as chat rooms have
s t a started segrega ting into spaces wh ere vi videocams captu re real images of the peop l e
ch a t ti n g, and spaces wh ere there is just tex t , the vi deo - u n a unappealing are again unappealing a l i n g.1 0 As the arch i tectu res ch a n ge , defin i ti ons of who is "d i s a bl ed " ch a n ge as well .
My point is not to argue that the Net should not change—though of course, if it
can change in ways that minimize the disabling effect of sound and graphics, then it
no doubt should. 11 However important, my point is not really about the "disabled"
at all.I use this example simply to highlight a link—between these structures of code
and the world this code en a bl e s . Codes con s ti tute cybers p ace s ; s p aces en a ble and
disable individuals and groups. The selections about code are therefore in part a selection about who, what,and, most important, what ways of life will be enabled and
disabled.

C Y B E R - P L A C E S

We can build on this point by looking at a number of "communities" that are cons ti tuted differen t ly and that con s ti tute different forms of l i fe , and by con s i considering n g
what makes these differences possible.

A m e r i c a O n l i n e

America Online (AOL) is an online service provider—the largest in the world with
some twelve million subscribers in 1998.12 With twice the population of Massachusetts (at least), AOL describes itself as a "community." A large community perhaps,
but a community nonetheless.

6 7

This com mu n i ty has a con s ti tuti on—not in the sense of a wri t ten doc u m en t
(though there is that as well), but in the sense of a way of life that defines life for
those who live there. Its founding vision was that community would make this place
s i n g. So from its start , AO L's em phasis has been on en a bling people to interact ,
through chat, bulletin boards,and e-mail.Earlier providers, obsessed with providing
con tent or adverti s i n g, l i m i ted or ign ored the po s s i bi l i ties for interacti on and exchange, but AOL saw interaction as the stuff that makes cyberspace different. It built
itself on building a community, establishing itself as a place where people could say
what they wanted.13

This interaction is governed by the rules of the place. Some of these rules are formal,others customary. Among the formal are express terms to which every member
subscribes upon joining AOL. These terms regulate a wide range of behaviors in this
space,including the behavior of AOL members anywhere on the Internet.14

In c re a s i n gly, these rules have become con trovers i a l . AOL policies have been
called "Big Brother" practices. Arguments that get heated produce exchanges that are
ru de . But ru den e s s , or of fen s iven e s s , is not perm i t ted in AO L's com mu n i ty. Wh en
these exchanges are expunged, claims of "censorship" arise.15

My aim here, however, is not to criticize these rules of "netiquette." AOL also has
other rules that regulate AOL members—rules expressed not in contracts but rather
through the very architectures of the space. These rules constitute the most important part of AOL's constitution, yet they are probably the part considered last when
we think about what regulates behavior in this cyber-place.

So consider some examples:
As a member of AOL you can be any one of five people. This is just one amazing
feature of the space. When you start an account on AOL, you have the right to establish up to five identities, through five different "screen names" that in effect establish five different a accounts. Some users, of course, use the five screen names to
give other family members access to AOL. But not everyone uses an AOL account
like this. Think about the single woman, signing up for her first AOL account. AOL
gives her up to five identities that she can define as she wishes—five different personae she can use in cyberspace.

What does that mean? A screen name is just a label for identifying who you are
when you are on the system. It need not (indeed, often cannot) be your own name.
If your screen name is "StrayCat," then people can reach you by sending e-mail to
"straycat@aol.com." If you are online, people can try to talk to you by paging Stray-
Cat on the AOL sys tem ; a dialogue would then appear on your screen asking
whether you want to talk to the person who paged you. If you enter a chat room, the
list of residents there will add you as "StrayCat."

But who is Stray Cat? Here is a second dimen s i on of con tro l . S tray Cat is wh o
StrayCat says she is. She can choose to define herself as no one at all. If she chooses
to place a description of herself in the members' directory, that description can be as
complete or incomplete as she wishes. It can be true or false, explicit or vague,inviting or not. A mem ber stu m bling ac ross Stray Ca t , t h en , in a chat room set up for

6 8

stamp collectors could get her profile and read that StrayCat lives in Cleveland and
is single and female. What happens next is anyone's guess.

Yet this need only be one of StrayCat's five identities. Let's say there is a different
persona that StrayCat likes to have when she wanders through chat rooms. She can
then select another screen name and define it in the directory as she wishes. Perhaps
wh en Stray Cat is having a serious discussion in a newsgroup or po l i tical list she
prefers to speak as hers el f . She could then sel ect a screen name close to her own
name and define it according to who she really is. At other times StrayCat may like
to pretend to be a man—engaging in virtual cross-dressing, and all that might bring
with it.One of her screen names could then be a man's. And so on. The point is the
multiplicity that AOL allows, and the freedom this multiplicity permits.

No one except StrayCat needs to know which screen names are hers. She is not
required to publish the full list of her identities, and no one can find out who she is
(unless she breaks the rules).(After revealing to the U.S. Navy the name of one of its
members so that the Navy could prosecute the person for being a homosexual, AOL
adopted a very strict privacy policy that promises never to allow a similar transgression to happen again.)16

So in AOL you are given a fantastic power of p s eu donym i ty that the "code wri ters" of real space simply do not give . You co u l d , of co u rs e , try in real space to live the
same ra n ge of mu l tiple live s , and to the ex tent that these lives are not incom p a ti ble or
i n con s i s ten t , you could qu i te of ten get aw ay with it. For instance , you could be a Cu b s
fan du ring the su m m er and an opera bu f f du ring the wi n ter. But unless you take extra ord i n a ry steps to hide your iden ti ty, in real space you are alw ays ti ed back to yo u .
You cannot simply define a different ch a racter; you must make it, and more important (and diffic u l t ) , you must sustain its sep a ra ti on from your ori ginal iden ti ty.

That is a first fe a tu re of the con s ti tuti on of AOL—a fe a tu re con s ti tuted by its

code.A second is tied to sp eech—what you can say, and where.

Within the limits of decency, and so long as you are in the proper place, you can
say what you want on AOL. But beyond these limits, speech on AOL is constrained
in a more interesting way. Not the constraint of rules. My point instead is about the
ra n ge of perm i s s i ble speech govern ed by the ch a racter of the po ten tial audien ce .
There are places in AOL where people can gather; there are places where people can
go and read messages posted by others. But there is no space where everyone gathers at one ti m e , or even a space that everyone must soon er or later pass thro u gh .
There is no public space where you could address all members of AOL. There is no
town hall or town meeting wh ere people can complain in public and have thei r
complaints heard by others. There is no space large enough for citizens to create a
riot. The owners of AOL, however, can speak to all. Steve Case, the "town mayor,"
writes "chatty" letters to the members.17 AOL advertises to all its members and can
send everyone an e-mail. But only the owners and those they authorize can do so.
The rest of the mem bers of AOL can speak to crowds on ly wh ere they noti ce a
crowd. And never to a crowd greater than twenty-three.

6 9

This is another feature of the constitution of the space that AOL is, and it too is
a feature defined by code. That only twenty-three people can be in a chat room at
once is a choice of the code engineers. While their reasons could be many, the effect
is clear. One can't imagine easily exciting members of AOL into public action. One
can't imagine easily picketing the latest pricing policy. There are places to go to complain, but you have to take the trouble to go there yourself. There is no place where
members can complain en masse.

Real space is different in this respect. Much of free speech law is devoted to pres erving spaces wh ere dissent can occ u r — s p aces that can be noti ced , and must be
confronted, by nondissenting citizens.18 In real space there are places where people
can gather, places where they can leaflet. People have a right to the sidewalks,public
streets,and other traditional public forums. They may go there and talk about issues
of p u blic import or otherwise say wh a tever they want. Con s ti tuti onal law in re a l
space protects the right of the passionate and the weird to get in the face of the rest.
But no such design is built into AOL.19

This is not to romanticize the power of real-space public forums. We have b ecome such a nonpolitical society that if you actually exercised this constitutionally
protected right, people would think you a nut. If you stood on a street corner and
attacked the latest tax proposal in Congress, your friends would be likely to worry—
and not about the tax proposal. There are exceptions—events can make salient the
n eed for pro te s t — but in the main, t h o u gh real space has fewer con trols thro u gh
code on who can speak where, it has many more controls through norms on what
people can say where. Perhaps in the end real space is much like AOL—the effective
space for public speech is limited,and often unimportant. That may well be. But my
aim here is to identify the feature and to isolate what is responsible for it. And once
again,it turns out to be a feature built into the code.

A third feature of AOL's constitution also comes from its code. This is traceability. While members are within the exclusive AOL content area (in other words, when
they're not using AOL as a gateway to the Internet), AOL can (and no doubt does)
trace your activities and collect information about them. What files you download,
what areas you frequent, who your "buddies" are—all this is available to AOL. These
data are ex trem ely va lu a bl e ; t h ey help AOL stru ctu re its space to fit custom er demand. But gaining the ability to collect these data required a design decision. This
decision too was part of the constitution that is AOL—again, a part constituted by
its code. It is a decision that gives some but not others the power to watch.

AOL is not e xclusive in this enabling capacity. It shares the power. One wonderful fe a tu re of the online space is som ething call ed "bu d dy lists." Add som eone to
your buddy list, and when he comes online you hear the sound of a creaking door
and are notified that he is online. (The "buddy"need not know he is being watched,
though he can,if he knows, block the watching.) If that person goes into a chat area
and you "locate" him, you will be told in what chat area he is. This power, given to
ordinary users, can have complicated consequences. (Imagine sitting at work with

7 0

your buddy feature turned on,watching your spouse come online, enter a chat area,
and—you get the point.) This ability to monitor is built into the space. Individuals
can turn it off, at least for a single watcher, but only if they know about it and think
to change it.

Con s i der one final fe a tu re of the con s ti tuti on of AO L , cl o s ely linked to the last:
com m erce . In AOL you can buy things . You can buy things and down l oad them , or
buy things and have them sent to your hom e . Wh en you buy, you buy with a screen
n a m e . And wh en you buy with a screen name, AOL knows (even if no one else doe s )
just who you are . It knows who you are , it knows wh ere you live in real space , a n d
most import a n t , it knows your credit card nu m ber and the sec u ri ty it provi de s .

AOL knows who you are—this is a fe a tu re of its de s i gn . All your beh avi or on
AOL is watch ed ; a ll of it is mon i tored and tracked back to you as a user. AO L
promises not to co ll ect data abo ut you indivi du a lly, but it cert a i n ly co ll ects data
about you as part of a collective. And with this collective, and the link it provides
back to you, AOL is a space that can better, and more efficiently, sell to you.

These four features mark AOL space as different from other places in cyberspace.
It is easier for AOL to identify who you are, and harder for individuals to find out
who you are; easier for AOL to speak to all its "citizens" as it wishes, and harder for
dissidents to organize against AOL's views about how things ought to be; easier for
AOL to market , and harder for indivi duals to hide . AOL is a different norm a tive
world; it can create this different world because it is in control of the architecture of
that world. Members in that space face, in a sense, a different set of laws of nature;
AOL makes those laws.

My aim is not to criticize the creation of this world or to say that it is improper.
No doubt AOL makes promises to its members that are designed to allay some of the
concern that this control creates, and no doubt if the place became oppressive, the
market would provide plenty of alternatives.

Rather my objective is to impart a sense of what makes AOL the way it is. It is not
just wri t ten ru l e s ; it is not just custom ; it is not just the su pp ly and demand of a
knowing consuming public. What makes AOL is in large part the structure of the
space. You enter AOL and you find it to be a certain universe. This space is constituted by its code. You can resist this code—you can resist how you find it,just as you
can resist cold weather by putting on a sweater. But you are not going to change how
it is. You do not have the power to change AOL's code, and there is no place where
you could rally AOL members to force AOL to change the code. You live life in AOL
subject to its terms; if you do not like them, you go elsewhere.

These features of the AOL space have important implications for how it is regulated. Imagine there is a problem on AOL that AOL wants to stop. It wants to prevent or at least control a certain behavior. What tools does AOL have?

First, it has all the tools that any club, fraternity, or "community" might have. It
can announce rules for its members (and AOL certainly does). Or it can try to stigmatize the behavior, to use the norms of the community to help regulate the problem. This AOL does as well. Alternatively, if the problem comes from the overuse of

7 1

a particular resource, then the managers at AOL can price that resource differently,
exacting a tax to reduce its usage, or a different price for those who use it too much.
But AOL has something more at hand. If AOL does not like a certain behavior,
then in at least some cases it can regulate that behavior by changing its architecture.
If AOL is trying to control indecent language,it can write routines that monitor lang u a ge usage ; i f t h ere is improper mixing bet ween adults and kids, AOL can track
who is talking to whom; if there is a virus problem caused by people uploading infected files,it can run the files automatically through virus checkers; if there is stalking or harassing or thre a tening beh avi or, AOL can bl ock the con n ecti on bet ween
any two individuals.

In short, AOL can deal with certain types of problems by changing its code. Because the universe that AOL members know (while in AOL) is defined by this code,
AOL can use the code to regulate its members.

Think a bit about the power I am describing—and again, I am not complaining
or criticizing or questioning this power, only describing it. As you move through this
space that AOL defines—entering a chat area, posting a message to a bulletin board,
entering a discussion space, sending instant-messages to another person, watching
or following other people,uploading or downloading files from sites, turning to certain ch a n n els and re ading certain arti cl e s , or ob s e s s ively paging thro u gh a space
looking for pictures of a certain actor or actress—as you do any of these things, AOL
is, in an important sense, there. It is as if the system gives you a space suit that you
use to navigate the space but that simultaneously monitors your every move.

In principle,the potential for control is extraordinary. Imagine AOL slowing the
response time for a certain kind of service it wants to discourage, or channeling the
surfer through ads that it wants customers to see, or identifying patterns of behavior that its monitors would watch,based on the fear that people with patterns like X
are typically dangerous to people of type Y. I do not think AOL engages in activities
like these,and I am not even saying that there would be anything wrong if it did. But
it is imp ortant to note that the potential for control in this "community" is unlimited—not in the sense that AOL could make life miserable (since people would then
leave), but in the sense that it has a regulatory tool that others,in both real spa ce and
other cyberspaces, do not. Its power is, of course, checked by the market, but it has
a tool of control that others in the market, but outside cyberspace, do not have.

In pri n c i p l e , t h en , AOL must ch oo s e . Every time AOL dec i des that it wants to
regulate a certain kind of behavior, it must select from among at least four modalities e s — ru l e s , n orm s , pri ce s , or arch i tectu re . And wh en sel ecting one of these fo u r
modalities, selecting architecture as a regulator will often make the most sense.

C o u n s e l C o n n e c t

David Johnson began Counsel Connect (CC) in 1992 as an online lawyers' cooperative. The idea was simple: give subscribers access to each other; let them engage in
convers a ti ons with each other; and thro u gh this access and these convers a ti on s ,

7 2

value would be created. Lawyers would give and take work; they would contribute
i deas as they found ideas in the space . A different kind of l aw practi ce wo u l d
emerge—less insular, less exclusive,more broadly based.

I thought the idea amazing, though many thought it nuts. For a time the system
was carried by Lexis; in 1996 it was sold to American Lawyer Media, L.P.; in 1997 it
migrated to the Internet and remains there today. It boasts thousands of subscribers,
though it is hard to know how many of them contribute to the discussion online.
Many no doubt simply watch the discussions of others, perhaps linking three or four
discussion groups of their particular interest, plus a few of more general interest.

This is how the more interesting feature of the space is designed: legal topics are
d ivi ded into discussion gro u p s , with each group led by a discussion leader. Th e
leader is not a moderator; he or she has no power to cancel a post. The leader is there
to inspire convers a ti on — to indu ce others to speak by being en co u ra ging or
provocative.

There are today some ninety groups in this space. The poster of a particular message may have it removed, but if the poster does not remove it, it stays—at first in
the list of topics being discussed,and later in an archive that can be searched by any
member.

Members pay a fee to join and get an account with their real name on it. Postings
use members' real names,and anyone wondering who someone is can simply link to
a directory. Members of CC must be members of the bar, unless they are journalists.
Others have no right to access; the community here is exclusive.

Postings in the space look very much like postings in a USENET newsgroup. A
thread can be started by anyone, and replies to a thread are appended to the end. Because messages do not move off the system, you can easily read from the start of a
thread to its end. The whole conversation, not just a snippet,is preserved to be read.
These features of CC space were obviously designed. The architects of the space
chose to enable certain features and to disable others. We can list here some of the
effects of these choices.

First, there is the effect of being required to use your own name. You are more
l i likely to think before speaking and to be careful abo ut being ri ght before sayi n g
something definitive. You are constrained by the community, which will judge what
you say, and in this community you cannot escape from being linked to what you
have said. Responsibility is a consequence of this architecture, but so is a certain inhibition. Does a senior partner at a leading law firm really want to ask a question
that wi ll announce his ign ora n ce abo ut a certain area of l aw? Names cannot be
changed to protect the ignorant, so they will often simply not speak.

Secon d , t h ere is an ef fect from forcing all discussion into thre ad s . Po s ti n gs are
kept together; a question is asked, and the discussion begins from the question. If
you want to con tri bute to this discussion , you must first re ad thro u gh the other
postings before responding. Of course,this is not a technical requirement—you certainly have a choice not to read. But if you do not read through the entire thread,

7 3

you could well be repeating what another has said and so reveal that you are speaking wi t h o ut listen i n g. Aga i n , the use of real names ties mem bers' beh avi or to the
norms of the community.

Third, there is the effect of reputation: the reputation you build in this space is
based on the kind of advice you give. Your reputation survives any particular post
and is, of co u rs e , a f affected by any su b s equ ent po s t s . These posts are arch ived and
searchable. If you say one thing about topic X and then the opposite later on, you are
at least open to a question about consistency.

Fourth,there is the effect of tying reputation to a real name in a real community
of profe s s i on a l s . Mi s beh aving here matters el s ewh ere . CC thus gets the ben efit of
that community—it gets the benefit, that is, of the norms of a par ticular community. These norms might support relatively productive community behavior—more
productive, that is,than the behavior of a group whose members are fundamentally
mixed. They might also sup port punishing those who deviate from appropriate behavior. Thus, CC g ets the benefit o f community sanc tion to control improper b ehavior, whereas AOL must rely on its own content police to ensure that people stay
properly on topic.

We can describe the world of CC that these features constitute in two different
ways, just as we can describe the world AOL constitutes in two different ways. One
is the life that CC's features make possible—highly dialogic and engaged, but monitored and with consequences. The other is the regulability by the manager of the life
that goes on in the CC space. And here we can see a significant difference between
this space and AOL.

CC can use the norms of a com mu n i ty to reg u l a te more ef fectively than AO L
can. CC benefits from the norms of the legal community; it knows that any misbehavior will be sanctioned by that community. There is, of course, less "behavior" in
this space than in AOL (you do fewer things he re), but such as it is, CC behavior is
quite significantly regulated by the reputations of members and the consequences of
using their real names.

These differences together have an effect on CC's ability to regulate its members.
They enable a regulation through modalities other than code. They make behavior
in CC more regulable by norms than behavior in AOL is. CC in turn may have less
control than AOL does (since the controlling norms are those of the legal community), but it also bears less of the burden of regulating its members' behavior. Limiting the pop u l a ti on , making mem bers' beh avi or publ i c , tying them to their re a l
names—these are the tools of self-regulation in this vir tual space.

But CC is like AOL in an important way. Neither is a democracy. Management in
both cases controls what will happen in the space—again, not without constraint,
for the market is an important constraint. But in neither place do "the people" have
the power to con trol what goes on . Perhaps they do, i n d i rect ly, in CC more than
AOL, since it is the norms of "the people" that regulate behavior in CC. But these
norms cannot be used against CC directly. The decisions of CC and AOL managers

7 4

may be affected by market forces—individuals can exit, competitors can steal customers away. But voting doesn't direct where either CC or AOL goes.

That's not the case with the next cyber-place. At least,not anymore.

L a m d a M O O

L a m d a M OO is a vi rtual re a l i ty. It is a tex t - b a s ed vi rtual re a l i ty. People from ac ross the
world (tod ay close to six thousand of t h em) link to this space and interact in ways that
the space perm i t s . The re a l i ty is the produ ct of this interacti on . In d ivi duals can parti ci p a te in the con s tru cti on of this re a l i ty — s om etimes for upw a rds of ei gh ty hours a
wee k . For some this interacti on is the most su s t a i n ed human con t act of t h eir en ti re
l ive s . For most it is a kind of i n teracti on unmatched ed by anything else they know.

In the main, people just talk here. But it is not the talk of an AOL chat room. The
talk in a MUD is in the service of construction—of constructing a char acter and a
community. You interact in part by talking, and this talking is tied to a name. This
name, and the memories of what it has done,live in the space, and over time people
in the space come to know the person by what these memo ries recall.

The life within these MUDs differ. E l i z a beth Reid de s c ri bes two differen t
"styles"20—social-style MUD and an adventure or game-style MUD. Social MUDs
are simply online communities where people talk and build characters or elements
for the MUD. Adventure MUDs are games, with (virtual) prizes or power to be won
through the deployment of skill in capturing resources or defeating an enemy. In either context,the communities survive a particular interaction. They become virtual
clubs, though with different purposes. Members build reputations through their behavior in these clubs.

You get a ch a racter simply by joining the MOO (though in LamdaMOO the waiting list for a ch a racter ex tends over many mon t h s ) . Wh en you join the space , you define the ch a racter you wi ll have . At least, you define certain fe a tu res of your ch a racter.
You sel ect a name and a gen der (no gen der is an opti on as well) and de s c ri be yo u r
ch a racter. Some de s c ri pti ons are qu i te ord i n a ry (Jo h n ny Manhattan is "t a ll and thin,
pale as string ch ee s e , we a ring a nei gh borh ood hat" ) .2 1 Ot h ers , h owever, a re qu i te extra ord i n a ry. ( Leg b a , for instance , is a Ha i tian tri ck s ter spirit of i n determ i n a te gen der,
brown - s k i n n ed and we a ring an ex pen s ive pe a rl gray su i t , top hat, and dark gl a s s e s .)2 2
Julian Dibbell broke the story of this space to the nonvirtual world in an article
in the Vi ll a ge Vo i ce .2 3 The story that was the focus of Di Dibbell 's arti cle invo lved a
character called Mr. Bungle who, it turns out, was actually a group of NYU undergraduates sharing this single identity. Bungle entered a room late one evening and
found a group of characters well known in that space. The full story cannot be told
any better than Dibbell tells it. For our purposes,the facts will be enough. 24

Bu n gle had a special sort of power. By earning special standing in the LamdaMoo community, he had "voodoo" power: he could take over the voices and actions of other characters and make them appear to do things they did not really do.
This Bungle did that night to a group of women and at least one person of ambiguity y b e r s p a c e s

7 5

ous gender. He invoked this power, in this public space, and took over the voices of
these people. Once they were in his control, Bungle "raped" these women, violently
and sadistically, and made it seem as if they enjoyed the rape.

The "rape" was vir tual in the sense that the event happened only on the wires.

"No bodies touched," as Dibbell describes it.

Whatever physical interaction occurred consisted of a mingling of electronic signals sent from sites spread out between New York City and Sidney, Australia.

. . . He commenced his assault entirely unprovoked at, or about 10 P.M. Pacific
S t a n d a rd Ti m e . . . . [H]e began by using his voodoo do ll to force one of t h e
room's occupants to sexually service him in a variety of more or less conventional
w ays . That this vi ctim was ex u . . . . He tu rn ed his atten ti ons now to Moondreamer . . . forcing her into unwanted liaisons with other individuals present in
the room . . . . His acti ons grew progressively s s ively vi o l en t . . . . He caused Moondreamer re a m er to vi o l a te hers el f with a piece of k i tch en cut l ery. He could not be
stopped until at last someone summoned Iggy . . . who brought with him a gun
of near wizardly powers, a gun that didn't kill but enveloped its targets in a cage
impermeable even to a voodoo doll's powers.25

Rape is a difficult word to use in any context, but particularly here. Some will object that whatever happened in this virtual space, it has nothing to do with rape. Yet
even if " i t" was not "ra pe ," a ll wi ll see a link bet ween ra pe and what happen ed to
these wom en there . Bu n gle used his power over these wom en for his own (and
against their) sexual desire; he sexualized his violence and denied them even the dignity of registering their protest.

For our purpo s e s , wh et h er what happen ed here was re a lly ra pe is be s i de the
point. What matters is how the community reacted. The community was outraged
by what Bu n gle had don e , and many thought som ething should be done in response.

Th ey ga t h ered then , this com mu n i ty of m em bers of L a m d a M OO, in a vi rtu a l
room at a set ti m e , to discuss what to do. Some thirty showed up, the largest meeting the com mu n i ty had known . Some thought that Bu n gle should be ex pell ed —
"toaded ," as it is de s c ri bed , k i ll ed for purposes of the MOO. Ot h ers thought that
nothing should be don e ; Bu n gle was cert a i n ly a creep, but the best thing to do to
c reeps was simply to ign ore them . Some call ed on the Wi z a rds of the space — t h e
c re a tors , the god s — to intervene to deal with this ch a racter. The Wi z a rds decl i n ed :
t h eir job, t h ey rep l i ed , was to cre a te the worl d ; the mem bers had to learn to live
within it.

There was really no law that governed what Bungle had done. No real-space law
reached sexual pranks like this, and neither did any explicit rule of LamdaMOO.26
This troubled many who wanted to do something . Invoking real-space ideals about
fair notice and due process, these people argued that Bungle could not be punished
for violating rules that did not exist at the time.

7 6

Two ex tremes even tu a lly em er ged . One side urged vi gi l a n ti s m : Bu n gle was a
miscreant, and something should be done about him. But what shouldn't be done,
t h ey argued , was for LamdaMOO to re s pond by cre a ting a world of reg u l a ti on .
LamdaMOO did not need a state; it needed a few good vigilantes. It needed people
who would enforce the will of the community without the permanent intrusion of
some central force called the state. Bungle should be expelled, killed, or "toaded"—
and someone would do it. If only the group resisted the call to organize itself into a
state.

The other side p romoted just one idea: democracy. With the cooperation of the
Wi z a rd s , L a m d a M OO should establish a way to vo te on rules that would govern
how people in the space behaved. Any question could be made the subject of a ballot; there was no constitution limiting the scope of what democracy could decide.
An issue decided by the ballot would be implemented by the Wizards. From then on,
it would be a rule.

Both extremes had their virtues. Both invited certain vices. The anarchy o f the
first risked chaos. It was easy to imagine the community turning against people with
little or no warning; one imagined vigilantes roaming the space, unconstrained by
a ny ru l e s , "toad i n g" people whose crimes happen ed to stri ke them as "awf u l ." For
those who took this place less se riously than real space, this compromise was tolera bl e . But what was to l era ble for some was into l era ble to others—as Bu n gle had
learned.

Dem oc racy seem ed natu ra l , yet many re s i s ted it as well . The idea that po l i ti c s
could exist in LamdaMOO seemed to sully the space. The thought that ideas would
have to be debated and then voted on was just another burden. Sure, rules would be
known and behavior could be regulated, but it all began to seem like work. The work
took something from the fun the space was to have been.

In the end, both happened. The debate that evening wound down after almost
three hours. No clear resolution had found its way in. But a resolution of sorts did
occur. As Dibbell describes it:

It was also at this poi n t , most likely, that Tom Traceb ack re ach ed his dec i s i on .
TomTraceback was a wizard, a taciturn sort of fellow who'd sat brooding on the
sidelines all evening. He hadn't said a lot, but what he had said indicated that he
took the crime committed against exu and Moondreamer very seriously, and that
he felt no particular compassion toward the character who had committed it. But
on the other hand he had made it equally plain that he took the elimination of a
fellow player just as seriously, and moreover that he had no desire to return to the
days of wizardly intervention. It must have been difficult, therefore, to reconcile
the con f l i cting impulses chu rning within him at that mom en t . In fact , it was
probably impossible, for . . . as much as he would have liked to make himself an
instrument of the MOO's collective will, [he surely realized that under the present order of things] he must in the final analysis either act alone or not act at all.

So TomTraceback acted alone.

7 7

He told the lingering few players in the room that he had to go, and then he
went. It was a minute or two before 10 P.M. He did it quietly and he did it privately, but all anyone had to do to know he'd done it was to type the @who comm a n d , wh i ch was norm a lly what you typed if you wanted to know a player 's
present location and the time he last logged in. But if you had run a @who on Mr.
Bu n gle not too long after Tom Traceb ack left em m el i n e's room , the database
would have told you something different.

"Mr_Bungle," it would have said,"is not the name of any player."
The date, as it happened, was April Fool's Day, but this was no joke: Mr. Bungle was truly dead and truly gone.27

When the Wizards saw this, they moved to the other extreme. With no formal
dec i s i on by the citi zen s , the Wi z a rds call ed forth a dem oc rac y. S t a starting May 1,
1993,28 any matter could be decided by ballot,and any proposition receiving at least
twice as many votes for as against would become the law.29 Many wondered whether
this was an advance or not.

There is a lot to think about in this story, even in my savagely abridged version.30
But I want to focus on the sense of loss that accom p a n i ed the Wi z a rd s' dec i s i on .
Th ere is a certain rom a n ce ti ed to the idea of e s t a blishing a dem oc rac y — Kod a k
com m commercials with te a tearful Berl i n ers as the Wa ll comes down and all that. The romance is the idea of self-government and of establishing structures that facilitate it.
But LamdaMOO's move to self-government, through structures of democracy, was
not just an achievement. It was also a defeat. The space had failed. It had failed, we
could say, to self-regulate. It had failed to engender values in its population sufficient
to avoid just the sort of evil Bungle had perpetrated. The debate marked the passage
of the space from one kind of p l ace to another. From a space sel f - reg u l a ted to a
space regulated by self.

It might seem odd that there would be a place where the emergence of democracy would so depress people. But this kind of reaction is not uncommon in cyberplaces. Katie Hafner and Matthew Lyon tell a story of the emergence of a "widget"
called the FINGER command on UNIX, that would allow users to see when the last
time another user had been on the computer, and whether she had read her mail.
Some thought (not surprisingly, I should think) that this command was something
of an invasion of privacy. Whose business was it when I was last at my machine, and
why should they get to know whether I have read my mail?

A programmer at Carnegie Mellon University, Ivor Durham, changed the command to give the user the power to avoid this spying finger. The result? "Durham
was flamed without mercy. He was called everything from spineless to socially irresponsible to a petty politician, and worse—but not for protecting privacy. He was
criticized for monkeying with the openness of the network."31

The values of the UNIX world were different. They were values embedded in the
code of UNIX. To change the code was to change the values, and members o f the
community fought that change.

7 8

So too with the ch a n ges to LamdaMoo. Before the ball o ti n g, L a m d a Moo was
regulated through norms. These regulations of social st ructures were sustained by
the constant policing of individual citizens. They were the regulations of a commun i ty; the rise of dem oc racy marked the fall of this com mu n i ty. Al t h o u gh norm s
would no doubt survive the establishment of a democracy, their status was forever
changed. Before the democracy, a st struggle over which norms should prevail could
be resolved only by consensus—by certain views prevailing in a decentralized way.
Now su ch a stru ggle could be re s o lved by the power of a majority ty—not thro u gh
what a majority did, but through how they voted.

I 've rom a n ti c i zed this bi z a rre little world far more than I inten ded . I do not
mean to su ggest that the world of L a m d a M OO before dem oc racy was nece s s a ri ly
better than the one after. I want only to mark a particular change.Like CC, and unlike AOL,LamdaMOO is a place where norms regulate. But unlike CC,LamdaMOO
is now a place where members have control over restructuring the norms.

Such control changes things. Norms become different when ballots can overrule
t h em . And code becomes different wh en ballots can order Wi z a rds to ch a n ge the
world. These changes mark a movement from one kind of normative space to another, from one kind of regulation to another.

In all three of these cyber-places, code is a regulator. But there are important differences among the three. Norms have a relevance in CC and LamdaMOO that they do
not in AOL; democracy has a relevance in LamdaMOO that it does not have in CC
or AO L . And mon i toring has a rel eva n ce in AOL that it does not have in LamdaMOO or CC (since neither of the latter two use data about individuals for commercial purposes, either internal or external to the organization). Code constitutes
these three communities; as Jennifer Mnookin says of LamdaMoo, "politics [is] imp l em en ted thro u gh tech n o l ogy."3 2 Di f feren ces in the code con s ti tute them differently, but some code makes community thicker than others. Where community is
thick, norms can regulate.

The final space in this sur vey is also constituted by code, though in this case the
"m a n a gem en t" has less abi l i ty to ch a n ge its basic arch i tectu re . This code is net
code—a protocol of the Internet that is not easily changed by a single user. At least
it was not easy for me.

. l a w . c y b e r

His name was IBEX, and no one knew who he was. I prob a bly could have figured
it out—I had the data to track him down — but after he did what he did, I did not
want to know who he was. He was prob a bly a stu dent in the very first class abo ut
c ybers p ace that I taught t , and I would have failed him, for I was furious abo ut wh a t
he had don e . The class was "The Law of Cybers p ace" ; vers i on one of that class was
at Ya l e .

7 9

I say version one because I had the extraordinary opportunity to teach that class
at three extraordinary law schools—first at Yale, then at the University of Chicago,
and finally at Harvard. These were three very different places, with three very different student bodies, but one part of the course was the same in each place. Every year
a "n ewsgro u p" was assoc i a ted with the class—an el ectronic bu ll etin boa rd wh ere
s tu dents could post messages abo ut qu e s ti ons ra i s ed in the co u rs e , or abo ut anything at all . These po s ti n gs began convers a ti on s — t h re ads of d i s c u s s i on , one message posted after another, debating or questioning what the earlier message had said.
These newsgroups constituted what philosophers might call "dialogic communities." They were spaces where discussion could occur, but where what was said was
preserved for others to read, as in CC. That was the dialogic part. The community
was what was made over time as people got to know each other—both in this space
and in real space. One year students in the class and students outside the class (who
had been watching the .law.cyber discussions develop) had a party; another year the
students outside the class were invited to attend one class. But over the three years,
at three different schools, it was clear that three communities had been made. Each
was born on a particular date, and each lived for at least a couple of months.

My story here comes from Yale. Yale is an odd sort of law school, though odd in
a good way. It is small and filled with extremely bright people, many of whom do
not really want to be lawyers. It fashions itself as a community, and everyone from
the dean on down (not a "Yale" way to describe things) strives continuously to foster and sustain this sense of com mu n i ty among the stu den t s . To a large ex ten t , i t
works—not in the sense that there is perpetual peace, but in the sense that people
everywhere are aware of this sense of community. Some embrace it, others resist it,
but the resistance, like an embrace, says that something is there. One does not resist
the community of people on a Greyhound bus.

One ex tra ord i n a ry fe a tu re of the Yale Law Sch ool is "the Wa ll ." The Wa ll is a
place where people can post comments about whatever in the world they want to
say. A letter can be posted about gay rights at Yale, or a protest about Yale's treatment
of unionized workers. Political messages are posted as well as points about law. Each
posting makes additional ones possible—either scribbled on the original post or appended underneath the post.

An extraordinary sign for any visitor, the Wall is located right at the center of the
law school. In the middle of a fake Gothic structure is a stone space with scores of
papers posted in random fashion. Around the posts stand wandering students, reading what others have said. This is Ya l e's spe a kers' corn er, t h o u gh the spe a kers are
wri ters , and the wri ting is su b s t a n tive . Th ere is little to be ga i n ed on the Wa ll
through rhetoric; to gain respect there, you must say something of substance.

One rule, however, governs this space. All postings must be signed; any posting
without a signature is removed. Originally, no doubt, the rule meant that the posting be signed by the person who wrote it. But because this is Yale, where no rule can
exist without a thousand questions raised,a custom has emerged whereby an anonymous-

8 0

mous post can be signed by someone not its author ("Signed but not written by X").
That signature gives the post the pedigree it needs to survive on the Wall.

The reasons for this rule are clear, but so too are its problems. Let's say you want
to criticize the dean for a decision he has made. The dean,however sweet, is a powerful person. You might well prefer to post a message without your name attached to
it.Or say you are a student with political views that make you an outsider. Posting a
m e s s a ge with those vi ews and your sign a tu re might draw the scorn of your cl a s classmates. Free speech is not speech without consequence, and scorn, or shame, or ostracism, are likely consequences of lots of speech.

An onym i ty, t h en , is a way around this dilem m a . With anonym i ty, you can say
what you want wi t h o ut fe a r. In some cases, for some peop l e , the ri ght to spe a k
anonymously makes sense.

Still, a community might want to resist this right. Just as anonymity might give
you the strength to state an unpopular view, it can also shield you if you post an irresponsible view. Or a slanderous view. Or a hur tful view. You might want to question the policies of the dean, or you might want falsely to accuse a fellow student of
cheating. Both utterances benefit from anonymity, but the community has good reason to resist utterances like the second.

As far as I know, IBEX never said anything on the Wall. Instead, he spoke in the
newsgroup associated with my class. By design, the newsgroup was open to anyone
at Yale who wanted to speak. Unlike the Wall,however, the technology allowed users
to call themselves whatever they wanted."IBEX," of course, was a pseudonym. For
purposes of the Wall,a pseudonym was just like anonymous speech—you had to use
your real name. But in a newsgroup a pseudonymous posting is quite different from
an anonymous posting . Over time you can come to know the character of a pseudonym. In the class that year, along with IBEX, we had SpeedRacer, MadMacs, Cliff-
Cl aven , Al i en s , bl a h , and Ch ri s toph er Robbin n . While mem bers of the class migh t
know who these participants were (we all knew who MadMacs was, but only a few
of us knew Speed Racer ) , e ach pseudonym donym had a ch a racter wh et h er people knew
who they were or not.

The character of IBEX was bad. This much was clear from the start. Before IBEX
a ppe a red , l i fe in the space flo u ri s h ed . At first people were ti m i d , but po l i te . Brave
souls would post an idea or a joke . The convers a ti on would con ti nue around the
idea or joke for a bit. After a couple of weeks the conversation would become quite
i n ten s e . Pa t terns of exch a n ge bega n . People had qu e s ti on s ; o t h ers had answers .
People stumbled as they spoke, but they were beginning, slowly, to speak.

Some things about how they spoke were immediately noticeable. First, women
spoke more in this space than they did in class. Maybe not more in a statistically significant sen s e , but more .3 3 Secon d , h el pers qu i ck ly devel oped , and those who received their help. Soon a class developed online—a real class that id identified itself as
such and spoke as a class in a way that a teacher dreams of in real space,and in a way
I had never known.

8 1

Why this happened I could not really say. Una Smith may have been a catalyst. I
said that I taught this course three times. Each time (without my intervention at all)
there was an Una Smith participating in the newsgroup. At Yale she was a real person, but after Yale I thought of her as a t ype.She was always a woman from outside
the cl a s s ; she was alw ays ex trem ely knowl ed ge a ble abo ut the Net and abo ut
USENET; and she always wandered into my (virtual) class and began telling the others how they should behave. When someone violated a norm of the Net, Una would
correct them. Often this instruction was not taken terribly well (these were, after all,
law students). Soon the class would rally to defend the instructed and to challenge
her to defend her rules. And of course, expert that she was, she usually had an answer that did defend the rules she had dictated. This exchange soon became a focus
of the class. Una had drawn their anger, and the class gained cohesiveness as a result.
About a month and a half into the course,the group reached an apex of sorts. It
became the best it would be. I remember the moment well. Early on a spring afternoon I noticed that someone had posted the first line of a poem. By the end of the
d ay, wi t h o ut any coord i n a ti on , the class had finished the poem . Th ere had been
rhythm to the exchanges; now there was rhyme. Things hummed in the newsgroup,
and people were genuinely surprised about this space.

It was then that IBEX appe a red . I think it was just after we had discussed
anonymity in class, so maybe his later claims to have been serving a pedagogical role
were true. But he appeared after one of our classes—appeared, it seemed, just to issue an attack on another mem ber of the cl a s s . Not an attack on his ide a s , but on
him. So vicious and so extensive was this attack that when I read it, I didn't know
quite how to understand it. Could it have been real?

Almost immediately, conversation in the group died. It just stopped. No one said
a nyt h i n g, as if everyone were afraid that the mon s ter that had en tered our space
would turn his fury on one of them next. Until, that is, the victim responded, with
an answer that evinced the wounds of the attack. IBEX's words had cut. The victim
was angry and hurt, and he attacked back.

But his salvo only inspired another round of viciousness, even more vile than the
first. With this, other members of the class could not resist joining in. IBEX was attacked by a string of characters in the class as cowardly for hiding behind a pseudonym and as sick for what he had said. None of this had any effect. IBEX came back,
again and again, with an ugliness that was as extreme as it was unrelenting.

The space had been changed. Conversation fell off, people drifted away. Some no
doubt left because they were disgusted with what had happened;others did not want
to be IBEX's next target. There was a brief period of life in the space as people rallied to attack IBEX. But as he came back again and again, each time more vicious
than the last, most simply left the space.(One time IBEX came back to protest that
he had been wronged; in the week before, he claimed, he had not posted anything,
but someone wearing the white sheet of IBEX had posted in IBEX's name,so that he,
the real IBEX, had been defamed. The class had little sympathy.)

8 2

But it was not just the online class that changed. As we met face to face each week
I felt the atm o s ph ere ben d . People felt the cre a tu re in the room , t h o u gh no on e
could believe he was a student at the Yale Law School. This was their classmate,hiding behind a smile, or a joke, in real spa ce, but vicious in cyberspace. And the very
idea that this evil was hidden under a smile changed how people felt about smiles.
Some called this the "David Lynch effect," an allusion to the film producer who
portrays the rot of society just under freshly painted facades. We felt in that class the
rot of our com mu n i ty just under the su rf ace of smiling and functi onal stu den t s .
There was a (relatively tame) Jake Baker in our midst. The space had permitted beh avi or that de s troyed com mu n i ty — com mu n i ty that the space itsel f h ad cre a ted .
Community had been created in part through the ability to hide—to hide behind a
benign pseudonym; to hide hesitation, or editing, in the writing; to hide your reaction; to hide that you were not paying attention. These anonymities had made the
community what it was. But the same anonymity that created the community gave
birth to IBEX as w ell,and thus took the community away.

H O W A R C H I T E C T U R E S M A T T E R A N D

S P A C E S D I F F E R

I said this at the start, but now it should have some real meaning: cyberspace is not
a place; it is many places. Its places don't have one nature; the places of cyberspace
have many different "natures." These natures are not given, they are made. They are
set (in part at least) by the architectures that constitute these different spaces. These
architectures are themselves not given; these architectures of code are set by the architects of cyberspace—code writers.

The spaces I have de s c ri bed h ere a re differen t . These differen ces have been the
purpose of my description. My aim has been to remind you of the different character that these places have, and to remind you again of the reasons that these places
have these differences.

In some places there is com mu n i ty—that is, a set of n orms that are sel f -
en forcing within the gro u p. Fe a tu res su ch as vi s i bi l i ty (as oppo s ed to anonym i ty) and
n on tra n s i en ce help cre a te those norm s ; a n onym i ty, tra n s i en ce , and divers i ty make it
h a rder to cre a te com mu n i ty.

In places where community is not ful ly self-enforcing, norms are supplemented
ei t h er by rules impo s ed thro u gh code or by rules recogn i zed thro u gh dem oc ra ti c
procedures. These supplements may further some normative end, but at times they
are in tension with the goal of community building.

If we had to simplify this divers i ty of s p aces by finding one dimen s i on alon g
wh i ch we could rank them , that dimen s i on might be their amen a bi l i ty to out s i de
control. "Community" in the sense that I've used the word means a group able to
en force its own norms among its mem bers . In this, the groups I've discussed are

8 3

universally vulnerable—.law.cyber being the most vulnerable. But as we move from
.law.cyber to CC to LamdaMOO to AOL,the ability to enforce a norm on the group
from the outside increases. In .law.cyber, people within the space can argue all they
want about introducing a new norm or changing an existing one, but a norm b becomes a group norm on ly if the whole group comes to see it as va lu a bl e , and so
adopts it. No external control is possible.

The possibility of external control is greater in CC, though CC and AOL share a
market constraint. In both, management can change the code to bring about a particular end, but if that end is too far removed from what most members think the
space is about, they may simply leave. As a result, AOL has more control than CC;
because the range of behavior on AOL is wider, the range of possible rules in this
space is greater as well.

In LamdaMOO the story is more complicated. Nothing really binds people to a
particular MOO. (There are thousands, and most are free.) But because characters
in a MOO are earned rather than bought,and because this takes time and characters
are not fungible, it becomes increasingly hard for members of a successful MOO to
move elsewhere. They have the right to exit, but in the sense that Soviet citizens had
the right to exit—namely, with none of the assets they had built in their particular
world.

The members of a MOO are in a sense the most vulnerable to changes imposed
f rom the out s i de . Because the world of the MOO is (like AOL) com p l etely constricted by code (whether collectively or individually), it is here that the control has
the potential to be the greatest.

T R A D E - O F F S O F C O N T R O L

Our look at these contrasting spaces should give depth to the idea that architecture
matters and highlight the different ways in which the code of a cyberspace might enable or disable certain forms of life. Cyberspaces differ not only in the amount of
regulation that each permits;they also differ in the values they embrace and the kind
of regulation they permit. Some spaces can be regulated by norms; code can change
that. Some places cannot be regulated by norms; sometimes code can change that as
well. The regulating norms can be those of real space as well as of cyberspace. And,
as we saw in the discussion of Jake Baker, the architecture of cyberspace may permit
an escape from the regulations of real space into a space regulated very differently.
The choices are rich, but they are choices.34

If we let the invisible hand work unimpeded,these choices will be made according to the set of interests that are expressed by commerce on the Net. In some cases,
certainly, those interests will be constrained by government. But now we must think
specifically about how we could structure the choices we will confront and how we
could resolve the conflicts of values these spaces will present.

8 4

Our choices in each case are two. We can try to make cyberspace the same as real
space, investing it with the same values, or we can g ive cyberspace values and properties that are fundamentally different.

There is no general answer as to which choice we should make. But if we decide
we should preserve values from real space, we need a way to think about how. And
if we decide we should change values from real space,then change them to what?

The next ch a pter is abo ut how we might con s ti tute va lues differen t ly. It is
grounded in a broader sense of this idea of "regulation." Using this broader sense, we
will see what control might be possible. And in chapter 8, we will see some of the
limits on that control.

Both ch a pters are abo ut how we might exercise ch oi ce . This ch a pter has been
about the differences in cyberspaces that these choices make. In part 3, we will consider which differences we should want and which we should avoid. We will,in other
words, practice this choice.

S E V E N

w h a t t h i n g s r e g u l a t e

Joh n St uar t Mil l was an Engl ish man, t h ough one of t h e most influential ial
po l i tical ph i l o s oph ers in Am erica in the nineteenth cen tu ry. His wri ti n gs ra n ged
from imp ortant work on logic to a still striking text, The Subjection of Women. But
his continuing influence comes from a relatively short book titled On Liberty. Publ i s h ed in 1859, this powerful argument for indivi dual liberty and divers i ty of
thought represents an important view of liberal and libertarian thinking in the second half of the nineteenth century.

" L i bert a ri a n ," h owever, has a specific meaning for us. It assoc i a tes with argum ents against govern m en t .1 G overn m en t , in the modern libert a ri a n's vi ew, is the
threat to liberty; private action is not. Thus, the good libertarian is focused on reducing government's power. Curb the excesses of government, the libertarian says,
and you will have ensured freedom for your society.

Mi ll 's vi ew was not so narrow. He was a defen der of l i berty and an oppon ent of
forces that su ppre s s ed it. But those forces were not con fin ed to govern m en t .L i berty, i n
Mi ll 's vi ew, was thre a ten ed as mu ch by norms as by govern m en t , as mu ch by sti gm a
and into l era n ce as by the threat of s t a te punishmen t . His obj ective was to argue aga i n s t
these priva te forces of coercion i on . His work was a defense against liberty - su ppre s s i n g
n orm s , because in England at the time these were the real threat to liberty.

Mill's method is important, and it should be our own. It asks, What is the threat
to liberty, and how can we resist it? It is not limited to asking, What is the threat to
l i berty f rom govern m en t ? It understands that more than govern m ent can thre a ten
liberty, and that sometimes this something more can be private rather than state action. Mill was not so concerned with the source. His concern was with liberty.

Th threats to liberty ch a n ge . In England norms may have been the probl em in the late
n i n nineteenth cen tu ry; in the Un i ted States in the first two dec ades of the twen ti eth centu ry it was state su ppre s s i on of s peech .2 The labor movem ent was fo u n ded on the ide a
that the market is som etimes a threat to liberty—not just because of l ow wage s , but

8 6

also because the market form of or ga n i z a ti on itsel f d i s a bles a certain kind of f reedom .3
In other soc i eti e s , at other ti m e s , the market is the key, not the en emy, to liberty.

Thus, rather than think of an enemy in the abstract, we should understand the
particular threat to liberty that exists in a particular time and place. And this is especially true when we think about liberty in cyberspace. For my argument is that cyberspace teaches a new threat to liberty. Not new in the sense that no theorist has
conceived of it before. Others have.4 But new in the sense of newly urgent. We are
coming to understand a newly powerful regulator in cyberspace, and we don't yet
understand how best to control it.

This regulator is code—or more generally, the "built environment" of social life,
its architecture.5 And if in the middle of the nineteenth century it was norms that
threatened liberty, and at the start of the twentieth state power that threatened liberty, and during much of the middle twentieth the market that threatened liberty,
my argument is that we understand how in the late twentieth century, and into the
twenty-first, it is a different regulator—code—that should be our concern.

But it is not my aim to say that this should be our new single focus. My argument
is not that there is a new single enemy different from the old. Instead, I believe we
need a more g eneral understanding of how regulation works. One that focuses on
more than the single influence of any one force such as government, norms, or the
market, and instead integrates these factors into a single account.

This chapter is a step toward that more general understanding.6 It is an invitation to think beyond the narrow threat of government. The threats to liberty have
n ever come solely from govern m en t , and the threats to liberty in cybers p ace certainly will not.

A D O T ' S L I F E

There are many ways to think about constitutional law and the limits it may impose
on government regulation.I want to think about it from the perspective of someone
who is regulated or constrained. That someone regulated is represented by this (pathetic) dot—a creature (you or me) subject to the different constraints that might
regulate it. By describing the various constraints that might bear on this individual,
I hope to show you something about how these constraints function together.

Here then is the dot.

8 7

How is this dot "regulated"?
Let's start with something easy: smoking. If you want to smoke, what constraints

do you face? What factors regulate your decision to smoke or not?

One constraint is legal. In some places at least,laws regulate smoking—if you are
under eighteen, the law says that cigarettes cannot be sold to you. If you are under
twenty-six, cigarettes cannot be sold to you unless the seller checks your ID. Laws
also regulate where smoking is permitted—not in O'Hare Airport, on an airplane,
or in an elevator, for instance. In these two ways at least, laws aim to direct smoking
beh avi or. Th ey opera te as a kind of con s traint on an indivi dual who wants to
smoke.7

But laws are not the most significant con s traints on smoking. Sm o kers in the
United States certainly feel their freedom regulated, even if only rarely by the law.
There are no smoking police, and smoking courts are still quite rare. Rather, smokers in America are regulated by norms. Norms say that one doesn't light a cigarette
in a private car without first asking permission of the other passengers. They also
say, however, that one needn't ask permission to smoke at a picnic. Norms say that
others can ask you to stop smoking at a restaurant, or that you never smoke during
a meal.

European norms are savagely different. There the presumption is in the smoker's
favor; vis-à-vis the smoker, the norms are laissez-faire. But in the States the norms
effect a certain constraint, and this constraint, we can say, regulates smoking behavior.

L aw and norms are sti ll not the on ly forces reg u l a ting smoking beh avi or. Th e
market too is a constraint. The price of cigarettes is a constraint on your ability to
smoke. Change the price, and you change this constraint. Likewise with quality. If
the market supplies a variety of cigarettes of widely varying quality and price, your
ability to select the kind of cigarette you want increases; increasing choice here reduces constraint.

Finally, there are the constraints created, we might say, by the technology of cigarettes, or by the technologies affecting their supply.8 Unfiltered cigarettes present a
greater constraint on smoking than filtered cigarettes if you are worried about your
health. Nicotine-treated cigarettes are addictive and therefore create a greater constraint on smoking than untreated cigarettes. Smokeless cigarettes present less of a
constraint because they can be smoked in more places. Cigarettes with a strong odor
present more of a constraint because they can be smoked in fewer places. In all of
these ways, how the cigarette is affects the constraints faced by a smoker. How it is,
how it is designed,how it is built—in a word, its architecture.

Thus, four constraints regulate this pathetic dot—the law, social norms,the market, and architecture—and the "regulation" of this dot is the sum of these four constraints. Changes in any one will affect the regulation of the whole. Some constraints
will support others; some may undermine others.A complete view, however, should
consider them together.

8 8

So think of the four together like this:

In this drawing, each oval represents one kind of constraint operating on our pathetic dot in the center. Each constraint imposes a different kind of cost on the dot
for engaging in the relevant behavior—in this case, smoking. The cost from norms
is different from the market cost, which is different from the cost from law and the
cost from the (cancerous) architecture of cigarettes.

The con s traints are disti n ct , yet they are plainly interdepen den t .E ach can su pport or oppose the others . Tech n o l ogies can undermine norms and laws ; t h ey can
also su pport them . Some con s traints make others po s s i bl e ; o t h ers make some impo s s i bl e . Con s traints work toget h er, t h o u gh they functi on differen t ly and the effect of e ach is disti n ct . Norms con s train thro u gh the sti gma that a com mu n i ty
i m po s e s ; m a rkets con s train thro u gh the pri ce that they ex act ; a rch i tectu res cons train thro u gh the physical bu rdens they impo s e ; and law con s trains thro u gh the
p u n i s h m ent it thre a ten s .

We can call each constraint a "regulator," and we can think of each as a distinct
m od a l i ty of reg u l a ti on . E ach mod a l i ty has a com p l ex natu re , and the interacti on
a m ong these four is hard to de s c ri be . I 've worked thro u gh this com p l ex i ty more
completely in the appendix. But for now, it is enough to see that they are linked and
that,in a sense,they combine to produce the regulation to which our pathetic dot is
subject in any given area.

The same model describes the regulation of behavior in cyberspace.

8 9

L aw reg u l a tes beh avi or in cybers p ace . Copyri ght law, def a m a ti on law, and obscenity laws all continue to threaten ex post sanction for the violation of legal rights.
How well law regulates, or how efficiently, is a different question: in some cases it
does so more efficiently, in some cases less. But whether better or not,law continues
to thre a ten a certain con s equ en ce if it is def i ed . Legi s l a tu res en act ;9 pro s ec prosecutors
threaten;10 courts convict.11

Norms also reg u l a te beh avi or in cybers p ace . Talk abo ut dem oc ra tic po l i tics in
the alt.knitting newsgroup u p, and you open yo u rs el f to flaming; "s poof " s om eon e's
identity in a MUD, and you may find yourself "toaded";12 talk too much in a discussion list, and you are likely to be placed on a common bozo filter. In each case, a
set of understandings constrain behavior, again through the threat of ex post sanctions imposed by a community.

Markets regulate behavior in cyberspace. Pricing structures constrain access, and
if they do not, busy signals do. (AOL learned this quite dramatically when it shifted
f rom an hourly to a flat ra te pricing plan.)1 3 Areas of the Web are beginning to
charge for access, as online services have for some time. Advertisers reward popular
sites; online services drop low-population forums. These behaviors are all a function
of market constraints and market opportunity. They are all,in this sense, regulations
of the market.

And fin a lly, an analog for arch i tectu re reg u l a tes beh avi or in cybers p ace —cod e . Th e
s of t w a re and hardw a re that make cybers p ace what it is con s ti tute a set of con s tra i n t s
on how you can beh ave . The su b s t a n ce of these con s traints may va ry, but they are experi en ced as con d i ti ons on your access to cybers p ace . In some places (online servi ce s
su ch as AO L , for instance) you must en ter a password before you gain acce s s ; in other
p l aces you can en ter wh et h er iden ti fied or not.1 4 In some places the tra n s acti ons yo u
en ga ge in produ ce traces that link the tra n s acti ons (the "mouse dropp i n gs") back to
yo u ; in other places this link is ach i eved on ly if you want it to be .1 5 In some places yo u
can ch oose to speak a language that on ly the rec i p i ent can hear (thro u gh en c rypti on ) ;1 6 in other places en c rypti on is not an opti on .1 7 The code or sof t w a re or arch architecture re or pro tocols set these fe a tu re s ; t h ey are fe a tu res sel ected by code wri ters ; t h ey
con s train some beh avi or by making other beh avi or po s s i bl e , or impo s s i bl e . The code
em beds certain va lues or makes certain va lues impo s s i bl e . In this sen s e , it too is reg ul a ti on , just as the arch i tectu res of re a l - s p ace codes are reg u l a ti on s .

As in real space ,t h en , these four mod a l i ties reg u l a te cybers p ace . The same balance

ex i s t s . As Wi lliam Mi tch ell puts it (though he omits the con s traint of the market ) :

Arch i tectu re , l aws , and customs maintain and repre s ent wh a tever balance has
been struck [in real space]. As we construct and inhabit cyberspace communities,
we wi ll have to make and maintain similar bargain i n s — t h o u gh they wi ll be embodied in software structures and electronic access controls rather than in architectural arrangements.18

9 0

L aws , n orm s , the market , and arch i tectu res interact to build the envi ron m en t

that "Netizens" know. The code writer, as Ethan Katsh puts it, is the "architect."19

But how can we "m a ke and maintain" this balance bet ween mod a l i ties? Wh a t
tools do we have to ach i eve a different con s tru cti on? How might the mix of re a l -
s p ace va lues be carri ed over to the world of c ybers p ace? How might the mix be
changed if change is desired?

O N G O V E R N M E N T S A N D W A Y S

T O R E G U L A T E

I've described four constraints that I've said "regulate" an individual. But these separate constraints obviously don't simply exist as g ivens in a social life. They are neither found in nature nor fixed by God.Each can be changed,though the mechanics
of changing each is complex. Law can have a significant role in this mechanics, and
my aim in this section is to describe that role.

A simple example will suggest the more general point. Say the theft of car radios
is a problem—not big in the scale of things, but a frequent and costly enough problem to make more regulation seem necessary. One response might be to increase the
penalty for car radio theft until the risk faced by thieves made it such that this crime
did not pay. Life in prison for radio theft. If radio thieves realized that they exposed
t h em s elves to a lifetime in pri s on each time they stole a rad i o, it might no lon ger
m a ke sense to them to steal rad i o s . The con s traint con s ti tuted by the thre a ten ed
punishment of law would now be enough to stop the behavior we are trying to stop.
But changing the law is not the only possible technique. A se cond might be to
change the radio's architecture. Imagine that radio manufacturers program radios to
work only with a single car—a security code that electronically locks the radio to the
car, such that if the radio is removed,it will no longer work. This is a code constraint
on the theft of radios; it makes the radio no longer effective once stolen. It too functions as a constraint on the r adio's theft, and like the threatened punishment of life
in prison, it could be effective in stopping the radio-stealing behavior.

Thus, the same constraint can be achieved through different means, and the different means are differently costly. The threatened punishment of life in prison may
be fiscally more costly than the change in the architecture of radios (depending on
how many people actually continue to steal radios,and how many are caught). From
this fiscal perspective, it may be more efficient to change code than law. Fiscal efficiency may also align with the expressive content of law—a punishment so extreme
would be barbaric for a crime so slight. Thus, the values may well track the efficient
response. Code would be the best means to regulate.

The costs,however, need not align so well, in this example or in others. Take the
Supreme Court's hypothetical example of life in prison for a parking ticket.20 It is
likely that whatever code c onstraint might match this law constraint, the law constraint would be more efficient (if reducing parking violations were the only aim).

9 1

There would be very few victims of this law before people conformed their behavior
appropriately. But the "efficient result" would conflict with other values. If it is barbaric to incarcerate for life for the theft of a radio, it is all the more so as a penalty
for a parking violation. The regulator has a range of means to effect the desired cons tra i n t , but the va lues that these means entail need not align with their ef fic i en c y.
The efficient answ er may well be unjust—that is, it may conflict with values inherent in the norms, or law (constitution), of the society.

Law-talk typically ignores these other regulators. It typically ignores how law can
affect their regulation. Many speak as if law must simply take the other three constraints as given and fashion itself to them.21

I say "as if " because today it takes only a second's thought to see that this narrowness is absu rd . Th ere were times wh en these other con s traints were tre a ted as
fixed—when the constraints of norms were said to be immovable by governmental
acti on ,2 2 or the market was thought to be essen ti a lly unreg u l a bl e ,2 3 or the cost of
changing real-space code was so high as to make the thought of using it for regulation absurd. 24 But we see now that these constraints are plastic.25 That they are, as
law is, changeable, and subject to regulation.

The examples are obvious and many. Think first about the market: talk of a "free
market" notwithstanding, there is no more heavily regulated aspect of our life.26 The
market is regulated by law not just in its elements—it is law that enforces contracts,
e s t a establishes property, and reg u l a tes curren c y — but also in its ef fect s . The law uses
t a xes to increase the market's con s traint on certain beh avi ors and subsidies to reduce its constraint on other behaviors. We tax cigarettes in part to reduce their consu m pti on , but we su b s i d i ze tob acco produ cti on to increase its su pp ly. We tax
alcohol to reduce its consumption. We subsidize child care to reduce the constraint
the market puts on raising children. In many such ways the constraint of law is used
to change the constraints of the market.

Law can also change the regulation of architecture. Think about the Americans
with Di s a bi l i ties Act (ADA ) .2 7 Ma ny of the "d i s a bl ed " a re cut of f f rom access to
much of the world. A building with only stairs is a building that is inaccessible to a
person in a wheelchair. The stairs are a constraint on the disabled person's access to
that bu i l d i n g. But the A DA in part aims to ch a n ge that con s traint by requ i ri n g
bu i l ders to ch a n ge the de s i gn of bu i l d i n gs so that the disabl ed are not exclu ded .
Here is a reg u l a ti on of re a l - s p ace code , by law, to ch a n ge the con s traint that re a l -
space code creates.

Other examples get even better.

•

Some of the power of the French Revolution derived from the architecture of
Pa ri s : the city 's small and winding streets were easily barri c barriaded , making it
possible for revolutionaries to take control of the city with relatively little abs o lute stren g t h . Louis Na po l eon III unders tood this, and in 1853 he too k
steps to change it.28 Paris was rebuilt, with wide boulevards and multiple passages, making it impossible for insurgents to take control of the city.

9 2

• Every schoolchild learns of Lafayette's design to make an invasion of Washington n g ton difficult. But more intere s ting is the placem ent of the Wh i te Ho u s e
relative to the Capitol.The distance between them is one mile,and at the time
it was a mile through difficult terrain. (The mall was a swamp.) The distance
was a barrier meant to tilt the intercourse between Congress and the president by making it margi n a lly more difficult for them to con n ect — a n d
thereby more difficult for the executive to control the legislature.

• This same idea has influ en ced the placem ent of con s ti tuti onal co u rts in Europe . Th ro u gh o ut Eu rope con s ti tuti onal co u rts were placed in cities other than
the capital. In Germ a ny the co u rt is in Ka rl s ruhe ra t h er than Berl i n ; in the
Czech Rep u blic it is in Brno ra t h er than Pra g u e . The re a s on again is ti ed to the
con s traint of geogra phy: p l acing con s ti tuti onal co u rts far aw ay from legi s l atu res and exec executives was meant to minimize both the pre s su re the latter two
bodies could place on the co u rt and redu ce the co u court's tem pt a ti on to bow to it.
• The principle is not limited to high politics. Designers of parking garages or
streets where children may play place speed bumps in the road so that drivers
must slow down. These structures have the same purpose as a speed limit or
a norm against driving too fast. But they operate by modifying architecture so
that architecture regulates.

• Nei t h er is the principle limited to vi rtuous reg u l a ti on : Robert Moses bu i l t
bri d ges on Long Island to bl ock bu s e s , so that Af rican Am eri c a n s , who depen ded pri m a ri ly on public tra n s port a ti on , could not easily get to publ i c
beaches.29 That was regulation through architecture,invidious yet familiar.
• Nor is it limited to governments.A major American airline noticed that pass en gers on early Mon d ay morning flights were fru s tra ted with the time it
took to retrieve eve bags from the plane. Th ey were mu ch more annoyed than
other passengers, even though it took no longer than average to retrieve the
bags from these flights. The company began parking these flights at gates farther away from baggage claim, so that by the time the passengers arrived at
baggage claim, their bags were there. Frustration with the baggage handling
system was eliminated.

• A large hotel in an American city received many complaints about the slowness of its elevators. It installed mirrors next to the elevator doors. The complaints ended.

In each example, a constraint of architecture is changed so as to realize a collective or social end. As a sign above one of the portals at the 1933 Chicago World's Fair
put it (though it was speaking of science): "Science Explores: Technology Executes:
Man Conforms."30

L aw can ch a n ge social norms as well , t h o u gh mu ch of our con s ti tuti onal jurisprudence seems dedicated to forgetting just how.31 Education is the most obvious
example. As Thurgood Marshall put it, "Education is not the teaching of the three
R's.Education is the teaching of the overall citizenship, to learn to live together with

9 3

fellow citizens,and above all to learn to obey the law."32 Education is,in part at least,
a process through which we indoctrinate children into certain norms of behavior—
we teach them how to "say no" to sex and drugs. We try to build within them a sense
of what is correct. This sense then regulates them to the law's end.

Plainly, the content of much of this education is regulated by law. Conservatives
worry, for example,that by teaching sex education we change the norm of sexual abstinence. Whether that is correct or not,the law is certainly being used to change the
norms of children. If conservatives are correct, the law is eliminating abstinence. If
l i berals are correct , the law is being used to insti ll a norm of s a fe sex . Ei t h er way,
norms have their own constraint, and law is aiming to change that constraint.

To say that law plays a role is not to say that it always plays a posit ive role. The
law can muck up norms as well as improve them, and I do not claim that the latter
result is more common than the former.33 The point is just to see the role, not to
praise or criticize it. The aim is descriptive; the normative comes later.

In each case, the law chooses between direct and indirect regulation. The questi on is: Wh i ch means best adva n ces the reg u l a tor 's goa l , su bj ect to the con s tra i n t s
(whether normative or material) that the regulator must recognize? We can represent the point through a modification of the second figure:

The point should be familiar, and the examples can be multiplied.

S e a tbel t s : The govern m ent may want citi zens to wear seatbelts more of ten .3 4 It
could pass a law to requ i re the we a ring of s e a seatbelts (law reg u l a ting beh avi or di-

9 4

rectly).Or it could fund public e ducation campaigns to create a stigma against those
who do not wear seatbelts (law regulating social norms as a means to regulating behavior). Or it could subsidize insurance companies to offer reduced rates to seatbelt
wearers (law regulating the market as a way of regulating behavior). Finally, the law
could mandate automatic seatbelts, or ignition-locking systems (changing the code
of the automobile as a means of regulating belting behavior). Each action might be
said to have some effect on seatbelt use; each has some cost. The question for the
government is how to get the most seatbelt use for the least cost.

Di discrimination m i n a tion against the disabl ed: The disabl ed bear the bu rden of s i gn i ficant social and physical barri ers in daily life .3 5 The govern m ent might dec i de to do som et h i n g
a bo ut those barri ers . The trad i ti onal answer is law reg u l a ting beh avi or direct ly: a law
b a rring discri m i n a ti on on the basis of physical disability l i ty. But the law could do more .
It co u l d , for ex a m p l e , edu c a te ch i l d ren so as to ch a n ge social norms (reg u l a ting norm s
to reg u l a te beh avi or ) . It could su b s i d i ze companies to hire the disabl ed (reg u l a ting the
m a rket to reg u l a te beh avi or ) . It could reg u l a te building codes to make bu i l d i n gs more
acce s s i ble to the disabl ed (reg u l a ting "n a tu ra l " or re a l - s p ace codes to reg u l a te beh avi or ) . E ach of these reg u l a ti ons would have some ef fect on discri m i n a ti on and wo u l d
h ave a co s t . The govern m ent would have to wei gh the costs against the ben efits and sel ect the mode that reg u l a tes most ef fectively.

Dru gs : The govern m ent is ob s e s s ed with reducing the con su m pti on of i ll i c i t
drugs. Its main strategy has been direct regulation of behavior through the threat of
barbaric p rison terms for violation of the drug laws. This policy has obvious costs
and non-obvious benefits. But most interesting for our pur poses are the non-obvious costs. As Tracey Meares persuasively argues, one effective structure for regulating the con su m pti on of i ll egal dru gs is the social stru ctu re of the com mu n i ty in
which an individual lives.36 These are what I've called social norm constraints: standards of appropriate behavior enforced by the sanctions of a community—whether
through shame, exclusion, or force.

Just as government can act to strengthen these social norm constraints,it should
be obvious that government can also act to weaken them.37 One way to do this is by
weakening the communities within which these norms operate. This,says Meares,is
what the extreme sanctions of the criminal law do.38 In their extremity and effect,
they undermine the social structures that would support this social policy. This is an
indirect effect of the direct regulation of law, and at some point this effect may overwhelm the effect of the law. We might call this the Laffer Curve for criminal law.

The net effect of these different constraints cannot be deduced a priori. The government acts in many ways to regulate the consumption of drugs. It supports extensive public education campaigns to stigmatize the consumption of drugs (regulating
social norms to regulate behavior). It seizes drugs at the border, thereby reducing the
supply, increasing the price,and presumably reducing demand (regulating the market to regulate behavior). And at times it has even (and grotesquely) regulated the
"code" of drugs (by, for example, spraying marijuana fields with paraquat), making

9 5

t h em more dangerous and thereby increasing the con s traint on their consumption.39
All of these together influence the consumption of drugs. But as advocates of legalization argue, they also influence the incidence of other criminal behavior as well.
The policy maker must assess the net ef fect — wh et h er on the whole these reg u l ations reduce or increase social costs.

Ab o rti o n : One final example wi ll com p l ete the acco u n t . Si n ce Roe v Wa d e , t h e
Co u rt has recogn i zed a wom a n's con s ti tuti onal ri ght to an aborti on .4 0 This ri gh t ,
however, has not stopped government from seeking to eliminate or reduce the number of abortions. Again, the government need not rely on direct regulation of abortion (which under Roe would be unconstitutional). It can instead use indirect means
to the same end. In Rust v Sullivan, the Court upheld the power of the government
to bias the provi s i on of f a m i ly planning advi ce by forbidding doctors in "government-funded" clinics from mentioning abortion as a method of family planning.41
This is a regulation of social norms (within the social structure of medical care) to
regulate behavior. In Maher v Roe, the Court upheld the right of the government selectively to disable medical funding for abortion.42 This is the use of the market to
regulate b ehavior. And in Hodgson v Minnesota, the Court upheld the right of the
state to force minor women to wait forty-eight hours before getting an abortion.43
This is the use of real-space code (the constraints of time) to regulate access to abortion. In all these ways, Roe notwithstanding, the government can regulate the behavior of women wanting abortions.

In each of these examples, law functions in two very different ways.44 When its operation is direct,it tells individuals how to behave and threatens punishment if they
deviate from that behavior. When its operation is indirect, it aims at modifying one
of the other structures of constraint.45 The regulator selects from among these various techniques according to the return from each—both in efficiency and in the values that each might express.

When we see regulation in this more general way, we can see more clearly how
the unregulability of cyberspace is contingent. We get a stronger sense of how the
state could intervene to make regulation work. And we should also get a sense of the
increased dangers presented by this more expansive sense of regulation. In particular, we should have a stronger sense of the danger it presents to constitutional values. The next section considers one such threat.

T H E P R O B L E M S O F I N D I R E C T I O N

In 1985, a f ter ye a rs of i n acti on , Con gress passed the Low Level Rad i oactive Wa s te
Policy Am en d m ents Act to deal with the probl em of nu clear waste .4 6 Som eon e
needed to take and store nuclear waste. After sufficient prodding by the government,
a number of states formed a compact, which Congress then ratified, implementing

9 6

a number of requirements and incentives for states to deal with the nuclear waste
they produce.

The details of the overall plan are not important here. It is enough to focus on
just one part . To indu ce states to fo ll ow federal guidelines for reg u l a ting nu cl e a r
waste, Congress gave them a choice: either enact certain regulations or "take title" to
the spent nuclear fuel. This was a "your money or your life" regulation, for the fuel
to which the states would take title was not an asset but a great liability. In a very
heavy-handed way, Congress was essentially forcing states to pass the regulations it
wanted.

The Supreme Court struck down this part of the law. In effect, the Court held,
Con gress was com m a n deering the state legi s l a tu res to en act Con gre s s's law. Congress itself, of course, had the power to enact those regulations directly. But it did
not have the power to order states to enact laws. Indirection here was not allowed.

This case—New York v United States—does not stand for the broad principle that
government must regulate only directly, or even for the principle that indirect regulation generally is disfavored. The case was focused quite narrowly on the question
of indirection as it involved the states. The most New York stands for is the idea that
states, as independent sovereigns deserving of special constitutional respect, cannot
be co - opted to the federal govern m en t's ends—that wh en the federal govern m en t
has a program it wants to car ry out, it must put its own name behind it.

But while New Yo rk doe s n't establish a gen eral con s ti tuti onal pri n c i p l e , it doe s
suggest why indirection should be a more general concern. And this general concern
is my focus here.

Indirection misdirects responsibility. When a government uses other structures
of constraint to effect a constraint it could impose directly, it muddies the responsibility for that constraint and so undermines political accountability. If transparency
is a value in constitutional government,indirection is its enemy. It confuses responsibility and hence confuses politics.

Su ch misunderstandings n ders t a n d i n gs are po s s i ble in other con texts as well . Think aga i n
about the case of Rust. The federal government helps to fund family planning clinics. ("Helps" fund, not completely funds.)47 Before 1988 these clinics gave advice on
a wide range of birth-related topics, including abortion. Doctors in family planning
clinics would advise their pati ents abo ut aborti on wh en ever they felt su ch advi ce
was proper.

The Re a gan ad m i n i s tra ti on wanted to ch a n ge that. So it ordered (the details of
h ow are not important here) doctors in those clinics to not discuss aborti on as a
m et h od of f a m i ly planning with their pati en t s . If a s ked , the doctors were to say,
"The proj ect does not con s i der aborti on an appropri a te met h od of f a m i ly planning i n g."4 8

The aim of this regulation was clear: to reduce the incidence of abortion. It did
this by using doctors to steer patients away from abortion.A doctor has a great deal
of power over a patient in a context like this; the patient would most likely understand the doctor to be recommending against abortion.

9 7

But notice the technique. The federal government could have stated its own position about abortion. It could have put up posters and billboards saying that abortion is wrong, or it could have used space in its clinics to advertise its view. But it
chose instead to bury its policy choice in the words of doctors. It thereby could trade
on the professional authority of the doctors to advance its own ends. It could regulate abortion indirectly by regulating the doctors directly.

Just as it tried to use the authority of the states to effect its ends in New York, the
government trades on a misrepresentation in Rust. But worse than in the federalism
context, the victim of the misrepresentation here does not even realize that the misrepresentation is a policy choice. The patient is unlikely to hear the doctor's statement as political broadcast from the government. She is most likely to hear it as a
m edical op i n i on . Not on ly is there a con f u s i on abo ut who is re s pon s i ble for the
opinion expressed, but there is also confusion about whether it is an opinion at all.
Rust v Su ll iva n is one of the great em b a rra s s m ents of the Su preme Co u rt ; t h e
case proving Ju s ti ce Scalia's rule that any issue gets distorted on ce it gets near the
question of abortion.49 But my argument here doesn't depend up on whether Rust
was right. My aim is to bring out a certain sensibility about regulation; Rust simply
points the way.

Consider a third case. Until 1948 deeds could include covenants (promises) that
the property covered by the deed could not be sold to people of a particular r ace.
The purpose of these provisions was clear: to effect and preserve segregation. Their
use was ex ten s ive . It was esti m a ted , for ex a m p l e , that wh en Sh ell ey v Kra em er5 0
struck these provisions down as unconstitutional under the equal protection clause,
25 percent of the properties in south Ch i c a go had been pro h i bi ted from sale to
African Americans.51

As awful as such provisions were, they had a certain integrity. They clearly stated
t h eir purpose and were tra n s p a rent abo ut the va lues they affirm ed . No one co u l d
pretend that the segregation they effected was somehow an accidental by-product of
decisions made elsewhere. Although they were private covenants,they were enforced
by the state and, indeed, derived their meaning from the state. They said: this society is racist.

Wh en the Co u rt stru ck these provi s i ons down , h owever, the qu e s ti on bec a m e
what would rep l ace them . Few ex pected that the atti tu des behind these coven a n t s
would suddenly disappear because of a single court judgment. So when the Court
ended direct segregation, we should have expected indirect segregation to emerge to
replace it.

Sure enough,after 1948 local communities shifted their technique for preserving
segregation. Rather than covenants, they used architecture. Communities were designed to "break the flow" of residents from one to another. Highways without easy
crossings were placed between communities. Railroad tracks were used to divide. A
thousand tiny inconveniences of architecture and zoning replaced the express preferen ces of coven a n t s . Nothing form a lly pro h i bi ted integra ti on . But inform a lly,
much did.52

9 8

Local governments thus did something very much like what the federal government did in Rust and tried to do in New York: no longer able to effect segregation direct ly, t h ey used zoning laws — geogra phical arch i tectu re , or re a l - s p ace code — to
effect it indirectly. They built their communities and designed their streets to make
it hard for integration to occur. The tiny inconveniences of zoning regulations succeeded in keeping communities separate.

What is most significant is that now, even more than with Rust, it becomes very
difficult to see the link between the regulation and its consequence. The continuing
segregation of these communities is described as the product of "choice." Individuals choose to live in one neighborhood rather than another. In a strict sense, that is
correct, but their choices are made in the face of costs that the state has imposed. It
is easier to remain segregated, so people choose to do that. But it is only easier because government has moved mountains to make it that way.

Here the govern m ent is reg u l a ting indirect ly, by using the stru ctu res of re a l -
space code to effect its ends, but this regulation,again,is not seen as regulation. Here
the government gets an effect at no political cost. It gets the benefit of what would
clearly be an illegal and controversial regulation, that is, without even having to admit any regulation exists.

In all three cases, the govern m ent is com m a n deering the power of a n o t h er
modality—another structure of constraint—to effect its own ends.53 This in itself is
not necessarily improper. There are plenty of examples that anyone would consider
proper. A requirement that streets be well lit, for instance,is a regulation designed to
reduce crime; it does so indirectly, by regulating the architecture of streets. No one
would think that regulation improper. Nor does all such regulation hide its pedigree.
Think again abo ut speed bu m p s . Th ey are examples of i n d i rect reg u l a ti on . L i ke a
winding road, they use the code of streets to keep down the speed of a car. But no
one is fooled about the source of this regulation; no one believes the bumps are a accidental.

Thus, the point is not against indirect regulation generally. The point is instead
a bo ut tra n s p a ren c y. The state has no ri ght to hide its agen d a . In a con s ti tuti on a l
democracy its regulations should be public. And thus, one issue raised by the practice of indirect regulation is the general issue of publicity. Should the state be permitted to use nontransparent means when transparent means are available?

W H E R E T H I S L E A D S

After I published an essay in The Industry Standard, arguing that "code is law,"54 the
following letter was sent to the editor:

Typical for a Ha rva rd Law Profe s s or. . . . Lessig misses the en ti re forest wh i l e
dancing among the tree s . . . . While his ri f f on West Coast Code (from Si l i con

9 9

Va ll ey Progra m m ers) vs . East Coast Code (from govern m ent law yers) is very
cleverly crafted, it completely avoids the real difference between the two.

The good professor seems to apply the word "regulation" equally to the efforts
of priva te en terprises to co n trol the beh avior of t h eir custo m ers t h rou gh market
mechanisms and the efforts of government agencies to control the behavior of all
citizens through force of law.

So long as the creators and purveyors of West Coast Code (no matter how selfish, monopolistic, demonic or incompetent they may be) do not carry guns and
badges,I will choose them over the enforcers of East Coast Code any time.55

Whether or not I've missed the "real difference" between code and law, the genius in this letter is that its author clearly sees the real similarity. The author (the
president of an Internet-related business) understands that "private enterprise" tries
to "control the behavior of their customers." He w rites of "market mechanisms" to
achieve that control. (Technically, I was speaking about architectures to achieve that
effect, but never mind. Whether markets or architectures,the point is the same.) He
t h erefore sees that there is "reg u l a ti on" beyond law. He just has his own favorites te s
(corporate executive that he is).

What this author sees is what we all must see to understand how cyberspace is
regulated, and to see how law might regulate cyberspace. I've argued in this chapter
that govern m ent has a ra n ge of tools that it uses to reg u l a te . Cybers p ace ex p a n d s
that range. The code of cyberspace is becoming just another tool of state regulation.
Indirectly, by regulating code writing, the government can achieve regulatory ends,
often without suffering the political consequences that the same ends, pursued directly, would yield.

We should worry about this. We should worry about a regime that makes invisible regulation easier; we should worry about a regime that makes it easier to regulate. We should worry about the first because invisibility makes it hard to resist bad
regulation; we should worry the second because we don't yet—as I argue in part 3—
have a sense of the values put at risk by the increasing scope of efficient regulation.
But the power that govern m ent has over cybers p ace hangs on an important fe atu re of c ybers p ace that I have not yet de s c ri bed . We can no lon ger take that fe a tu re for
gra n ted — ei t h er in this argument or in the worl d . One fe a tu re of the code determ i n e s
mu ch abo ut the power of govern m en t . It is the topic of the ch a pter that fo ll ows .

E I G H T

t h e l i m i t s i n o p e n c o d e

I've t ol d a st or y of h ow r egul at ion wor ks and of increasing easing r egul abil it y—
of changes in the architecture of the Net that will better enable government's contro l . These ch a n ge s , I have argued , wi ll em er ge even if govern m ent does nothing.
They are the by-product of changes made to enable e-commerce.

That was part 1. In this part ,I 've upped the stake s . My aim has been to give a deeper
account of the va lues built into a particular arch i tectu re of the Net , and thus a deeper
u n derstanding of the ways in wh i ch govern m ent might act to shape those va lu e s .

But now the story changes. I want to introduce a complication on this road to
reg u l a bi l i ty. While rel a tively new in In tern et ti m e , this com p l i c a ti on promises (or
threatens) to bring about an important change in the character of the Net and the
feasibility of regulating it.

This com p l i c a ti on is free sof t w a re , or open source sof t w a re or, m ore simply,
open code.1 Put too simply, everything I have said about the regulability of behavior in cyberspace—or more specifically, about government's ability to affect regulability l i ty in cybers p ace — c ru c i a lly depends on wh et h er the app l i c a ti on space of
cyberspace is dominated by open code. To the extent that it is, government's power
is decreased; to the extent that it remains dominated by closed code, government's
power is preserved.2 Open code, in other words, can be a check on state power.

This is a lot to convince you of in a single chapter—especially since the conclusion will seem to be an important reversal on much that I have argued so far. To see
the point, we must back up and understand a bit more about the nature of the code
space that government might regulate and the nature of the actors who might control that space.

T H E N E T

I 've spent lots of time talking abo ut the code of c ybers p ace . For those who know
something about code in cyberspace (and who are still with me here), what I've said

1 0 1

will have been quite frustrating. As they know (and though they doubt it,as I know),
there are many different kinds or layers of code on the Internet. When we talk about
regulating code, it matters deeply which code we are describing.

The Internet is defined by a set of protocols together referred to as TCP/IP. That
label refers to a large number of protocols that feed different "layers" of the network.
The standard model for describing layers of a network is the open systems interconnect ect (OSI) referen ce model . It de s c ri bes seven net work layers , e ach repre s en ting a
"f u n cti on perform ed wh en data is tra n s ferred bet ween coopera ting app l i c a ti on s
ac ro s s" the net work . But the TCP/IP su i te is not as well arti c u l a ted . According to
Craig Hunt,"most descriptions of TCP/IP define three to five functional levels in the
pro tocol arch i tectu re ," t h o u gh it is simplest to de s c ri be four functi onal layers in a
TCP/IP architecture.3 From the bottom o f the stack up, we can call these the data
link, network, transport, and application layers.4

Very few pro tocols opera te at the lowest layer—the data link layer — s i n ce that
handles local network interactions exclusively. More protocols exist at the next layer
up—the network layer, where the IP protocol is dominant. It routes data between
hosts and across network links, determining which path the data should take. At the
n ext layer up—the tra n s port layer — t wo different pro tocols dom i n a te , TCP and
UDP. These negotiate the flow of data between two network hosts. (The difference
between the two is reliability—UDP offers no reliability guarantee.)

These three layers are the essential plumbing of the Internet, hidden in the Net's

walls. (The faucets work at the next layer; be patient.)

The protocols together function as a kind of odd UPS. Data are passed from the
application to the transport layer. There the data are placed in a (virtual) box and a
( vi rtual) label is slapped on . That label ties the con tents of the box to parti c u l a r
processes. (This is the work of the TCP or UDP protocols.) That box is then passed
to the network layer, where the IP protocol puts the package into another package,
with its own label . This label inclu des the ori gi n a ti on and de s ti n a ti on ad d re s s e s .
That box then can be furt h er wra pped at the data link layer, depending on the
specifics of the local network (whether, for example, it is an Ethernet network).

The whole process is a bizarre packaging game: a new box is added at each layer,
and a label on each box de s c ri bes the process at that layer. At the other en d , t h e
p ack a ging process is revers ed : l i ke a Russian do ll , e ach pack a ge is open ed at the
proper layer, until at the end the machine recovers the initial application data.

On top of these three layers is the application layer of the Internet. Here protocols "pro l i fera te ."5 These inclu de the most familiar net work app l i c a ti on pro toco l s ,
such as FTP (file transfer protocol, a protocol for transferring files), SMTP (simple
mail tra n s port pro toco l , a pro tocol for tra n s ferring mail), and HTTP (hyper tex t
tra n s fer pro toco l , a pro tocol to publish and re ad hypertext doc u m ents ac ross the
Web). These are rules for how a client (your computer) will interact with a server
(where the data are), and the other way around.

These four layers of protocols, then, constitute "the Internet." Building on simple
bl ock s , the sys tem makes po s s i ble an ex tra ord i n a ry ra n ge of i n teracti on . It is per-

1 0 2

haps not qu i te as amazing as natu re—think of D NA — but it is built on the same
principle: keep the elements simple, and the compounds will astound. 6

Wh en I speak abo ut reg u l a ting the code , I do not mean that we reg u l a te the
TCP/IP protocols. (Though in principle, of course,they could be regulated,and others have suggested that they should be regulated.)7 Instead, I've had in mind a different part of the code of cyberspace—the part that TCP/IP connects. In the terms
of network theory, I've had the "ends" in mind.8 Not the code at its most basic level
of Internet exchange, but the applications (both in hardware and software) that use
or implement those protocols.

A different metaphor may help you see the difference. Tim Wu likens the Internet to the electric grid: TCP/IP is the architecture for that grid; programs then "plug
into" TCP/IP, or into the Internet. At the top layer, the protocol defines what the plug
looks like; lower down, it governs how power flows.9

This is a helpful picture. Just as a very large number of appliances can be plugged
into the electric grid, so too can a very large number of programs use the Internet.
Before doing so, this wide variety need only ag ree on a simple protocol of data exchange.

My focus is on the code that plugs into the Internet.I will call that code the "application space" of the Internet. This includes all the code that implements TCP/IP
pro tocols at the app l i c a ti on layer — brows ers , opera ting sys tem s , en c rypti on modules, Java, e-mail systems, whatever elements you want. This application space code
would be the target of regulation in the story of regulability that I have told so far.
The question in this chapter is: What is the character of that code that makes it susceptible to regulation?

A S H O R T H I S T O R Y O F C O D E

T H E N E T

In the begi n n i n g, of co u rs e , t h ere were very few app l i c a ti ons on the Net . The Net
was no more than a protocol for exchanging data,and the original programs simply
took advantage of this protocol. The file transfer protocol (FTP) was born early in
the Net's history;10 the electronic message protocol (SMTP) was born soon after. It
was not long before a pro tocol to display directories in a gra phical way (Gopher er )
was developed. And in 1991 the most famous of protocols—the hyper text transfer
pro tocol (HTTP) and hyper text markup language (HTML)—gave bi rth to the
World Wide Web.

Each protocol spawned many applications. Since no one had a monopoly on the
protocol,no one had a monopoly on its implementation. There were many FTP applications and many e-mail servers. There were even a large number of browsers.11
The protocols were open standards, gaining their blessing from the standards bodies such as the Internet Engineering Task Force (IETF) and W3C. Once a protocol
was specified, programmers could build programs that utilized it.

1 0 3

Mu ch of the sof t w a re implem en ting these pro tocols was "open ," at least initially—that is, the source code for the software was available along with the object
code .* This openness was re s pon s i ble for mu ch of the early Net's growt h . Ot h ers
could explore how a program was implemented and learn from that example how
better to implement the protocol in the future.

The World Wi de Web is the best example of this poi n t . Aga i n , the code that
m a kes a web page appear as it does is call ed the hyper text markup language , or
HTML.† With HTML, you can specify how a web page will appear, and to what it
will be linked.

The ori ginal HTML was propo s ed in 1991 by the CERN re s e a rch er Tim
Berners-Lee12 It was designed to make it easy to link documents at a research facility, but it quickly became obvious that documents on any machine on the Internet
could be linked . Bern ers - Lee and Ca i Calliau made both HTML and its com p a n i on
HTTP freely available for anyone to take.

And take them people did, at first slowly, but then at an extraordinary rate. People starting building web pages and linking them to others. HTML became one of
the fastest-growing computer languages in the history of computing.

Why? One imp ortant reason was that HTML was always "open." Even today, on
the two major browsers still in distribution, you can always reveal the "source" of a
web page and see what makes it tick. The source remains open: you can download
it, copy it,and improve it as you wish. Copyright law may protect the source code of
a web page, but in reality it protects it very imperfectly. HTML became as popular as
it did primarily because it was so easy to copy. Anyone, at any time, could look under the hood of an HTML document and learn how the author produced it.

Openness—not property or con tract but free code and acce s s — c re a ted the
boom that gave birth to the Internet that we now know. And it was this boom that
t h en attracted the atten ti on of com m erce . With all this activi ty, com m erce ri gh t ly
reasoned, surely there was money to be ma de.

Hi s tori c a lly the com m ercial model for producing sof t w a re has been differen t .1 3 Th o u gh the history began even as the open code movem ent con ti nu ed ,
com m ercial sof t w a re ven dors were not abo ut to produ ce "f ree" (as in open source )
s of t w a re . Com m ercial ven dors produ ced sof t w a re that was cl o s ed—that travel ed

*Source code is the code that programmers write. It is close to a natural language, but not quite a natural language.A program is written in source code, but to be run it must be converted into a language the
machine can read. Some source code is converted on the fly—BASIC, for example, is usually interpreted
by the c omputer as the computer runs a BASIC program. But most sour ce code—or the most powerful
source code—is "compiled" before it is run. The compiler converts the sour ce code into either assembly
code (which mavens can read) or object code (which only geniuses and machines can read). Object code
is machine-readable. It is an undifferentiated string of 0s and 1s that instructs the machine about the tasks
it is to perform. Programmers do not directly write object code, even if some are able to decipher it; programmers write source code. Object code speaks to the computer; source code speaks to humans and to
computers (compilers);assembly code speaks to mavens and computers.

†Hyper text is text that is linked to another location in the same document or in another document

located either on the Net or on the same c omputer.

1 0 4

wi t h o ut its source and was pro tected against mod i f i c a ti on both by the law and by
its own code .

By the second half of the 1990s—marked most famously by Mi c ro s of t's Wi ndows 95, which came bundled Internet-savvy—commercial software vendors began
producing "a pp l i c a ti on space" code . This code was incre a s i n gly con n ected to the
Net—it incre a s i n gly became code "on" the In tern et — but for the most part it rem a i n ed cl o s ed .1 4 And as we prep a re to we a t h er Y 2 K , most of the most sign i fic a n t
software on the market is closed code that has nonetheless found a way to connect
to the Net.

It is this balance that we need to track—the balance bet ween open and cl o s ed
code on the Net. Most of the application space that ordinary users now use is closed.
Th ere are many excepti on s : Ap ach e , s ti ll the nu m ber- one server on the In tern et
whether users realize it or not, and SENDMAIL, still the most widely used program
for forwarding mail, are both open code. But if we include within the application
space the operating systems that connect to the Net, application space code on the
Net is closed.

O P E N I N G C O D E

T H E N E T

But this balance is changing. From the beginning the trend to enclose code on the
Internet has bothered many—some because they believe closed code is less efficient
than open code, others b ecause they believe closed code interferes with important
values of the Internet.

Ri ch a rd Stallman is in the latter camp. In 1985 Stallman began the Free Sof tw a re Fo u n d a ti on , with the aim of f u fueling the growth of open and free sof t w a re on
the Net . A Mac Art hur Fell ow who gave up his career to commit himsel f to the
c a u s e , S t a Stallman has devo ted his life to "f ree" s of t w a re . In 1984, ye a rs before the Net
re a lly took of f , he began devel oping an open source opera ting sys tem .G N U* was to
be the basis of an open code world wh ere , f rom the opera ting sys tem on up, code
was open .

Despite its many admirers, GNU was a bit ahead of its time. In the world before
easy Internet access,it was hard to coordinate a major project, such as developing an
operating system. Early in the 1990s, after an injury had slowed Stallman's progress,
a different project, devoted to similar ideals, overtook GNU.

In 1991, an undergraduate at the University of Helsinki posted on the Internet
the kernel of an operating system. This undergraduate was Linus Torvalds; his kernel was the first step in producing Linux. He posted his kernel and invited the world
to help him turn it into an operating system—a free and open operating system that
would come with its source code bundled alongside.15

*GNU is a recursive acronym. The idea was to build an operating system that was not Unix. GNU

stands for "GNU's Not Unix." Cute,no?

1 0 5

People took up the challenge, and slowly, through the early 1990s,they built this
kernel into an operating system. They did it in part by marrying Linux to Stallman's
GNU (which is why it may be most accurate to call it GNU/Linux). But whatever its
genealogy, by 1998 it had become apparent to all that Linux was an important competi tor to the Mi c ro s oft opera ting sys tem . Mi c ro s oft may have imagi n ed in 1995
that by 2000 there would be no other server operating system available except Windows NT, but when 2000 came around, there was GNU/Linux.

G N U / L i nux is amazing in many ways . It is amazing first because it is theoreti c a lly
i m perfect but practi c a lly su peri or. L i nus Torvalds rej ected what com p uter scien ce to l d
him was the ideal opera ting sys tem de s i gn,1 6 and inste ad built an opera ting sys tem
that was de s i gn ed for a single proce s s or (an In tel 386) and not cro s s - p l a tform - comp a ti bl e . Its cre a tive devel opm en t , and the en er gy it inspired ,s l slowly tu rn ed GNU/Linu x
i n to an ex tra ord i n a ri ly powerful sys tem . As of this wri ti n g, it has been ported to many
d i f ferent chip platforms—it can run on the In tel ch i p, the PowerPC chip (used by App l e ) , and the Sun SPA RC ch i p s . Al t h o u gh initi a lly de s i gn ed to speak on ly one lang u a ge ,G N U / L i nux has become the lingua franca of open source opera ting sys tem s .

What makes a sys tem open source is a com m i tm ent among its devel opers to
keep its core code public—to keep the hood of the car unlocked. That commitment
is not just a wish. Stallman encoded it in a contract that sets the terms that control
the future use of much open source software. This is the Free Software Foundation's
gen eral public license (GPL), wh i ch requ i res that any code licen s ed with GPL (as
Linux is) keep its source free. GNU/Linux was developed by an extraordinary collection of hackers worldwide only because its code was open for others to work on.
Its code, in other words, sits in the commons.17 Anyone can take it and use it as
he wishes. Anyone can take it and come to understand how it works. The code of
GNU/Linux is like a research program whose results are always published for others
to see. Everything is public; anyone, without having to seek the permission of anyone else, may join the project.

Al t h o u gh the GNU/Linux proj ect is the most important el em ent in the futu re
of open code on the In tern et , it is not the on ly on e . An o t h er cri tical example is
Net s c a pe , wh i ch in 1998 ded i c a ted its code to the public by giving it over to a
com p a ny call ed Moz i ll a . Anyone can down l oad the Net s c a pe source code from
Moz i ll a ; a nyone can take it and improve it. With the backing of a com p a ny like
Net s c a pe and the su pport of companies like IBM for Linu x , it appe a rs qu i te certain that the near futu re of a pp l i c a ti on space code on the In tern et wi ll in important ways be open source .1 8

R E G U L A T I N G O P E N S O U R C E

So imagine a future in which a significant portion of the application space code is
open code. What would that mean for regulability? How would that affect the story
I've told of the increasing power of the state to order cyberspace?

1 0 6

In ch a pter 4, I sketch ed examples of govern m ent reg u l a ting code . But think

again about those examples: How does such regulation work?

Con s i der two. The govern m ent tells the tel eph one com p a ny som ething abo ut
how its networks are to be designed, and the government tells television manufacturers what kinds of chips TVs are to have. Why do these regulations work?

The answer in each case is obvious. The code is regulable only because the code
writers can be controlled. If the state tells the phone company to do something, the
phone company is not likely to resist. Resistance would bring punishment; punishment is expensive; phone companies, like all other companies, want to reduce their
cost of doing business. If the state's regulation is rational (that is, effective),it will set
the cost of disobeying the state above any possible benefit. If, in addition, the target
of regulation is within the reach of the state,and a rational actor, then the regulation
is likely to have its effect. CALEA's regulation of the network architecture for t telephones is an obvious example of this (see chapter 5).

An unmovable, and unmoving, target of regulation, then, is a good start to regu l a bi l i ty. And this statem ent has an intere s ting corollary ll a ry: reg u l a ble code is cl o s ed
code . Think again abo ut tel eph one net work s . Wh en the govern m ent indu ces the
telephone networks to modify their network software, users have no choice about
whether to adopt this modification or not. You pick up the phone, you get the dial
tone the phone company gives you. No one I know hacks the telephone company's
code to build a different network design. The same with the V-chip—I doubt that
many people would risk destroying their television by pulling out the chip, and I am
certain that no one re-burns the chip to build in a different filtering technology.

In both cases the government's regulation works because when the target of the

regulation complies, customers can do little but accept it.

Open code is different. We can see something of the difference in a story told by

Netscape's legal counsel, Peter Harter, about Netscape and the French.19

I've described SSL, Netscape's protocol for exchanging encrypted data;it permits
secure exchange between a browser and a server. The French were not happy with
the security that SSL gave. They wanted to be able to crack SSL transactions. So they
requested that Netscape modify SSL to enable their spying.

There are plenty of constraints on Netscape's ability to modify of SSL—not the
least of which being that Netscape has given SSL over to the public, in the form of a
public standard. But assume for a second that it had not.Assume Netscape really did
control the standards for SSL and in theory could modify the code to enable French
spying. Would that mean that Netscape could comply with the French demand?

No. Technically, it could comply by modifying the code of Netscape Communicator a tor and then po s ting a new module that en a bl ed hacking by a govern m en t . But
just because it posts su ch a module does not mean it wi ll be adopted . Si n ce
Net s c a Netscape's code is open code , u s ers take on ly what they want. Al t h o u gh Net s c a pe
could offer a feature that the French government wants,there is no reason to believe
that users would want this same feature. Another supplier would undoubtedly provide an SSL module without the alteration demanded by the French government.

1 0 7

The point is simple, but its implication profound. To the extent that code is open
code , the power of govern m ent is con s tra i n ed . G overn m ent can dem a n d , government can threaten, but when the target of its regulation is plastic, it cannot rely on
its target remaining as it wants.

Say you are a Soviet propagandist, and you want to get people to read lots of information about Papa Stalin. So you declare that every book published in the Soviet
Union must have a chapter devoted to Stalin. How likely is it that such books will actually affect what people read?

Books are open source sof t w a re : t h ey hide nothing; t h ey reveal their source —
they are their source! A user or adopter of a book always has the choice to read only
the chapters she wants. If it is a book on electronics, then the reader can certainly
choose not to read the chapter on Stalin. There is very little the state can do to modify the reader's power in this respect.

The same idea libera tes open source code . The govern m en t's rules are ru l e s
on ly to the ex tent that they impose re s tri cti ons that adopters would want. Th e
govern m ent may coord i n a te standards (like "d rive on the ri gh t" ) , but it cert a i n ly
cannot impose standards that con s train users in ways they do not want to be cons tra i n ed . This arch i tectu re , t h en , is an important ch eck on the govern m en t's reg ul a tory power. Open code means open con tro l — t h ere is con tro l , but the user is
aw a re of i t .

Closed code functions differently. With closed code, users cannot easily modify
the control that the code comes packaged with. Hackers and very sophisticated programmers may be able to do so, but most users would not know which parts were
required and which parts were not.Or more precisely, users would not be able to see
the parts required and the parts not required because the source code does not come
bu n dl ed with cl o s ed code . Cl o s ed code is the prop a ga n d i s t's best stra tegy—not a
separate chapter that the user can ignore, but a persistent and unrecognized influence that tilts the story in the direction the propagandist wants.

W H E R E T H I S L E A D S

My argument so far has taken a simple path. In answer to those who say that the Net
cannot be regulated, I've argued that whether it can be regulated depends on its architecture. Some architectures would be regulable,others would not.I have then argued that government could take a role in deciding whether an architecture would
be regulable or not. The government could take steps to transform an architecture
from unregulable to regulable.

The final step in this progression of regulability is a constraint that is only now
becoming sign i f i c a n t . G overn m en t's power to reg u l a te code , to make beh avi or
within the code regulable, depends in part on the character of the code. Open code
is less reg u l a ble than cl o s ed code ; to the ex tent that code becomes open , government's power is reduced.

1 0 8

This is not, obviously, an absolute claim. I am discussing relative, not absolute,
regulability. Even with open code, if the government threatens punishments that are
s severe en o u gh , it wi ll indu ce a certain com p l i a n ce . And even with open code , t h e
techniques of identity, tied to code that has been certified as compliant, will still give
government plenty of power. Thus, much of the argument from part 1 sur vives this
point about open code—if the world becomes certificate-rich, regulability still increases.*

But when designing an architecture for cyberspace, the margins matter. The values of a given space are not only the values of speech, autonomy, access, or privacy.
They may also be values of limited control. As John Perry Barlow puts it,they are the
values of a certain bug being programmed into the architecture of the Net—a bug
that inhibits the power of government to control the Net perfectly, even if it does not
disable that power entirely.

For som e , the obj ective is to build code that disables any po s s i ble govern m en t a l
con tro l . That is not my obj ective . I cert a i n ly bel i eve that govern m ent must be cons tra i n ed , and I en endorse the con s traints that open code impo s e s , but it is not my obj ective to disable govern m ent gen era lly. As I've argued alre ady, and as the next part make s
p l a i n , s ome va lues can be ach i eved on ly if govern m ent interven e s . G overn m ent has a
ro l e , even if not as su b s t a n tial a role as it would wi s h . We need to understand this ro l e ,
as well as how our va lues might be adva n ced in the con text of the Web.

One constraint seems clear in this account. As I argue more extensively later in
the book, even if open code does not disable government's power to regulate comp l etely, it cert a i n ly ch a n ges that power. On the margi n , open code redu ces the reward from burying regulation in the hidden spaces of code. It functions as a kind of
Freedom of In form a ti on Act for net work reg u l a ti on . As with ord i n a ry law, open
code requires that lawmaking be public, and thus that lawmaking be transparent. In
a sense that Geor ge Soros ought to unders t a n d , open code is a fo u n d a ti on to an
open society.

Even this is an important—some might say an essential—check on the power of
government. But whether or not one is for transparency generally, my aim so far is
just to map out the links. Regulability is conditional on the character of the code,
and open code changes that character. It is a limit on government's power to regulate—not necessarily defeating the power to regulate, but changing it. 20

*Another constraint would arise if more code were burned into hardware rather than existing as software. Then, even if the code were open,it would not be modifiable.I am grateful to Hal Abelson for this
point.

P A R T T H R E E

a p p l i c a t i o n s

Nature doesn't determine cyberspace. Code does. Code is not constant. It changes. It
is changing now in a way that will make cyberspace more regulable. It could change
in a way that makes cyberspace less regulable. How it changes depends on the code
writers. How code writers change it could depend on us.

If we do nothing, the code of c ybers p ace wi ll ch a n ge . The invi s i ble hand wi ll
change it in a predictable way. To do nothing is to embrace at least that. It is to accept the changes that this change in code will bring about. It is to accept a cyberspace
that is less free, or differently free, than the space it was before.

But then , h ow should the futu re devel op? What va lues should the space have ?
I've emphasized the need for choice but have done little to show what that choice
should be.

In this part , I practi ce that ch oi ce . I begin with a tech n i que that is familiar to
American constitutionalists in cases where constitutional law confronts changed circumstances. This technique, which I call translation, decides the present in terms of
the past. Its aim is to choose in a way that is faithful to the choices of the past, to
translate the commitments of the past into a fundamentally different context. Just as
a language translator constructs a text that is different from the source but has the
same meaning as the source, so too does the constitutional translator construct an
application that,though different from the original application,has the same meaning in the current context as the original did in its context.

Translation will guide in important cases. It will show us how we can go on, consistent with traditions we respect. But in the cases I focus on most extensively, trans-

1 1 0

lation alone will not be enough; the past will not resolve the future. The questions
raised by the future are issues that were not decided in the past.

These are the l a tent ambi g u i ti e s that I spo ke of at the start , i llu s tra ted wi t h
searches by worms. My argument in part 3 is that these cases of ambiguity will force
us to choose where the framers did not. Cyberspace will make the necessity of this
choice patent.

N I N E

t r a n s l a t i o n

At t he h ei ght of our l ast war on dr u gs — P r o h i bi t i on , in t h e l at e 1920s—t h e
federal government began using a technique of police work that startled many but
proved qu i te ef fective . The tech n i que was wi ret a pp i n g.1 Tel eph ones had become a
dominant mode of communication, life had just begun to move onto the wires, and
in an effort to take advantage of the evidence that this new medium might yield,the
government, without warrants, began to tap phones.

Because law enforcement officials themselves were conflicted about the ethics of
wiretapping, taps were used sparingly. Nonetheless, for threats perceived to be extrem ely grave , the tech n i que was dep l oyed . Ill egal alcohol h o l , as the ob s e s s i on of t h e
age, was just such a threat.

The most famous of these taps led to the 1928 Supreme Court case Olmstead v
United States. The government was investigating one of the largest illegal liquor import,distribution,and sales organizations in the nation. As part of the investigation,
the government began to tap the telephones used by dealers and their agents. These
were priva te ph on e s , but the taps were alw ays sec u red wi t h o ut trespassing on the
property of the targets.2 Instead, the taps were placed on the wires in places where
the government had rightful access to the phone lines. Though wiretapping was illegal under many states' laws,the government had not illegally trespassed on the defendants' property while tapping phones.

Using these taps, the govern m ent recorded many hours of convers a ti ons (775
typewritten pages, according to Justice Louis Brandeis's dissent)3, and it used these
recordings to convict the defendants in the case. The defendants challenged the use
of these recordings, claiming that the government had violated the Constitution in
securing them. The Fourth Amendment protects "persons, houses, papers, and effects, against unreasonable searches and seizures," and this wiretapping, the defendants argued , was a vi o l a ti on of t h eir ri ght to be pro tected from unre a s on a bl e
searches.

1 1 2

Under then-existing law, it was plain that to enter the apartments of Mr. Olmstead and his accomplices and search them (at least while they were gone), the government investigators would have needed a warrant,that is,they would have needed
the approval of a judge or magistrate before invading the defendants' privacy. This is
what the Fo u rth Am en d m ent had come to mean—that certain places (pers on s ,
houses,papers,and effects) were protected by presumptively requiring a warrant before they could be invaded.4 Here there had been no warrant, and hence, as the defendants argued, the search had been illegal. The evidence had to be excluded.

We might pause to ask why. If we read the text of the Fourth Amendment carefully, it is hard to see just where a warrant is required:

(a) The right of the people to be secure in their persons, houses, papers, and effects,against unreasonable searches and seizures,shall not be violat ed,and (b) no
Warrants shall issue, but upon probable cause, supported by Oath or affirmation,
and particularly describing the place to be searched, and the persons or things to
be seized.

The Fourth Amendment is really two commands. (I've added "a" and "b" to help
make the point.) The first says that a certain right ("the right of the People to be secure") shall not be violated; the second limits the conditions under which a warrant
shall be issued. But the text of the amendment does not state a relationship between
the first part and the second part. And it certainly does not say that a search is unreasonable if it is not supported by a warrant. So why "the warrant requirement"?5
To make sense of the amendment, we must go back to its framing . At that time,
the legal protection against the invasion of privacy was trespass law. If someone entered your property and rifled through your stuff, that person violated your common law rights against trespass. You could sue that person for trespass, whether he
was a police officer or private citizen. The threat of such suits gave the police an incentive not to invade your privacy.6

Even without a warrant, however, a trespassing police officer might have a number of defenses. These boil down to whether the search was "reasonable." But there
were two important facts about this reasonableness. First, the determination of reasonableness was made by a jur y. Neighbors and peers of the officer judged whether
his behavior had been proper. Second, in some cases reasonableness was found as a
matter of law—that is, the judge would instruct the jury to find that the search had
been reasonable.(For example, when the officer found contraband on the property
of the defendant, whether there was sufficient suspicion before the search or not, the
search was reasonable.)7

This regime cre a ted obvious risks for an of ficer before he search ed som eon e's
property. If he searched and found nothing, or if a jury thought later that his search
had not been reasonable, then he paid for his illegal behavior by being held personally liable for the rights he had violated.

1 1 3

But the regime also offered insurance against this liability—the warrant. If the
officer secured a warrant from a judge before he made his search, the warrant immunized him against trespass liability. If he then found no contraband or his search
turned out to be unreasonable, he still had a defense to a suit.

Creating incentives was one aim of the original system. The law gave an officer
an incentive to obtain a warrant before he searched; if he was uncertain, or wanted
to avoid all risk o f liability, he could first check his judgment by asking a judge. But
if the officer was sure, or wanted to hazard the gamble, then not getting a warrant
did not make the search automatically unreasonable. He was at risk of increased liability, but his liability was all that was at stake.

The weak link in this system was the judge. If judges were too lax, then warrants
would be too easy to get.8 And weak judges were a concern for the framers. Under
British rule judges had been appointed by the Crown, and by the time of the Revolution on the Crown was the en emy. Having seen mu ch abuse of the power to issu e
warrants, the framers were not keen to give judges control in determining whether
the government's searches were reasonable.

In particular (as I described in chapter 2),the framers had in mind some famous
cases in wh i ch ju d ges and the exec utive had issu ed "gen eral warra n t s" giving government officers the p ower to search generally for objects of contraband.9 In modern terms, these were "fishing expeditions." Because the officers had warrants, they
could not be sued; because the judges were largely immune from suit,they could not
be su ed . Because no one could be su ed , t h ere was a tem pt a ti on for abu s e . Th e
framers wanted to avoid just such judge-made abuse. If there was to be immunity, it
would come from a jury, or from a successful search.

This is the origin of clause (b) of the Fourth Amendment. The framers required
that judges, when issuing warrants,name particularly "the place to be searched, and
the persons or things to be seized," so that judges would not be able to issue warrants
of gen eral power. The immunity n i ty of the warrant would be limited to particular
people and places, and only when probable cause existed to issue the war rant.

This constitutional regime was designed to balance the people's interests in p rivacy against the legitimate need for the government to search. The officer had an incentive to get a warrant (to avoid the risk of personal liability); the judge had a rule
that re s tri cted the con d i ti ons under wh i ch he could issue a warra n t ; and toget h er
these structures limited official invasions of privacy to cases that presented a strong
reason to invade.

So much is background. But notice what follows.
The ori ginal regime pre su ppo s ed a great de a l . Most obvi o u s ly, it pre su ppo s ed a
com m on law sys tem of trespass law—it was the threat of l egal liabi l i ty from tre s p a s s
l aw that cre a ted the incen tives for of ficers to seek warrants in the first place . This presupposition ppo s i ti on placed property at the core of the Con s ti tuti on's ori ginal pro tecti on s .

Equally important, the r egime presupposed much about the technology of the
ti m e . The Fo u rth Am en d m ent focuses on trespass because that was the pri m a ry

1 1 4

mode of searching at the time. If it had been possible simply to view the contents of
a house without going inside,the restrictions of the Fourth Amendment would have
made little sense. But the protections of the amendment did make sense as a way to
d raw the balance bet ween govern m en t's power to search and the peop l e's ri ght to
privacy given the regime of trespass law and privacy-invading technologies that prevailed at the end of the eighteenth century.

Pre su ppo s i ti on s — what is taken for gra n ted or con s i dered undebatable a t a bl e —
change.10 How do we respond when such presuppositions change? How do we read
a text w ritten against a background of certain presuppositions when those presuppositions no longer apply?

For Am eri c a n s , or for any nati on with a con s ti tuti on some two hu n d red ye a rs
old, this is the central problem for constitutional interpretation. What if the state,
for example, were simply to abolish rights against trespass? Would the amendment
be read any differently?11 What if technologies for searching were to change so dramatically that no one would ever need to enter another's property to know just what
is kept there? Should the amendment then be read differently?

The history of the Supreme Court's treatment of such questions lacks a perfectly
clear pattern, but we can identify two distinct strategies, always competing for the
Court's attention. One strategy is focused on what the framers or founders would
have done—the strategy of one-step originalism. The second strategy aims at finding
a current reading of the original Constitution that preserves its original meaning in
the present context—a strategy that I call translation.

Both strategies are present in the Olmstead wiretapping case. When the government tapped the phones of the d defendants without any warrant, the Court had to
decide whether the use of this kind of evidence was p permissible or consistent with
the principles of the Fo u rth Am en d m en t . The defendants said: the govern m en t
must get a warrant to tap ph on e s . The govern m ent said: the Fo u rth Am en d m en t
simply does not apply.

The govern m en t's argument was qu i te simple. The amen d m ent pre su ppo s ed
that the government would be trespassing to search, and it was regulating the conditions under which officers could trespass. But because wiretapping is an invasion
of privacy without a trespass, the government is able to tap the defendants' phones
wi t h o ut ever en tering their property; the amen d m ent therefore does not app ly. It
simply does not reach to protect invasions that are invasions without trespass.

The Supreme Court agreed. In an opinion written by Chief Justice William H.

(and former President) Taft, the Court followed the government.

The amen d m ent does not forbid what was done here . Th ere was no search i n g.
There was no seizure. The evidence was secured by the use of the sense of hearing and that only. . . . The language of the amendment cannot be extended and
expanded to include telephone wires, reaching to the whole world from the defendant's house or office.12

1 1 5

This conclusion was received with some surprise, and also with shock. Already
much of life had moved to the wires. People were beginning to understand what it
meant to have intimate contact "online"; they counted on the telephone system to
protect their intimate secrets. Indeed, telephone companies, having strongly fought
the authority that the government claimed,pledged not to assist the government except as required by law.13 This resistance notwithstanding, the Court concluded that
the Constitution did not interfere with invasions of this sort. It would not have done
so when the Constitution was written;it did not do so at the time when the case was
decided.

But the dissent written by Justice Brandeis (the re was also a dissent by Justices
Holmes,Stone,and Butler) had a different view. Like Taft,the focus was fidelity. But
his fidelity was quite differently conceived.

Brandeis acknowledged that the Fourth Amendment, as originally w ritten, applied only to trespass.14 But it did so, he argued, because when it was written trespass
was the t echnology for invading privacy. That was the framers' presupposition, but
that pre su ppo s i ti on had now ch a n ged . G iven this ch a n ge , Bra n deis argued , it was
the Court's responsibility to read the amendment in a way that preserved its meaning, changed circumstances notwithstanding. The aim must be to translate the original pro tecti ons into a con text in wh i ch the tech n o l ogy for invading privacy had
ch a n ged .1 5 This would be don e , Bra n deis argued , by app lying the Fo u rth Am en demand's protection to invasions that were not themselves trespasses.

These two opinions mark two different modes of constitutional interpretation.
Taft finds fidelity by simply repeating what the framers did; Brandeis finds fidelity by
finding the current equivalent to what the framers did. If we followed Taft, Brandeis
argued, we would defeat the protections for privacy that the framers originally set; if
we followed Brandeis, Taft implied, we would be adding to the Constitution something that the framers had not written.

Pa Partisans on both sides cl a i m ed that the op i n i on of the other would have
"changed"the meaning of the Constitution. But whose opinion, the Court's or Justice Brandeis's, would really "change" the meaning of the Fourth Amendment?

To answer this qu e s ti on , you would first have to ask: Ch a n ge rel a tive to wh a t ?
What is the baseline against which this change is a change? Certainly Brandeis would
have agreed that in 1791, just after the amendment was passed, any finding by the
Court that the amendment reached beyond trespass would have been improper. But
wh en som ething pre su ppo s ed by the ori ginal amen d m ent has ch a n ged , is it cl e a r
that the Court's proper response is to act as if nothing has changed at all?

Brandeis's method accounted for the changed presupposition. He offered a reading that changed the scope of the amendment in order to maintain the amendment's
protection of privacy. Taft, on the other hand, offered a reading that maintained the
scope of the amendment but changed its protection of privacy. Each reading kept
something constant; each also changed something. The question is: Which reading
preserved what fidelity demands should be preserved?

1 1 6

We might better see the point through a somewhat stylized re-creation. Imagine
that we could quantify privacy: we could thus describe the change in the quantity of
privacy that any change in technology might bring. (Robert Post has given an abs o lutely persu a s ive argument abo ut why privacy is not qu a n ti f i a bl e , but my purposes here are simply illu s tra tive .1 6) Im a gine then that in 1791 pro tecting aga i n s t
physical trespass pro tected 90 percent of pers onal privac y. The govern m ent co u l d
still stand on the street and listen through open windows, but the invasion presented
by that threat was small, all things considered. For the most part, a regime that protected against trespass also protected privacy.

When telephones came along, however, this protection changed.A lot of private
information was put out across the phone lines. Now, if tapping was not trespass,
much less of private life was protected from government snooping. Rather than 90
percent being protected by the amendment, only 50 percent was protected.

Brandeis wanted to read the amendment so that it protected what it originally
pro tected—the 90 percent t , even though doing so requ i red that it pro tect aga i n s t
more than simple trespass. He wanted to read it differently, we could say, so that it
protected the same.

This form of argument is common in our constitutional history, and central to
the best in our constitutional tradition.17 It is an argument that responds to changed
circumstances by proposing a reading that neutralizes those changes and preserves
an original meaning. It is an argument invoked by justices on both the right and the
l ef t .1 8 It is a way to keep life in a con s ti tuti onal provi s i on — to make certain that
changes in the world do not change the meaning of the Constitution's text. It is an
a r g u m en t , we can say, that aims at tra n s l a ti n g the pro tecti ons that the Fo u rt h
Amendment gave in 1791 into the same set of protections at any time later in our
history. It acknowledges that to do this the Court may have to read the amendment
differently. But it is not reading the amendment differently to improve the amendment or to add to its protections. It is reading the amendment differently to accommodate the changes in protection that have resulted from changes in technology. It
is translation to preserve meaning.

If t h ere is a ju s ti ce who de s erves c-worl d 's pra i s e , i f t h ere is a Su preme Co u rt
opinion that should be the model for cyberactivists in the future, if there is a first
chapter in the fight to protect cyberspace,it is this Justice,this opinion,and this case.
Brandeis gave us a model for reading the Constitution to preserve its meaning, and
its values, across time and context. It is a method that recognizes what has changed
and accom m od a tes that ch a n ge to pre s erve som ething of what the fra m ers ori ginally gave us. It is a method,again,that translates the Constitution's meaning across
fundamentally different contexts—whether they are as temporally distant as we are
from the framers or as distant as cyberspace is from real space.

But it was Ta f t's op i n i on that became law, and his narrow vi ew of the Fo u rt h
Am en d m ent that preva i l ed . It took forty ye a rs for the Su preme Co u rt to em brace
Bra n dei s's pictu re of the Fo u rth Am en d m en t — forty ye a rs before O l m s tead w a s
overruled. The case overruling it was Katz v United States.19

1 1 7

Charles Katz was suspected o f transmitting gambling information to clients in
other states by telephone. Federal agents recorded his half of several of his telephone
calls by attaching an eavesdropping device to the outside of a public phone booth
where he made his calls. Katz was convicted on the basis of this evidence, and the
court of appeals upheld the conviction on the basis of Olmstead.

Harvard Law School Professor Laurence Tribe was involved in the case at the beginning of his legal career:

As a [law] clerk to Supreme Court Justice Potter Stewart,I found myself working
on a case involving the government's electronic surveillance of a suspected criminal in the form of a ti ny devi ce attach ed to the out s i de of a public tel eph on e
boo t h . Because the inva s i on of the su s pect's privacy was accom p l i s h ed wi t h o ut
physical trespass into a "constitutionally protected area," the Federal Government
argued, relying upon Olmstead, that there had been no "search" or "seizure" and
therefore the Fourth Amendment "right of the people to be secure in their pers on s , h o u s e s , p a pers , and ef fect s , a gainst unre a s on a ble searches and sei z u re s"
simply did not apply.

At first,there were only four votes to overrule Olmstead and to hold the Fourth
Amendment applicable to wiretapping and electronic eavesdropping. I'm proud
to say that, as a 26-year-old kid,I had at least a little bit to do with changing that
nu m ber from four to seven—and with the argumen t , form a lly adopted by a
seven-Justice majority in December 1967,that the Fourth Amendment "protects
peop l e , not place s" [389 US at 351]. In that dec i s i on , Katz v. Un i ted St a te s , t h e
Supreme Court finally repudiated Olmstead and the many decisions that had relied upon it, reasoning that, given the role of electronic telecommunications in
modern life,the [First Amendment] purposes of protecting free speech as well as
the [Fo u rth Am en d m ent] purposes of pro tecting priva c y requ i re tre a ting as a
"search" any invasion of a person's confidential telephone communications, with
or without physical trespass.20

The Court in Katz followed Brandeis rather than Taft. It sought a reading of the
Fourth Amendment that made sense of the amendment in a changed context. In the
framers' context of 1791, protecting against trespass to property was an effective way
to protect against trespass to privacy, but in the Katz context of the 1960s it was not.
In the 1960s much of intimate life was conducted in places where property rules did
not reach (in the "ether," for example, of the AT&T telephone network). And so a
regime that made privacy hang on property did not protect privacy to the same degree that the framers had intended. Justice Stewart in Katz sought to remedy that by
linking the Fourth Amendment to a more direct protection of privacy.

The link was the idea of "a re a s on a ble ex pect a ti on of privac y." The core va lu e ,
S tew a rt wro te , was the pro tecti on of "peop l e , not place s"2 1; h en ce , the core technique should be to protect people where they have an expectation of privacy, and
where that expectation is reasonable. Where people have a reasonable expectation of

1 1 8

privac y, the govern m ent cannot invade that space wi t h o ut sati s f ying the requ i rements of the Fourth Amendment.

There is much to admire in Stewart's opinion,at least to the extent that he is willing to fashion tools for preserving the Constitution's meaning in changed circumstances—or again, to the extent that he attempts to translate the protections of the
Fourth Amendment into a modern context. There is also much to question.22 But
we can put those questions aside for the moment and focus on one feature of the
problem that is fairly uncontentious.

While lines will be hard to draw, it is at least fairly clear that the framers made a
conscious choice to protect privacy. This was not an issue off the table of their original debate, or a question they did not notice. And this is not the "right to privacy"
that conservatives complain about in the context of the right to abortion. This is the
ri ght to be free from state intru s i on into the "s a n cti ty " of a priva te hom e . S t a te -
enforced threats to individual privacy were at the center of the movement that led to
the rep u bl i c . Bra n deis and Stew a rt simply aimed to ef fect that ch oi ce in con tex t s
where the earlier structure had grown ineffectual.

Translations like these are fairly straightforward. The original values chosen are
fairly clear; the way in which contexts undermine the original application is easily
grasped; and the readings that would restore the original values are fairly obvious.
Of course, such cases often require a certain interpretive courage—a willingness to
preserve interpretive fidelity by changing an interpretive practice. But at least the direction is clear, even if the means are a bit unseemly.23

These are the easy cases.They are even easier when we are not trying to carry values from some distant past into the futu re but inste ad are simply carrying va lu e s
from one context into another. When we know what values we want to preserve, we
need only be creative about how to preserve them in a different context.

Cyberspace will present many such easy cases. When courts confront them,they
should follow the example of Brandeis: they should translate, and they should push
the Supreme Court to do likewise. Where circumstances have changed to nullify the
protections of some original right, the Court should adopt a reading of the Constitution that restores that right.

But some cases will not be so easy. Sometimes translation will not be an option.
Sometimes the values that translation would track are values we no longer want to
preserve. And sometimes we cannot tell which values translation would select. This
was the probl em in ch a pter 2 with the worm , wh i ch made the point abo ut laten t
ambiguities. Changing contexts sometimes reveals an ambiguity latent in the original con tex t . We must then ch oose bet ween two different va lu e s , ei t h er of wh i ch
could be said to be consistent with the original value. Since either way could be said
to be right, we cannot say that the original context (whether now or two hundred
years ago) decided the case.

Professor Tribe describes an example in a founding article in the law of cyberspace, "The Constitution in Cyberspace."24 Tribe sketches a method of reading the
Con s ti tuti on in cybers p ace that aims to make the Con s ti tuti on "tech n o l ogi c a lly

1 1 9

neutral." The objective is to adopt readings (or perhaps even an amendment) that
make it plain that changes in technology are not to change the Constitution's meaning. We must always adopt readings of the Constitution that preserve its original judges d ges are to be tra n s l a tors ; d i f feren t
u e s . Wh en dealing with cybers p ace ,
technologies are the different languages; and the aim is to find a reading of the Constitution that preserves its meaning from one world's technology to another.25

This is fidelity as translation. This kind of translation speaks as if it is just carrying over something that has already been said. It hides the creative in its act;it feigns
a certain polite or respectful deference. This way of reading the Constitution insists
that the important po l i tical dec i s i ons have alre ady been made and all that is required is a kind of technical adjustment. It aims at keeping the piano in tune as it is
moved from one concert hall to another.

But Tribe then offers an example that may make this method seem empty. The
qu e s ti on is abo ut the meaning of the con f ron t a ti on clause of the Sixth Am en amendment—the defendant's right in a criminal trial "to be confronted with the witnesses
against him." How, Tribe asks, should we read this clause today?

At the time of the founding, he argues, the technology of confrontation was simple—confrontation was two-way. If a witness confronted the accused, the accused,
of necessity, confronted the witness. This was a necessity given to us by the technology of the time. But today it is possible for confrontation to be one-way—the witness con f ronts the acc u s ed , but the acc u s ed need not con f ront the wi tn e s s . Th e
question then is whether the confrontation clause requires one-way or two-way confrontation.26

Let us grant that Tri be's de s c ri pti ons of the ava i l a ble tech n o l ogies are correct
and that the fra m ers em braced the on ly con f ron t a ti on clause that their tech n o l ogy
perm i t ted . The real qu e s ti on comes in step two. Now that tech n o l ogy all ows two
po s s i bi l i ti e s — on e - w ay or two - w ay con f ron t a ti on — wh i ch does the Con s ti tuti on
re q u i re ?

The Court's answer in its 1990 decision in Maryland v Craig was clear: the Cons ti tuti on requ i res on ly on e - w ay con f ron t a ti on . A con f ron t a ti on clause regime that
permits only one-way confrontation, at least when there are strong interests in not
requiring two, is a fair translation of the original clause.27

As a matter of po l i tical ch oi ce , I cert a i n ly like this answer. But I do not see its
source. It seems to me that this is a question the framers did not decide, and a question that if presented to them might well have divided them. Given the technology
of 1791, they did not have to decide between one-way and two-way confrontation;
given the conflict of values at stake, it is not obvious how they would have decided
it. Thus, to speak as if there were an answer here that the framers simply gave us is a
bit misleading. The framers gave no answer here,and in my view, no answer can be
drawn from what they said.

Like the worm in chapter 2, the confrontation clause presents a latent ambiguity -
ity.28 Constitutional law in cyberspace will reveal many such latent ambiguities. And
these ambiguities offer us a choice: How will we go on?

1 2 0

Choices are not terrible. It is not a disaster if we must make a decision—so long,
that is, as we are capable of it. But here is the nub of the problem that I see. As I argue in more detail in part 4, given the current attitudes of our courts, and our legal
c u l tu re gen era lly, con s ti tuti onal ch oi ces are co s t ly. We are bad at making these
choices; we are not likely to get better at it soon.

Wh en there is no answer abo ut how to proceed — wh en the tra n s l a ti on leave s
open a question—we have two sorts of responses in constitutional practice. One response is passive: the court simply lets the legislature decide as it will. This is the response that Justice Scalia presses in the context of the Fourteenth Amendment. On
matters that, to the framers, were "undebatable," the Constitution does not speak. 29
In this case, only the legislature can engage, and press, questions of constitutional
value and thus say what the Constitution will continue to mean.

The second response is more active: the court finds a way to articulate constitutional values that were not present at the founding. The courts help spur a convers a ti on abo ut these fundamental va lu e s — or at least add their voi ce to this
conversation—to focus a debate that may ultimately be resolved elsewhere. The first
response is a way of doing nothing; the second is a way of exciting a dialogue about
constitutional values as a means to confronting and resolving new questions.

My fear about cyberspace is that we will respond in the first way—that the instituti ons most re s pon s i ble for arti c u l a ting con s ti tuti onal va lues wi ll simply stand
back while issues of constitutional import are legislatively determined. The institutions most responsible for articulating constitutional values today are the courts.My
sense is that they will step back because they feel (as the balance of this book argues)
that these are new qu e s ti ons that cybers p ace has ra i s ed . Th eir newness wi ll make
t h em feel po l i ti c a l , and wh en a qu e s ti on feels po l i ti c a l , co u rts step aw ay from resolving it.

I fear this not because I fear legislatures, but because in our day constitutional
discourse at the le vel of the legislature is a very thin sort of discourse. The philosoph er Bern a rd Wi Williams has argued that because the Su preme Co u rt has taken so
central a role in the articulation of constitutional values, legislatures no longer do.30
Whether Williams is correct or not, this much is clear: the constitutional discourse
of our present Congress is far below the level it must be at to address the questions
about constitutional values that will be raised by cyberspace.

How we could re ach beyond this thinness of d i s co u rse is unclear e a r. We are in a
time when constitutional thought has been for too long the domain of lawyers and
judges. We have been trapped by a mode of reasoning that pretends that all the important questions have already been answered, that our job now is simply to translate them for modern times. As a result, we do not quite know how to proceed when
we think the answers are not already there. As nations across the world struggle to
express and embrace constitutional values, we, with the oldest written constitutional
tradition, have lost the practice of embracing, articulating, and deciding on constitutional values.

1 2 1

I return to this problem in chapter 15. For now, my point is simply descriptive.
Translation is one way to deal with the choices that cyberspace presents. It is one way
of finding equ iva l en ce ac ross con tex t s . But in the four app l i c a ti ons that fo ll ow, I
press the qu e s ti on : Is the past en o u gh? Are there ch oi ces the fra m ers did not address? Are they choices that we could make?

T E N

i n t e l l e c t u a l p r o p e r t y

Har ol d Reeves is among t h e best r research ch assist ant s I h ave h ad. He wor ked
with me to develop the first course I taught on the law of cyberspace.Early into his
second year at the University of Chicago Law School,he came to me with an idea he
had for a student comment—a student article that would be published in the law review.1 The topic was trespass law in cyberspace—whether and how the law should
protect owners of space in cyberspace from the kinds of intrusions that trespass law
protects against in real space. His initial idea was simple: there should be no trespass
law in cyberspace.2 The law should grant "owners" of space in cyberspace no legal
protection against invasion. They should be forced to fend for themselves.

Reeves's idea was a bit nutty, and in the end,I think, wrong.3 But it contained an
insight that was quite genius,and that should be central to thinking about law in cyberspace.

The ide a — mu ch more bri efly and mu ch less el ega n t ly than Reeves has put it—is
t h i s : the qu e s ti on that law should ask is what means would bring abo ut the most ef fic i ent set of pro tecti ons for property interests in cybers p ace . Two sorts of pro tecti on s
a re po s s i bl e . One is the trad i ti onal pro tecti on of l aw—the law defines a space wh ere
o t h ers should not en ter and punishes people who non et h eless en ter. The other protecti on is a fen ce , a tech n o l ogical devi ce (a bit of code) that (among other things )
bl ocks the unw a n ted from en teri n g. In real space , of co u rs e , we have bo t h — l aws and
fen ces that su pp l em ent law. No do u bt there is some optimal mix bet ween fen ces and
l aw. Both cost mon ey, and the retu rn from each is not nece s s a ri ly the same. From a social pers pective , we would want the mix that provi des optimal pro tecti on at the lowe s t
co s t . ( In econ om i c s - s pe a k , we would want a mix su ch that the marginal cost of an add i ti onal unit of pro tecti on is equ iva l ent to the marginal ben efit . )

The implication of this idea in real space is that it sometimes makes sense to shift
the burden of protection to citizens rather than the state. If, for example, a farmer
wants to store some valuable seed on a remote part of his farm, it is better for him
to bear the cost of fencing in the seed than to require the police to patrol the area

1 2 3

more consistently or to increase the punishment for those they catch. The question,
then, is always one of balance between the costs and benefits of private protection
and state protection.

Reeves's insight about cyberspace follows the same line. The optimal protection
for spaces in cyberspace is a mix between public law and private fences. The questi on to ask in determining the mix is wh i ch pro tecti on , on the margi n , costs less.
Reeves argues that the costs of law in this context are extremely high—in part because of the costs of enforcement, but also because it is hard for the law to distinguish bet ween legi ti m a te and ill egi ti m a te uses of c ybers p ace s . Th ere are many
"agents" that might "use" the space of cyberspace. Web spiders, which gather data for
web search engines; browsers, who are searching across the Net for stuff to see;hackers (of the good sort) who are testing the locks of spaces to see that they are lo cked;
and hackers (of the bad sort) who are breaking and entering to steal. It is hard, ex
ante, for the law to know which agent is using the space legitimately and which is
not. Legitimacy depends on the intention of the person granting access.

So that led Reeves to his idea: since the intent of the "owner" is so crucial here,
and since the fen ces of c ybers p ace can be made to reflect that intent ch e a p ly, it is
best to put all the incentive on the owner to define access as he wishes. The right to
browse should be the norm, and the burden to lock doors should be placed on the
owner.4

Now put Reeves's argument aside, and think for a second about something that
will seem completely different but is very much the same idea. Think about "theft"
and the protections that we have against it.

I have a stack of firewood behind my house. No one steals it. If I left my bike out
overnight,it would be gone.

A friend told me that, in a favorite beach town, the city used to find it impossible to plant flowers—they would immediately be picked. But, he now proudly
report s , a f ter a long "com mu n i ty spiri t" c a m p a i gn , the flowers are no lon ger
picked.

There are special laws about the theft of automobiles,planes,and boats. There
a re no special laws abo ut the theft of s kys c ra pers . Ca rs , p l a n e s , and boats need
protection. Skyscrapers pretty much take care of themselves.

Many things protect property against theft—differently. The market protects my
firewood (it is cheaper to buy your own than it is to haul mine away); the market is
a special threat to my bike (which if taken is easily sold). Norms sometimes protect
flowers in a park; sometimes they do not. Nature sometimes conspires with thieves
(cars,planes, and boats) and sometimes against them (skyscrapers).

These protections are not fixed. I could lock my bike and thereby use real-space
code to make it harder to steal. There could be a shortage of firewood,increasing demand and making it harder to protect. Public campaigns about civic beauty might
s top flower thef t ; s el ecting a disti n ctive flower might do the same. Soph i s ti c a ted

1 2 4

l ocks might make sto l en cars usel e s s ; s oph i s ti c a ted bank fraud might make skyscrapers c ra pers vu l n era bl e . The point is not that pro tecti ons are given , or unch a n ge a bl e ,
but that they are multiplied and their modalities different.

Property is protected by the sum of the different protections that law, norms,the
market, and real-space code yield. This is just an application of the point made in
chapter 7. From the point of view of the state, we need law only when the other three
m od a l i ties leave property vu l n era bl e . From the point of vi ew of the citi zen , re a l -
s p ace code (su ch as locks) is needed wh en laws and norms alone do not pro tect
enough. Understanding how property is protected means understanding how these
different protections work together.

Reeves's idea and these reflections on firewood and skyscrapers point to the different ways that law might pro tect "property " and su ggest the ra n ge of kinds of
property that law might try to pro tect . Th ey also invi te a qu e s ti on that has been
asked by Justice Stephen Breyer and many others: Should law protect some kinds of
property—in particular, intellectual property—at all?5

Among the kinds of property law might protect, my focus in this chapter will be
on just one—"intellectual property," or more particularly, the property protected by
copyright. Of all the different types of property, this type is said to be the most vulnerable to the changes that cyberspace would bring. Intellectual property, it is said,
cannot be protected in cyberspace. And in the terms that I've sketched, we can begin
to see why—and more important, why what is said must be wrong.

O N T H E R E P O R T S O F C O P Y R I G H T ' S

D E M I S E

Roughly put, copyright gives a copyright holder the right to control the copying of
that to which the right extends.6 I have a copyright in this book. That means, subject
to some important exceptions, you cannot copy this book without my permission.
The right is protected to the extent that laws (and norms) support it,and it is threatened to the extent that technology makes it easy to copy. Strengthen the law, holding
tech n o l ogy con s t a n t , and the ri ght is stron ger. S tren g t h en the tech n o l ogy, h o l d i n g
the law constant, and the right is weaker.7

In this sense, copyright has always been at war with technology. Before the printing press (and especially the availability of paper8),there was not much need to protect an author's copyright. Copying was so expensive that nature itself protected that
ri gh t . But as the cost of copying dec re a s ed , the threat to the aut h or 's con trol increased. As each generation has delivered a technology better than the last, the ability of the copyright holder to protect her intellectual property has been weakened.
But up to now, the law could respond quite easily. If photocopying machines in
libraries posed a new threat to the right, then the law could be modified to better
deal with photocopying machines.9 If videotape allowed TV viewers to tape a show
to view at a different time, the law could be modified to deal with time shifting.10 In

1 2 5

all these cases,the real protection accorded to property is the sum of these different
kinds of constraints; we can see that increases in legal protection, in response to inc re a s ed threats to copyi n g,1 1 m ay on balance simply re s tore the power an aut h or
once held rather than increase the author's right. 12

Fortu n a tely, f rom law 's pers pective at least, tech n o l ogical ch a n ges have alw ays
been gradu a l . Copies have become bet ter and ch e a per, but on ly by degree s , a n d
over a rel a tively ex ten ded peri od . Th ere have been shocks to the sys tem , but the
l aw has had time to re act wh en the old sys tem seem ed out of s tep — by slowly
m od i f ying its pro tecti ons and ex tending them wh ere tech n o l ogy seem ed to be
eroding them .1 3

It is said by some that cybers p ace ch a n ges not on ly the tech n o l ogy of copyi n g
but also (and more important) the power of law to protect against illegal copying.14
It does both simultaneously, and extremely quickly. Not only does the Net promise
perfect copies of digital originals at practically no cost,15 but it also threatens to impose an almost impossible task on law enforcers: tracing and punishing copyright
violators. In the terms of chapter 7: the effective constraint of law (against copying)
disappears just at the time when the constraints of technology disappear as well. The
t h reat po s ed by tech n o l ogy is maximal, while the pro tecti on prom i s ed by law is
minimal. For the holder of the copyright,cyberspace appears to be the worst of both
worlds—a place where the ability to copy could not be better, and where the protection of law could not be worse.

Talk like this gave birth to the panic of copyright holders, who wanted to see legislative changes made to better protect the copyright. For of course, the predictions
of c ybers p ace mavens notwi t h s t a n d i n g, not everyone was wi lling to con cede that
copyri ght law was de ad . In tell ectual property law yers and interest groups pushed
early on to have law shore up the protections of intellectual property that cyberspace
would erase.

L A W T O T H E R E S C U E

The produ ct of the ori ginal push was a Wh i te Pa per produ ced by the Com m erce
Dep a rtm ent in 1995 after soliciting com m ents for more than two ye a rs abo ut how
c ybers p ace thre a ten ed copyri gh t .1 6 The Wh i te Pa per out l i n ed a series of m od i f i c ati ons aimed , it said, at re s toring "b a l a n ce" in intell ectual property law. E n ti t l ed
" In tell ectual Property and the Na ti onal In form a ti on In f ra s tru ctu re ," the report
s o u ght to re s t a te ex i s ting intell ectual property law in terms that anyone could unders t a n d , as well as recom m end ch a n ges in the law in re s ponse to the ch a n ges the
Net would bri n g. But as sch o l a rs qu i ck ly poi n ted out , the first part was a bu s t .1 7
The report no more "re s t a ted " ex i s ting law than Sovi et historians "reto l d " s tori e s
of S t a l i n's ad m i n i s tra ti on . The re s t a tem ent had a ti l t , very def i n i tely in the directi on of i n c re a s ed intell ectual property pro tecti on , but it preten ded that its tilt was
the natu ral lay of the land.

1 2 6

For our purposes, however, it is the recommendations that are most significant.
The government proposed four responses to the threat presented by cyberspace. In
the terms of chapter 7, these responses should be familiar.

The first response was traditional. The government proposed changes in the law
of copyright to "clarify" the rights that it was to protect.18 These changes were intended to better define the rights granted under intellectual property law and to further support these rights with clarified (and possibly greater) legal penalties for their
violation.

But the proposal went far beyond these traditional means.A second recommendation was for increased educational efforts, both in the schools and among the general publ i c , a bo ut the natu re of i n tell ectual property and the import a n ce of
protecting it. In the terms of chapter 7,this is the use of law to change norms so that
n orms wi ll bet ter su pport the pro tecti on of i n tell ectual property. It is an indirect
regulation of behavior by direct regulation of norms.

Education was not, however, the most significant indirect regulation. More interesting for our pur poses was the government's financial and legal support for the
development of copyright management schemes—software that would make it easi er to con trol access to and use of copyri gh ted materi a l . We wi ll ex p l ore these
s ch schemes at some length later in this ch a pter, but I men ti on it now as another example of indirect regulation—using the market to subsidize the development of a
certain sof t w a re too l , and using law to reg u l a te the properties of o t h er sof t w a re
tools. Copyright manag ement systems are supported by government funding, and
the threat of felony conviction hangs over anyone interested in designing software to
crack them.19

The 1995 package of proposals was a scattershot of techniques—some changes
in law, some support for changing norms,and lots of support for changing the code
of cyberspace to make it better able to protect intellectual property. Perhaps nothing
better than this could have been expected in 1995. The law promised a balance of responses to deal with the shifting balance brought on by cyberspace.

Ba l a n ce is attractive . Modera ti on seems ri gh t . But som ething is missing from
this approach. The White Paper proceeds as if the problem of protecting intellectual
property in cyberspace were just like the problem of protecting intellectual property
in real space. It proceeds as if the four constraints would operate in the same proportions as in real space, as if nothing fundamental had changed.

But something fundamental has changed: the role that code plays in the protection of intellectual property has changed. Code can, and increasingly will, displace
law as the primary defense of intellectual property in cyberspace. Private fences, not
public law.

The White Paper does not see this. Built into its scattershot of ideas is one that is
crucial to its approach but fundamentally wrong—the idea that the nature of cyberspace is anarchy. The White Paper promises to strengthen law in every area it can.
But it approaches the question like a ship battening down for a storm: whatever happens n t e l l e c t u a l p r o p e r t y

1 2 7

pens, the threat to copyright is real, damage will be done, and the best we can do is
ride it out.

This is fundamentally wrong. We are not entering a time when copyright is more
threatened than it is in real space. We are instead entering a time when copyright is
more effectively protected than at any time since Gutenberg. The power to regulate
access to and use of copyri gh ted material is abo ut to be perfected . Wh a tever the
mavens of the mid-1990s may have thought, cyberspace is about to give holders of
copyrighted property the biggest gift of protection they have ever known.

In su ch an age—in a time wh en the pro tecti ons are being perfected—the re a l
question for law is not, how can law aid in that protection? but rather, is the protecti on too great? The mavens were ri ght wh en they pred i cted that cybers p ace wi ll
teach us that everything we thought about copyright was wrong.20 But the lesson in
the future will be that copyright is protected far too well. The p roblem will center
not on copy-right but on copy-duty—the duty of owners of protected property to
make that property accessible.

That's a big claim. To see it, however, and to see the consequences it entails, we
need consider only two small examples. The first is a vision of a researcher from Xerox PARC (appropriately enough), Mark Stefik, and his idea of "trusted systems."21
The second is an implication of a world dominated by trusted systems. Both examples will throw into relief the threat that these changes present for values that our
tradition considers fundamental. Both should force us to make a choice about those
values,and about their place in our future.

T H E P R O M I S E F O R I N T E L L E C T U A L

P R O P E R T Y I N C Y B E R S P A C E

It all depends on wh et h er you re a lly understand the idea of tru s ted sys tem s . If you
d o n't understand them , t h en this wh ole approa ch to co m m erce and digital pu bl i s h i n g
is utterly unthinkable e . If you do understand them ,t h en it all foll ows easily.

Ralph Merkle, quoted in Stefik,"Letting Loose the Light" (1996)

Given the present code of the Internet, you can't control well who copies what. If
you have a copy of a copyrighted photo, rendered in a graphics file, you can make
unlimited copies of that file with no effect on the original. When you make the onehundredth copy, nothing indicates that it is the one-hundredth copy rather than the
first. There is very little in the code as it exists now that regulates the distribution of
and access to material on the Net.

This probl em is not unique to cybers p ace . We have alre ady seen a tech n o l ogy
that presented the same problem; a solution to the problem was subsequently built

1 2 8

i n to the tech n o l ogy.2 2 Di gital audio tech n o l ogy (DAT) tape was a threat to copyright, and a number of solutions to this threat were proposed. Some people argued
for higher penalties for illegal copying of tapes (direct regulation by law). Some arg u ed for a tax on blank tape s , with the proceeds com pen s a ting copyri ght holders
(indirect regulation of the market by law). Some argued for better education to stop
illegal copies of tapes (indirect regulation of norms by law). But some argued for a
change in the code of tape machines that would block unlimited perfect copying.

With the code changed, when a machine is used to copy a particular CD, a serial
number from the CD is recorded in the tape machine's memory. If the user tries to
copy that tape more than a limited number of times, the machine adjusts the quality of the copy. As the copies increase, the quality is degraded. This degradation is
deliberately created. Before DAT, it was an unintended consequence of the copying
technologies—each copy was unavoidably worse than the original. Now it has been
reintroduced to restore a protection that had been eroded by technology.

The same idea animates Stefik's vision, though his idea is not to make the quality of copies decrease but rather to make it possible to track and control the copies
that are made.23

Think of the proposal like this. Tod ay, wh en you buy a boo k , you may do any
number of things with it. You can read it once or one hundred times. You can lend
it to a friend. You can photocopy pages in it or scan it into your computer. You can
burn it, use it as a paperweight, or sell it. You can store it on your shelf and never
once open it.

Some of these things you can do because the law gives you the ri ght to do
them—you can sell the book, for example, because the copyright law explicitly gives
you that right. Other things you can do because there is no way to stop you.A book
seller might sell you the book at one price if you promise to read it once, and at a
different price if you want to read it one hundred times, but there is no way for the
seller to know whether you have obeyed the contract. In principle, the seller could
sell a police officer with each book to follow you around and make sure you use the
book as you promised, but the costs would plainly be prohibitive.

But what if e ach of these ri ghts could be con tro ll ed , and each unbundled n dl ed and
sold separately? What if, that is, the software itself could regulate whether you read
the book once or one hundred times; whether you could cut and paste from it or
simply read it without copying; whether you could send it as an attached document
to a friend or simply keep it on your machine; whether you could delete it or not;
whether you could use it in another work, for another purpose, or not; or whether
you could simply have it on your shelf or have it and use it as well?

Stefik describes a network that makes such unbundling of rights possible. He describes an architecture for the network that would allow owners of copyrighted materials to sell access to those materials on the terms they want and would en force
those contracts.

The details of the system are not important here24 (it builds on the encryption
architecture I described in chapter 4), but its general idea is easy enough to describe.

1 2 9

As the Net is now, basic functions like copying and access are crudely regulated in an
all-or-nothing fashion. You generally have the right to copy or not, to gain access or
not.

But a more sophisticated system of rights could be built into the Net—not into
a different Net, but on top of the existing Net. This system would function by discriminating in the intercourse it has with other systems.A system that controlled access in this more fine-gra i n ed way would grant access to its re s o u rces on ly to
another system that controlled access in the same way. A hierarchy of systems would
develop, and copyrighted material would be traded only among systems that p roperly controlled access.

In such a world,then, you could get access, say, to the New York Times and pay a
different price depending on how much of it you read. The Times could determine
how much you read, whether you could copy portions of the newspaper, whether
you could save it on your hard disk,and so on. But if the code you used to access the
Times site did not enable the control the Times demanded,then the Times would not
let you onto its site at all. In short, systems would e xchange information only with
others that could be trusted, and the protocols of trust would be built into the architectures of the systems.

Stefik calls this "trusted systems," and the name evokes a helpful analog. Think of
bonded couriers. Sometimes you want to mail a letter with something particularly
valuable in it. You could simply g ive it to the post office, but the post office is not a
terri bly rel i a ble sys tem ; it has rel a tively little con trol over its em p l oyee s , and thef t
and loss are not uncommon. So instead of going to the post office, you could give
your letter to a bonded courier. Bonded couriers are insured, and the insurance is a
cost that constrains them to be reliable. This reputation then makes it possible for
senders of valuable material to be assured about using their se services.

This is what a structure of trusted systems does for owners of intellectual property. It is a bonded courier that takes the thing of value and controls access to and
use of it according to the orders given by the principal.

Im a gine for a mom ent that su ch a stru ctu re em er ged gen era lly in cybers p ace .

How would we then think about copyright law?

An important point about copyright law is that, though designed in part to protect authors, its protection was not to be absolute—the copyright is subject to "fair
use," limited terms, and first sale. The law threatened to punish violators of copyright laws—and it was this threat that induced a fairly high proportion of people to
comply—but the law was never designed to simply do the author's bidding. It had
public purposes as well as the author's interest in mind.

Trusted systems provide authors with the same sort o f protection. Because authors can restrict unauthorized use of their material, they can extract money in exchange for access. Trusted systems thus a achieves what copyright law achieves. But it
can achieve this protection without the law doing the restricting. It permits a much
more fine-grained control over access to and use of protected material than law permits, and it can do so without the aid of the law.

1 3 0

What copyri ght seeks to do using the threat of l aw and the push of n orm s ,
trusted systems do through the code. Copyright orders others to respect the rights of
the copyright holder before using his property. Trusted systems g ive access only if
rights are respected in the first place. The controls needed to regulate this access are
built into the systems,and no users (except hackers) have a choice about whether to
obey these con tro l s . The code displaces law by cod i f ying the ru l e s , making them
more efficient than they were just as rules.

Trusted systems in this scheme are an alternative for protecting intellectual property rights—a privatized alternative to law. They need not be exclusive; there is no
reason not to use both law and trusted systems. Nevertheless, the code in effect is
doing the work that the law used to do. It implements the law's protection, through
code, far more effectively than the law did.

What could be wrong with this? We do not worry wh en people put do u ble bolts on
t h eir doors to su pp l em ent the work of the nei gh borh ood cop. We do not worry wh en
t h ey lock their cars and take their keys . It is not an of fense to pro tect yo u rs el f ra t h er
than rely on the state . In deed , in some con texts it is a vi rtu e . An d rew Jack s on's mother,
for ex a m p l e , told him," Never tell a lie, n or take what is not your own ,n or sue anybody
for slander, assault and battery. Alw ays settle them cases yo u rs el f ."2 5 Sel f - su f fic i ency is
of ten seen as a sign of s tren g t h , and going to the law as a sign of we a k n e s s .

There are two steps to answering this question. The first rehearses a familiar but
forgotten point about the nature of property; the second makes a less familiar, but
central, point about the nature of intellectual property. Together they suggest why
perfect control is not the control that law has given owners of intellectual property.

T H E L I M I T S O N T H E P R O T E C T I O N O F

P R O P E R T Y

The realists in American legal history (circa 1890–1930) were scholars who (in part)
emphasized the role of the state in what was called "private law."26 At the time they
wrote,it was the "private" in private law that got all the emphasis. Forgotten was the
"law," as if "property"and "contract" existed independent of the state.

The realists' aim was to undermine this view. Contract and property law, they argued, was law that gave private parties power.27 If you breach a contract with me, I
can have the court order the sheriff to force you to pay; the contract gives me access
to the state power of the sheriff. If your contract with your employer says that it may
dismiss you for being late, then the police can be called in to eject you if you refuse
to leave. If your lease forbids you to have cats, then the landlord can use the power
of the courts to evict you if you do not get rid of the cats. These are all instances
where contract and property, however grounded in private action, give a private person an entitlement to the state.

No doubt this power is justified in many cases; to call it "law"is not to call it unjust. The greatest prosperity in history has been created by a system in which private

1 3 1

parties can order their lives freely through contract and property. But whether justified in the main or not, the realists argued that the contours of this "law"should be
architected to benefit society.28

This is not communism. It is not an attack on private property. It is not to say
that the state creates wealth. Put your Ayn Rand away. These are claims about the relationship between private law and public law, and they should be uncontroversial.
Private law creates private rights to the extent that these private rights serve some
collective good. If a private right is harmful to a collective good,then the state has no
reason to create it. The state's interests are general, not particular. It has a reason to
create rights when those rights serve a common, rather than particular, end.

The institution of private property is an application of this point. The state has
an interest in defining rights to private property because private property helps produce a general, and powerful, prosperity. It is a system for ordering economic relations that greatly benefits all members of society. No other system that we have yet
devised better orders economic relations. No other system, some believe, could.29

But even with ordinary property—your car, or your house—property rights are
never absolute. There is no property that does not have to yield at some point to the
interests of the state. Your land may be taken to build a highway, your car seized to
carry an accident victim to the hospital, your driveway crossed by the postman,your
house inspected by health inspectors. In countless ways, the system of property we
call "private property" is a system that balances exclusive control by the individual
against certain common state ends. When the latter conflict with the former, it is the
former that yields.

This balance,the realists argued,is a feature of all property. But it is an especially
i m portant fe a tu re of i n tell ectual property. The balance of ri ghts with intell ectu a l
property differs from the balance with ord i n a ry real or pers onal property. " In formation," as Boyle puts it,"is different."30 And a very obvious feature of intellectual
property shows why.

When property law gives me the exclusive right to use my house, there's a very
good reason for it. If you used my house while I did,I would have less to use. When
the law gives me an exclusive right to my apple, that too makes sense. If you eat my
apple, then I cannot. Your use of my property ordinarily interferes with my use of
my property. Your consumption reduces mine.

The law has a good reason, then, to give me an exclusive right over my personal
and real property. If it did not,I would have little reason to work to produce it.Or if
I did work to produce it, I would then spend a great deal of my time trying to keep
you away. It is better for everyone, the argument goes, if I have an exclusive right to
my (rightly acquired) property, because then I have an incentive to produce it and
not waste all my time t rying to defend it.31

Things are different with intellectual property. If you "take" my idea, I still have
it. If I tell you an idea, you have not deprived me o f it.32 An unavoidable feature of
intellectual property is that its consumption,as the economists like to put it,is "nonrivalrous." Your consumption does not lessen mine. If I write a song, you can sing it

1 3 2

wi t h o ut making it impo s s i ble for me to sing it. If I wri te a boo k , you can re ad it
(please do) without disabling me from reading it. Ideas, at their core, can be shared
with no reduction in the amount the "owner" can consume. This difference is fundamental, and it has been understood since the founding.

Jefferson put it better than I:

If n a tu re has made any one thing less su s cepti ble than all others of exclu s ive
property, it is the action of the thinking power called an idea, which an individual may exclusively possess as long as he keeps it to himself; but the moment it is
divulged,it forces itself into the possession of every one, and the receiver cannot
d i s possess himsel f of i t . Its peculiar ch a racter, too, is that no one possesses the
less, because e very other possess the whole of it. He who receives an idea from
me, receives instruction himself without lessening mine;as he who lights his taper
at mine, receives light wi t h o ut darkening me. That ideas should freely spread ad
f rom one to another over the gl obe , for the moral and mutual instru cti on of
m a n , and improvem ent of his con d i ti on , s eems to have been pec u l i a rly and
benevolently designed by nature, when she made them,like fire, expansible over
all space, without lessening their density at any point,and like the air in which we
breathe, move, and have our physical being, incapable of confinement or exclusive appropriation. Inventions then cannot, in nature, be a subject of property.33

Technically, Jefferson is confusing two different concepts. One is the possibility
of excluding others from using or get ting access to an ide a . This is the qu e s ti on
whether ideas are "excludable"; Jefferson suggests that they are not. The other concept is whether my using an idea lessens your use of the same idea. This is the questi on of wh et h er ideas are "riva l ro u s";3 4 a ga i n , Jef fers on su ggests that they are not.
Jefferson believes that nature has made ideas both nonexcludable and nonrivalrous,
and that there is little that man can do to change this fact.35

But in fact , i deas are not both non exclu d a ble and non riva l ro u s . I can exclu de
people from my ideas or my wri ti n gs—I can keep them sec ret , or build fen ces to
keep people out. How easily, or how effectively, is a technical question. It depends on
the arch i tectu re of pro tecti on that a given con text provi de s . But given the proper
technology, there is no doubt that I can keep people out.

What I cannot do, however, is change the nature of my ideas as "nonrivalrous"
good s . No tech n o l ogy (that we know of) wi ll erase an idea from your head as it
passes into my head. No technology will make it so that I cannot share your ideas
with no harm to you. My knowing what you know does not lessen your knowing of
the same thing. That fact is given in the world,and it is that fact that makes intellectual property different. Unlike apples, and unlike houses, ideas are something I can
take from you without diminishing what you have.

It does not fo ll ow, h owever, that there is no need for property ri ghts over expressions or inventions.36 Just because you can have what I have without lessening

1 3 3

what I have does not mean that the state has no reason to create rights over ideas, or
over the expression of ideas.

If a novelist cannot stop you from copying (rather than buying) her book, then
she has very little incentive to produce more books. She may have as much as she
had before you took the work she produced, but if you take it without paying, she
has no monetary incentive to produce more.

Now in fact, of course, the incentives an author faces are quite complex, and it is
not possible to make simple generalizations about the incentives authors face.37 But
generalizations do not have to be perfect to make a point: even if some authors write
for free,it is still the case that the law needs some intellectual property rights. If the
law did not protect the author at all, there would be fewer authors. The law has a
reason to protect the rights of authors, at least insofar as doing so gives them an in -
centive to produce. With ordinary property, the law must both create an incentive to
produce and protect the right of possession; with intellectual property, the law need
only create the incentive to produce.

This is the difference between these two very different kinds of property, and this
d i f feren ce affects fundamen t a lly the natu re of i n tell ectual property law. While we
pro tect real and pers onal property to pro tect the own er from harm and give the
owner an incentive, we protect intellectual property only to ensure that we create a
sufficient incentive to produce it. "Sufficient incentive," however, is something less
than "perfect control." And in turn we can say that the ideal protections of intellectual property law are something less than the ideal protections for ordinary or real
property.

This difference between the nature of intellectual property and ordinary p roperty was recognized by our Constitution, which in article I,section 8, clause 8, gives
Congress the power "to promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries."

Note the special structure of this clause. First, it sets forth the precise reason for
the power—to promote the progress of science and useful arts. It is for those reasons,and those reasons only, that Congress may grant an exclusive right—otherwise
known as a monopoly. And second, note the special t temporality of this right: "for
limited Times." The Constitution does not allow Congress to g rant authors and inven tors perm a n ent exclu s ive ri ghts to their wri ti n gs and discoveries e s , on ly limited
rights. It does not give Congress the power to give them "property"in their writings
and discoveries, only an exclusive right over them for a limited time.

The Con s ti tuti on's pro tecti on for intell ectual property then is fundamen t a lly
d i f ferent from its pro tecti on of ord i n a ry property. I 've said that all property is
granted subject to the limit of the public good. But even so, if the government decided to nationalize all property after a fifteen-year term of ownership, the Constitution would require it to compensate the owners. By contrast, if Congress set the
copyri ght term at fif teen ye a rs , t h ere would be no claim that the govern m ent pay

1 3 4

compensation after the fifteen years were up. Intellectual property rights are a monopoly that the state gives to producers of intellectual property in exchange for their
producing intellectual property. After a limited time, the product of their work becomes the public 's to use as it wants. This is Communism, at the core of our Constitution's protection of intellectual property. This "property"is not property in the
ordinary sense of that term.

And this is true for reasons better than tradition as well. Economists have long
understood that granting property rights over information is dangerous (to say the
least).38 This is not because of leftist leanings among economists. It is because economists are pragmatists, and their objective in granting any property right is simply
to facilitate production. But there is no way to know, in principle, whether increasing or decreasing the rights granted under intellectual property law will lead to an
increase in the production of intellectual property. The reasons are complex, but the
point is not: increasing intellectual property's protection is not guaranteed to "promote the progress of science and useful arts"—indeed, often doing so will stifle it.

The balance that intell ectual property law trad i ti on a lly stri kes is bet ween the
protections granted the author and the public use or access granted everyone else.
The aim is to give the author sufficient incentive to produce. Built into the law of intellectual property are limits on the power of the author to control use of the ideas
she has created.39

A classic example of these limits and of this public use dimension is the right of
"fair use." Fair use is the right to use copyrighted material, regardless of the wishes
of the owner of that material.A copyright gives the owner certain rights; fair use is
a limitation on those rights. Under the right of fair use, you can criticize this book,
cut sections from it, and reproduce them in an article attacking me. In these ways
and in others, you have the right to use this book independent of how I say it should
be used.

Fair use does not necessarily work against the author's interest—or more accurately, fair use does not necessarily work against the interests of authors as a class.
When fair use protects the right of reviewers to criticize books without the permission of authors, then more critics criticize. And the more criticism there is, the better the inform a ti on is abo ut what books people should buy. And the bet ter the
information is about what to buy, the more people there are who will buy. Authors
as a whole benefit from the system of fair use, even if particular authors do not.

The law of copyright is filled with such rules. Another is the "first sale" doctrine.
If you buy this book, you can sell it to someone else free of any constraint I might
impose on you.40 This d octrine differs from the tradition in, for example, Europe,
where there are "moral rights" that give the creator power over subsequent use.41 I've
already mentioned another example—limited term. The creator cannot extend the
term for which the law will provide protection; that is fixed by the statute and runs
when the statute runs.42

Ta ken toget h er, these rules give the cre a tor significant con trol over the use of
what he produces, but never perfect control. They give the public some access, but

1 3 5

not complete access. They are balanced by design,and different from the balance the
law strikes for ordinary property. They are constitutionally structured to help build
an intellectual and cultural commons.

The law strikes this balance. It is not a balance that would exist in nature. Without the law, and before cyberspace, authors would have very little protection; with
the law, t h ey have sign i f i c a n t , but not perfect , pro tecti on . The law gives aut h ors
something they otherwise would not have in exchange for limits on their rights, secured to benefit the intellectual commons as a whole.

P R I V A T E S U B S T I T U T E S F O R

P U B L I C L A W

But what happens when code protects the interests now protected by copyright law?
What happens when Mark Stefik's vision is realized,and when what the law protects
as intellectual property can be protected through code? Should we expect that any of
the limits will remain? Should we expect code to mirror the limits that the law imposes? Fair use? Limited term? Would private code build these "bugs" into its protections?

The point should be obvi o u s : wh en intell ectual property is pro tected by code ,
nothing requ i res that the same balance be stru ck . Nothing requ i res the own er to
grant the ri ght of fair use. She migh t , just as a boo k s tore all ows indivi duals to
browse for free , but she might not. Wh et h er she grants this ri ght depends on
whether it profits her. Fair use becomes subject to private gain.43

As privatized law, trusted systems regulate in the same domain where copyright
law regulates, but unlike copyright law, they do not guarantee the same public use
protection. Trusted systems give the producer maximum control—admittedly at a
cheaper cost, thus permitting many more authors to publish. But they give authors
more control (either to charge for or limit use) in an area where the law gave less
than perfect control. Code displaces the balance in copyright law and doctrines such
as fair use.

Some wi ll re s pond that I am late to the party: copyri ght law is alre ady bei n g
d i s p l aced , i f not by code then by the priva te law of con tract . Th ro u gh the use of
cl i ck - wra p, or shri n k - wra p, l i cen s e s , a ut h ors are incre a s i n gly demanding that purch a s ers , or licen s ee s , w a ive ri ghts that copyri ght law gave them . If copyri ght law
gives the ri ght to revers e - en gi n eer, t h en these con tracts might ex tract a prom i s e
not to revers e - en gi n eer. If copyri ght law gives the ri ght to dispose of the boo k
h owever the purch a s er wants after the first sale, t h en a con tract might requ i re that
the user waive that ri gh t . And if these terms in the con tract attach ed to every
copyri ght work are en force a ble merely by being "a t t ach ed " and "k n ow a bl e ," t h en
a l re ady we have the abi l i ty to rewrite te the balance that copyri ght law cre a te s . Alre ady, t h ro u gh con tract law, copyri ght holders can defeat the balance that copyri ght law inten d s .

1 3 6

I agree that this race to priva ti ze copyri ght law thro u gh con tract is alre ady far
along, fueled in particular by decisions such as Judge Frank Easterbrook's in ProCD
v Zeidenberg44 and by the efforts in some quarters to push a new uniform code that
would facilitate these contracts.45

But contracts are not as bad as code. Contracts are a form of law. If a term of a
contract is inconsistent with a value of copyright law, you can refuse to obey it and
let the other side get a court to enforce it. The ultimate power of a contract is a decision by a court—to enforce the contract or not. Although courts today are relatively eager to find ways to enforce these contracts, there is at least hope that if the
other side makes its case very clear, courts could shift direction again.46

The same is not true of code. Whatever problems there are when contracts rep l ace copyri ght law, the probl ems are worse wh en code displaces copyri ght law.
Again—where do we challenge the code? When the software protects in a particular
way without relying in the end on the state,where can we challenge the nature of the
protection? Where can we demand balance when the code takes it away?

The rise of contracts modifying copyright law (due in part to the falling costs of
contracting) and the rise of code modifying copyright law (promised as trusted systems become all the more common) raise for us a question that we have not had to
answer before. We have never had to choose whether authors should be permitted
perfectly to control the use of their intellectual property independent of the law, for
su ch con trol could on ly be ach i eved thro u gh law.4 7 The balance stru ck by the law
was the best that aut h ors could get . But now the code gives aut h ors a bet ter de a l .
And thus we must now decide whether this better deal makes public sense.

Some argue that it does, and that this increased power to control use in fact is
not incon s i s tent with fair use.4 8 Fair use, these com m en t a tors argue, def i n ed the
rights in an area where it was not possible to meter and charge for use. In that context,fair use set a default rule that parties could always contract around. The default
rule was that use was free.

But as the limits of what it is possible to meter and charge for changes, the scope
of fair use ch a n ges as well .4 9 If it becomes po s s i ble to license every aspect of u s e ,
t h en no aspect of use would have the pro tecti ons of fair use. Fair use, u n der this
conception, was just the space where it was too expensive to meter use. By eliminating that space , c ybers p ace merely forces us to recogn i ze the ch a n ge in the con tex t
within which fair use functions.

There are then, from this view, two very different conceptions of fair use.50 One
con cepti on vi ews it as inherent in the copyri gh t — requ i red wh et h er tech n o l ogy
makes it possible to take it away or not; the other views it as contingent—needed
where technology makes it necessary. We can choose between these two conceptions,
if indeed our constitutional commitment is ambiguous.

A nice para ll el to this probl em exists in con s ti tuti onal law. The fra m ers gave
Congress the power to regulate interstate commerce and commerce that affects interstate commerce.51 At the founding, that was a lot of commerce, but because of the

1 3 7

inefficiencies of the market,not all of it. Thus,the states had a domain of commerce
that they alone could regulate.52

Over time,however, the scope of interstate commerce has changed so that much
less com m erce is now within the exclu s ive domain of the state s . This ch a n ge has
produced two sorts of responses. One is to find other ways to give states domains of
exclu s ive reg u l a tory aut h ori ty. The ju s ti fic a ti on for this re s ponse is the claim that
these changes in interstate commerce are destroying the framers' vision about state
power.

The other response is to concede the increasing scope of federal authority, but to
deny that it is incon s i s tent with the framing balance .5 3 Cert a i n ly, at the fo u n d i n g,
some commerce was not interstate and did not affect interstate commerce. But that
does not mean that the fra m ers inten ded that there must alw ays be su ch a space .
They tied the scope o f federal power to a moving target; if the target moves completely to the side of federal power, then that is what we should embrace.54

In both con tex t s , the ch a n ge is the same. We start in a place wh ere balance is
given to us by the mix of frictions within a particular regulatory domain: fair use is
a balance given to us because it is too expensive to meter all use; state power over
com m erce is given to us because not all com m erce affects inters t a te com m erce .
When new technology disturbs the balance, we must decide whether the original intent was that there be a balance, or that the scope of one side of each balance should
faithfully track the index to which it was originally tied. Both contexts,in short, present ambiguity.

Many observers (myself included) have strong feelings one way or the other. We
bel i eve this latent ambi g u i ty is not an ambi g u i ty at all . In the con text of federa l
power, we believe either that the states were meant to keep a domain of exclusive authority55 or that the federal government was to have whatever power affected interstate commerce.56 In the context of fair use, we believe that either fair use is to be a
minimum of public use, guaranteed regardless of the technology,57 or that it is just
an inefficient consequence of inefficient technology, to be removed as soon as efficiency can be achieved.58

But in both cases, this may make the problem too easy. The best answer in both
con texts may be that the qu e s ti on was unre s o lved at the ti m e : perhaps no on e
t h o u ght of the matter, and hen ce there is no answer to the qu e s ti on of what they
would have intended if some central presupposition had changed. And if there was
no original answer, we must decide the question by our own lights. As Stefik says of
trusted systems—and, we might expect, of the implications of trusted systems—"It
is a tool never imagined by the creators of copyright law, or by those who believe
laws governing intellectual property cannot be enforced."59

The loss of fair use is a con s equ en ce of the perfecti on of tru s ted sys tem s .
Whether you consider it a problem or not depends on your view of the value of fair
use. If you consider it a public value that should exist regardless of the technological
regime, then the emergence of this perfection should trouble you. From your per-

1 3 8

spective, there was a value latent in the imperfection of the old system that has now
been erased.

But even if you do not think that the loss of fair use is a problem, trusted systems
threaten other values latent in the imperfection of the real world. Consider now a
second.

T H E A N O N Y M I T Y T H A T I M P E R F E C T I O N

A L L O W S

I was a student in England for a number of years,at an English university. In the college I attended,there was a "buttery"—a shop that basically sold alcohol. During the
first week I was there I had to buy a large amount of Scotch (a series of unimaginative gifts, as I remember). About a week after I made these purchases, I received a
summons from my tutor to come talk with him in his office. When I arrived, the tutor asked me about my purchases. This was, to his mind,an excessive amount of alcohol,and he wanted to know whether I had a good reason for buying it.

Needless to say, I was shocked at the question. Of course, formally, I had made a
purchase at the college,and I had not hidden my name when I did so (indeed, I had
charged it on my college account), so formally, I had revealed to the college and its
a gents my alcohol purch a s e s . S ti ll , it shocked me that this inform a ti on would be
monitored by college authorities and then checked up on. I could see why they did
it, and I could see the good that might come from it. It just never would have occurred to me that this data would be used in this way.

If this is an invasion, of course it is a small one. Later it was easy for me to hide
my bi n ges simply by buying from a local store ra t h er than the co ll ege but tery.
(Though I later learned that the local store rented its space from the college,so who
knows what deal they had struck.) And in any case, I was not being punished. The
college was just concerned. But the example suggests a more general point: we reveal
to the world a certain class of data abo ut ours elves that we ord i n a ri ly ex pect the
world not to use.

Trusted systems depend on such data—they depend on the ability to know how
people use the property that is being protected. To set prices most efficiently, the system ideally should know as much about individuals and their reading habits as possible. It needs to know this data because it needs an efficient way to track use and so
to charge for it.60

But this tracking involves a certain invasion. We live now in a world where we
think about what we read in just the way that I thought about what I bought as a
student in England—we do not expect that anyone is keeping t rack. We would be
s h ocked if we learn ed that the libra ry was keeping tabs on the books that peop l e
checked out and then using this data in some monitoring way.

Such tracking, however, is just what trusted systems require. And so the question
becomes: Should there be a right against this kind of monitoring? The question is

1 3 9

parallel to the question of fair use. In a world where this monitoring could not effectively occur, there was, of course, no such right against it. But now that monitoring can occur, we must ask whether the latent right to read anonymously, given to us
before by imperfections in technologies, should be a legally protected right.

Julie Cohen argues that it should, and we can see quite directly how her argument proceeds.61 Whatever its source, it is a value in this world that we can explore
intellectually on our own. It is a value that we can read anonymously, without fear
that others will know or watch or change their behavior based on what we read.This
is an element of intellectual freedom. It is a part of what makes us as we are.62

Yet this element is potentially erased by trusted systems. These systems need to
monitor, and this monitoring destroys anonymity. We need to decide whether, and
how, to preserve values from today in a context of trusted systems.

This is a matter of translation.63 The question is, how should changes in technology be accommodated to preserve values from an earlier context in a new context? It is the same qu e s ti on that Bra n deis asked abo ut wi ret a pp i n g.6 4 It is the
question the Court answers in scores of contexts all the time. It is fundamentally a
question about preserving values when contexts change.

In the context of both fair use and reading, Cohen has a consistent answer to this
question of translation. She argues that there is a right to resist, or "hack," trusted
systems to the extent that they infringe on traditional fair use. (Others have called
this the "Cohen Theorem.") As for reading, she argues that copyright management
schemes must protect a right to read anonymously—that if they monitor, they must
be con s tru cted so that they pre s erve anonym i ty. The stra tegy is the same: Co h en
identifies a value yielded by an old architecture but now threatened by a new architecture,and then argues in favor of an affirmative right to protect the original value.

T H E P R O B L E M S T H A T P E R F E C T I O N M A K E S

These two examples reveal a com m on probl em — one that wi ll re ach far beyond d
copyright. At one time we enjoy a certain kind of liberty, but that liberty comes from
the high costs of control.65 That was the conclusion we drew about fair use—that
wh en the cost of con trol was high , the space for fair use was gre a t . So too wi t h
anonymous reading: we read anonymously in real space not so much because laws
protect that right as because the cost of tracking what we read is so great.

When those costs fall,the liberty is threatened. That threat requires a choice—do
we allow the erosion, or do we erect other limits to re-create the original space for
liberty?

The law of intellectual property is the first example of this general point. The architectures of property will change; they will allow for a greater protection for intell ectual property than re a l - s p ace arch i tectu res all owed ; and this gre a ter pro tecti on
will force a choice on us that we do not need to make in real space. Should the architecture allow perfect control over intellectual property, or should we build into

1 4 0

the architecture an incompleteness that guarantees a certain aspect of public use? Or
a certain space for individual freedom?

Ign oring these qu e s ti ons wi ll not make them go aw ay. Pretending that the
framers answered them is no solution either. In this context (and this is just the first)
we will need to make a judgment about which values the architecture will protect.

C H O I C E S

I've argued that cyberspace will open up at least two important choices in the context of intellectual property: whether to allow intellectual property in effect to become completely propertized (for that is what a perfect code regime for protecting
i n tell ectual property would do ) , and wh et h er to all ow this regime to erase the
a n onym i ty latent in less ef fic i ent arch i tectu res of con tro l . These ch oi ces were not
made by our framers. They are for us to make now.

I have a view, in this context as in the following three, about how we should exercise that ch oi ce . But I am a law yer, tra i n ed to be shy abo ut saying "h ow things
ought to be." Lawyers are taught to point elsewhere—to the framers, to the United
Nations charter, to an act of Congress—when arguing about how things ought to be.
Having said that there is no such authority here, I feel as if I ought therefore to be
silent.

Cowardly, not silent, however, is how others might see it. I should say, they say,
what I think. So in each of these four applications (intellectual property, privacy, free
s peech , and soverei gn ty ) , I wi ll of fer my vi ew abo ut how these ch oi ces should be
made. But I do this under some duress and encourage you to simply ignore what I
believe. It will be short, and summary, and easy to discard. It is the balance of the
book—and, most importantly, the claim that we have a choice to make—that I really want to stick.

A n o n y m i t y

Cohen,it seems to me,is plainly right about anonymity, and the Cohen Theorem inspirational. However efficient the alternative may be, we should certainly architect
c ybers p aces to en su re anonym i ty — or more prec i s ely, p s eu donym i ty — f i rs t . If t h e
code is going to monitor just what I do, then at least it should not know that it is "I"
that it is monitoring. I am less troubled if it knows that "14AH342BD7" read such
and such; I am deeply troubled if that number is tied back to my name.

Co h en is plainly ri ght for a second re a s on as well : a ll of the good that com e s
from monitoring could be achieved while protecting privacy as well. It may take a
bit more coding to build in routines for breaking traceability; it may take more planning to ensure that privacy is protected. But if those rules are embedded up front,
the cost would not be terribly high. Far cheaper to architect privacy protections in
now rather than retrofit for them later.

1 4 1

T h e C o m m o n s

An intellectual commons I feel much more strongly about.

We can architect cy berspace to preserve a commons or not. (Jefferson thought
that nature had already done the architecting, but Jefferson wrote before there was
code.66) We should choose to architect it with a commons.Our past had a commons
that could not be designed away; that commons gave our culture great value. What
value the commons of the future could bring us is something we are just beginning
to see. Intellectual property scholars saw it—long before cyberspace came along—
and laid the gro u n dwork for mu ch of the argument we need to have now.6 7 Th e
gre a test work in the law of c ybers p ace has been wri t ten in the field of i n tell ectu a l
property. In a wide range of contexts, these scholars have made a powerful case f or
the substantive value of an intellectual commons.68

James Boyle puts the case most dramatically in his extraordinary book Shamans,
Software,and Spleens.69 Drawing together both cyberspace and noncyberspace questions,he spells out the challenge we face in an information society—and particularly
the political challenge we face.70 Elsewhere he identifies our need for an "environm ental movem en t" in inform a ti on policy—a rh etoric that gets people to see the
broad range of values put at risk by this movement to propertize all information.71
We are far from that understanding just now, and this book, on its own, won't get
us much closer. It is all that I can do here to point to the choice we will have to make,
and hint, as I have, about a direction.

E L E V E N

p r i v a c y

Th e c conclusion conclusion o f par t 1 was t h at code coul d enabl e a mor e r egul abl e cyberspace and that this is cause for concern. The conclusion of the last chapter was
that code could enable a more regulable regime of intellectual property, and again,
that this is cause for concern. In both cases, code resets a traditional balance between
freedom and constraint, and we need to ask whether the new balance is consistent
with our tradition or with how we want the space to be.

With "privacy," the story is a bit different. Here the code has already upset a traditional balance. It has already changed the control that individuals have over facts
a bo ut their priva te live s . The qu e s ti on now is: Could code re - c re a te som ething of
that traditional balance? I argue that it can.1

There's a story from early MUD history that will introduce this debate about privacy.2 You recall that MUDs are text-based virtual realities where people build characters and those ch a racters come to repre s ent who their cre a tors are . In the early
history of MUDs the community of MUDers was relatively small, and certain characters became well known ac ross MUD com mu n i ti e s . Famous ch a racters bec a m e
known to everyone.

There is a behavior in MUDs and MOOs called "tinySex"—text-based virtual sex
in which (at least) two people talk through a sexual encounter. Sometimes this talking is just talk. Sometimes something more is going on. But in any case, tinySex is a
significant part of the history of MUDs, as its cognates are in other parts of cyberspace and in real space as well.3

In an early and prominent MUD, there appeared a character who was particularly interested in tinySex, and especially in tinySex with famous MUD characters.
This character (a man in real space) "was" a woman, and he proceeded to "seduce"
( ti ny Sedu ce?) a string of famous ch a racters . O f f t h ey would go to some "priva te
room" and engage in a tinySex affair. Many famous MUDers were seduced by this
character, who engaged in quite a bit of tinySex.

1 4 3

We know this because the character recorded these tinySex t trysts, both the sedu cti on and the sex that fo ll owed . Af ter co ll ecting a large nu m ber of vi cti m s , h e
posted the recordings. Now sitting in the MUD space of this previously flourishing
community were the transcripts of sexual encounters by some of the most prominent members of the community. All Monica,all the time, but long before any Monica existed.

Now of co u rs e , t h ere have alw ays been affairs . People have alw ays raced of f to
s ome corn er to en ga ge in sex , wh et h er ti ny or not. And there have alw ays been
people who just love to kiss and tell . But ra t h er than the similarities ti e s , think abo ut
s ome of the differen ce s . It is not just the fact that an affair has occ u rred , but that
every twist of the event is replayed. And it is not just that a recording exists, but that
this "recording" is posted in a prominent and searchable space. The private goings-on were monitored, in a space that makes monitoring extremely easy. The product
of this mon i toring is then search a ble—the de s i gn makes that easy as well . Every
move is captured; only some are discarded;the rest remain out there to be searched.
This event de s troyed this MUD com mu n i ty. People could not qu i te face each
other in the same way again. They moved on, took different characters, or left MUD
space entirely. No laws had been broken, but the space was destroyed.

And so it should be , you might be tem pted to say. Perhaps it is best that a bit of
l i ght flu s h ed out this sort of "devi a n t" beh avi or, that we live in a world wh ere our acti ons accord with our word s , wh ere we are who we seem to be . Perhaps we are bet ter
of f l iving in su ch a worl d , and maybe it is good that cybers p ace makes this po s s i bl e .

Th ere is a part of a anyone e's life that is m o n i to red , and there is a part that can be
searched. The monitored is that part of one's daily existence that others see or notice
and that others can respond to, if response is appropriate. As I walk down the street,
my behavior is monitored. If I walked down the street in a small village in western
China, my behavior would be monitored quite extensively. This monitoring in both
cases would be transitory. People would notice, for example, if I were walking with
an elephant or walking in a dress, but if there were nothing sp special about my walk,
if I simply blended into the crowd, then I might be noticed for the moment but forgotten soon after—more quickly in Cambridge, perhaps, than in China.

The searchable is the part of your life that leaves, or is, a record. Scribblings in
your diary leave a record of your thoughts. Stuff in your house is a record of what
you possess. The recordings on your telephone answering machine are a record of
who called and what they said. These parts of your life are not so ephemeral. They
instead remain to be reviewed—if technology and the law permit.

Privacy, as Ethan Katsh defines it, is the power to control what others can come
to know about you. 4 People gain knowledge about you in only two ways—through
m on i toring or searching (or by reports relying on the re sults of m on i toring and
searching). One can do little about gossip, and the law can do little about reporting.
So to understand the real privacy that you have , we must understand som et h i n g
about these two ideas of monitoring and searching. What are the constraints in real

1 4 4

space on others' ability to monitor and search,and how do those constraints change
as we move to cyberspace?

I begin by examining these two qu e s ti ons sep a ra tely, m a rking out the ch a n ge s
that cybers p ace might bring and iden ti f ying the latent ambi g u i ties that these
changes reveal.5 Then,as in the last chapter, I will consider arguments on both sides
of these ambiguities. Again, in the end I will push one side. But whether you accept
my position is not as important to me as whether you accept the idea that an argument for a position is required. Here too we do not have a decision of the framers to
follow. We must make our own.

S P A C E S P R O T E C T E D B Y L A W

Recall the worm from the start of this book:a bit of code works itself onto your machine, scans your disk, and reports back to some central place facts about your mach i n e . " Ill egal copy of Word 98," or, " Mu l tiple copies of Now Uti l i ti e s ," or, " N S A
Document 5G67K13"—such facts are reported if they are true; nothing is reported
if they are not.

This example may have seemed oddly removed from the mainstream of privacy
issues. After all, we do not really think the government has a set of worms working
themselves across the Net, spying on people (though it is alleged by some that the
NSA installs sniffers at various network switches).

But whether or not the specifics of the example convince you, the general form
should. We can imagine a host of contexts where the burdens of a search have been
el i m i n a ted and its perfecti on incre a s ed , and wh ere the con s ti tuti onal qu e s ti on
raised by the search is thus made all the more difficult.

In each of these contexts, the same question presents itself: Is the constitutional
value a protection against unjustified burdens imposed by the state, or is it a substantive value of privacy? When the burden decreases, does the protected privacy decrease? Is the protection against state trespass or against incursions into a particular
space? This is the same question that Louis Brandeis and William Howard Taft confronted in the wiretapping case of 1928.6 It is a question we must now ask in an increasingly large range of our own private lives.

I consider some of that range in the section that follows. My aim is to explore the
co n s ti tu ti o n a l qu e s ti on that this ch a n ge pre s en t s ; I am not talking abo ut statutory
protections, which are in fact quite rich. My question is: What would the Constitution protect absent the protections of a statute?7

I am also not considering any technological steps that the individual might take

to protect privacy on her own.I consider that in a section that follows.

E-mail

Electronic mail is a text-based message stored in digital form. It is like a transcribed telephone call. When sent from one person to another, e-mail is copied and

1 4 5

transmitted from machine to machine; it sits on these different machines until removed either by routines—decisions by machines—or by people.

The con tent of m a ny e-mail messages is like the con tent of an ord i n a ry tel eph one call — u n p l a n n ed , u n t h i n k i n g, the ord i n a ry ch a t ter of f ri en d s . But unlike a
tel eph one call , this con tent is saved , and on ce saved , it is mon i tora bl e , a rch iva bl e ,
and searchable. Companies can build routines that watch the interactions between
employees, that watch what is said to others, and that collect and organize what is
said, to be used as the company sees fit.

Can,and do. The single greatest invasion of any sensible space of privacy that cyberspace has produced is the extraordinary monitoring of employees in which corpora ti ons now en ga ge . On the theory that they "own the com p uter," em p l employers
i n c re a s i n gly snoop in the e-mail of em p l oyee s , l ooking for stu f f t h ey deem improper.

To be su re , in pri n c i p l e , su ch mon i toring and searching are po s s i ble with tel eph one calls or let ters . But in practi ce ,t h ey are not. To mon i tor tel eph ones or reg u l a r
mail requ i res time and mon ey—that is, human interven ti on . And this cost means
that most won't do it. Here aga i n , the costs of con trol yi eld a certain kind of f reedom .
This freedom is redu ced as the costs of s e a searching fall . More con tent can be
searched without imposing any burden on the target of the search. Should protections against searching therefore fall as well?

V-mail

If e-mail, why not v-mail? Voice mail systems archive messages and record the
communication attributes of the conversations.8 As technologies for voice recogniti on improve , so does the abi l i ty to search voi ce record s . These records exist in
archives and could be searched, just as the NSA scans international telephone calls,
for example.9 And thus, we could well imagine technologies that would allow us to
scan v-mail, looking for key words or topics and pulling out from a general archive
only those keys.

This search would also impose no bu rden on the user. It could be targeted on
and limited to sp specific topics, and it could operate in the background without anyone ever knowing. Does a constitutional privacy speak to these practices?

Video

A pictu re might be worth a thousand word s , but Hewl et t - Pack a rd has found a
w ay to repre s ent a face in less than a hu n d red byte s .1 0 A face can be captu red ,
s tored , and match ed against vi deo arch ives of l oc a ti on s . Hewl et t - Pack a rd estimates a tes that even at one hu n d red ya rds its tech n o l ogies could iden tify the face in a
vi deo t a pe . Using vi deo cameras loc a ted around a city, the govern m ent could begi n
to mon i tor wh ere people go by attem pting to iden tify the people captu red by the
c a m era s .

But that is the future. Even now video technologies are used to identify license
plates in the Channel Tunnel11 or vehicles entering airport parking garages. 12 Using

1 4 6

these tech n o l ogi e s , and others , it wi ll become incre a s i n gly easy to mon i tor movements in public.

Telephones

Cell phones need to locate themselves so that transmitters can follow the caller
as she moves from one zone to another. These data about location are collected by
s ys tems that servi ce the call . But obvi o u s ly these data could be put to other uses,
su ch as mon i toring and track i n g. And as I de s c ri bed in ch a pter 5, the FBI is now
pushing for this data to be made readily available so that the government, if it wants,
can track who it wants.

Of course, the FBI justifies such tracking not by arguing that it wants the ability
to spy but by citing public safety reasons. If we could track your cell phone's location, the argument goes, then when you call 911, it would be easier for emergency
relief services to be dispatched to find you. True enough, though of course, the system could also be programmed to report locations only when 911 was dialed. The
FBI, not surprisingly, overlooked that possibility.13

In each case, there is a question about whether to protect the space against invasions i ons by the govern m ent (the con s ti tuti onal qu e s ti on ) . Tex tu a lly, the Con s ti tuti on
seems to require that we answer that question by asking what is "reasonable." Historically, we have determined what is reasonable by weighing the burdens,taking the
technologies that produce them for granted. It was a given that searching a house is
invasive, and a given that listening to phone calls is too expensive. These givens have
governed what kind of privacy seemed reasonable. We took the world as we found
it, and then built our privacy around that.

But in the digital world these burdens are not givens. Burdens are determined by
the architectures of the spa ce, and these architectures are plastic. If the protection
turns on how burdensome a search is,then we can design the space to eliminate the
burden. And if we do that,then the question rightly becomes whether the protection
for privacy is eliminated as well.

The answer to that question depends, of course, on the conception of privacy at
s t a ke . The kind of privacy I have spo ken of a l re ady—as a way to minimize intrusion—is only the first of at least three conceptions.

P r i v a c y t o M i n i m i z e B u r d e n

The first conception, which we could call the utility conception, seeks to minimize
i n tru s i on . We want to be left alon e , not interfered wi t h , not tro u bl ed . And so we
want a pro tecti on that minimizes the ex tent to wh i ch tra n qu i ll i ty is disturbance rbed .
Sometimes the state will have reason to search us or to interfere with our peace. But
we want this interference ce kept at a minimu m . The test then is the bu rden of t h e
state's intervention; when an intervention can be made less burdensome,the protection against it decreases as well.

1 4 7

P r i v a c y a s D i g n i t y

The second conception tracks dignity. Even if a search does not bother you at all, or
even if you do not notice the search, this conception of privacy holds that the very
idea of a search of your possessions is an offense to your dignity. From this perspective , i f the state wants to search your house, it had bet ter have a good re a s on . It s
search harms your dignity whether it interferes with your life or not.

I saw these two conceptions of privacy play out against each other in a tragically
common encounter in Washington, D.C.A friend and I had arranged a "police ridealong"—riding with District police during their ordinary patrol. The neighborhood
we patrolled was among the poorest in the city, and around 11:00 P.M. a report came
in that a car alarm had been tripped in a location close to ours. When we arrived
near the scene,at least five police officers were attempting to hold three youths; three
of the officers were holding the suspects flat against the wall, with their legs spread
and their faces pressed against the brick.

These three were "suspects"—they were near a car alarm when it went off—and
yet,from the looks of things, you would have thought they had been caught holding
the Hope diamond.

And then an ex tra ord i n a ry disru pti on bro ke out . To the su rprise of everyon e ,
and to my terror (for this seem ed a ti n der box , and what I am abo ut to de s c ri be
seemed a match), one of the three youths, no older than seventeen, turned around
in a fit of anger and started screaming at the cops."Every time anything happens in
this neighborhood, I get thrown against the wall,and a gun pushed against my head.
I 've never done anything ill ega l , but I'm con s t a n t ly being pushed around by cop s
with guns."

His fri end then tu rn ed around and tri ed to calm him down . "Cool it, m a n ,
they're just trying to do their job. It'll be over in a minute, and e verything will be
cool."

" I 'm not going to cool it. Why the fuck do I have to live this way? I am not a
criminal. I don't deserve to be treated like this. Someday one of these guns is going
to go off by accident—and then I'll be a fucking statistic. What then?"

At this point the cops interven ed , t h ree of t h em flipping the indignant yo ut h
around against the wall, his face again flat against the brick. "This will be over in a
minute. If you check out, you'll be free to go. Just relax."

In the voi ce of ra ge of the first yo uth was the claim of d i gn i ty den i ed . Wh et h er
re a s on a ble or not, wh et h er minimally intru s ive or not, t h ere was som ething insu l ting abo ut this ex peri en ce — a ll the more insu l ting wh en repe a ted , one imagi n e s ,
over and over aga i n . I was rem i n ded of an op i n i on by Ju s ti ce Scalia (an odd assoc ia ti on , I re a l i ze , but I had worked for the man), who won dered wh et h er the fra m ers
of the Con s ti tuti on would have con s i dered con s ti tuti onal the po l i ce practi ce
k n own as a "Terry stop" — s topping and frisking any indivi dual wh en ever the po l i ce
h ave a re a s on a ble su s p i c i on . As Ju s ti ce Scalia wro te : "I fra n k ly do u bt . . . wh et h er

1 4 8

the fiercely proud men who adopted our Fo u rth Am en d m ent would have all owed
t h em s elves to be su bj ected , on mere su s p i ci o n of being arm ed and dangero u s , to
su ch indignity i ty."1 4

And yet, on the other hand, there is the argument of minimal intrusion. If privacy is a protection against unjustified and excessive disruption,then this was no invasion of privacy. As the second youth argued, the intrusion was minimal; it would
pass quickly (as it did—five minutes later, after their identification checked out, we
had left); and it was reasonably related to some legitimate end. Privacy here is simply the protection against unreasonable and burdensome intrusions,and this search,
the second youth argued, was not so unreasonable and burdensome as to justify the
fit of anger (which also risked a much greater danger).

P r i v a c y a s S u b s t a n t i v e

These two conceptions of privacy, however, are distinct from a third, which is about
n ei t h er pre s erving dign i ty nor minimizing intru s i on but inste ad is su b s t a n tive —
privacy as a way to con s train the power of the state to reg u l a te . Here the work of
William Stuntz is a guide.15 Stuntz argues that the real purpose of the Fourth and
Fifth Am en d m ents is to make some types of reg u l a ti on too difficult to ef fect by
making the evidence needed to prosecute violations unavailable.

This is a hard idea for us to imagine, for in our world the sources of evidence are
m a ny — c redit card record s , tel eph one record s , vi deo cameras at 7-Eleven s , and so
on. But put yourself back two hundred years, when the only real evidence was testimony and things. Imagine that in that time the state wanted to punish you for "sedition on ." The on ly good evi den ce of s ed i ti on would be your wri ti n gs or your own
testimony about your thoughts. If those two sources were eliminated,then it would
be practically impossible to prosecute sedition successfully.

As Stuntz argues, this is just what the Fourth and Fifth Amendments do. Combi n ed , t h ey make co ll ecting the evi den ce for a crime like sed i ti on impo s s i bl e ,
thereby making a crime like sedition impossible. And not just sedition—as Stuntz
a r g u e s , the ef fect of the Fo u rt h , F i f t h , and Sixth Am en d m ents was to re s tri ct the
scope of regulation that was practically possible. As he captures the idea: "Just as a
law banning the use of contraceptives would tend to encourage bedroom searches,
so also would a ban on bedroom searches tend to discourage laws prohibiting contraceptives."16

But were not such searches already restricted by, for example, the First Amendment? Would not a law punishing seditious libel have been unconstitutional in any
case? In fact, it was not clear at the founding; indeed, it was so unclear that in 1798
Congress passed the Alien and Sedition Acts, which in effect punished sedition quite
d i rect ly.1 7 Ma ny thought these laws uncon s ti tuti on a l . But the Fo u rth and Fifth
Am en d m ents would have been ef fective limits on their en forcem en t , wh et h er the
substantive laws were constitutional or not.

1 4 9

On this conception, privacy is a substantive limit on government's power.18 As a
restriction on the power of government to enforce certain laws, it provides a subs t a n tive limit on the kinds of reg u l a ti on that govern m ent can ef fectively impo s e .
Understood this way, privacy does more than protect dignity or limit intrusion; privacy limits what government can do.

C h o o s i n g a C o n c e p t i o n o f P r i v a c y

In principle,these three distinct conceptions of privacy could yield different results
depending on the case.A search, for example, might not be intrusive but might offend dignity. In that case, we would have to choose a conception of privacy that we
believed best captured the Constitution's protection.

At the time of the fo u n d i n g, h owever, these different con cepti ons of privac y
prob a bly would not, for the most part , h ave yi el ded different con clu s i on s . Any
search that reached beyond the substantive limits of the amendment, or beyond the
limits of dignity, would also have been a disturbance. Half of the framers could have
held the dignity conception and half the utility conception, but because every search
would have invo lved a vi o l a ti on of bo t h , a ll the fra m ers could have en dors ed the
protections of the Fourth Amendment.

Today, however, these three conceptions could yield different results. The utility
con cepti on could permit ef f i c i ent searches that are forbidden d den by the dign i ty and
substantive conceptions. The correct translation (as Brandeis employed the term in
the O l m s te a d wi ret a pping case) depends on sel ecting the proper con cepti on to
translate.

In this sen s e , our ori ginal pro tecti ons were the produ ct of what Cass Su n s tei n
c a lls an " i n com p l etely theori zed agreem en t ."1 9 G iven the tech n o l ogy of the ti m e ,
there was no reason to work out which theory underlay the constitutional text; all
three were consistent with existing technology. But as the technology has changed,
the original context has been challenged. Now that technologies such as the worm
can search without disturbing, there is a conflict about what the Fourth Amendment
protects.

This con fli ct is the other side of Su n s tei n's incom p l etely theori zed agreem en t .
We might say that in any incompletely theorized agreement ambiguities will be latent, and we can describe contexts where these latencies emerge. The latent ambiguities about the protection of privacy, for example, are being rendered patent by the
evolution of technology. And this in turn forces us to choose.

Some wi ll on ce again try to su ggest that the ch oi ce has been made — by our
Con s ti tuti on , in our past. This is the rh etoric of mu ch of our con s ti tuti onal juri s pru den ce , but it is not very hel helpful here . I do not think the fra m ers worked out
what the amen d m ent would pro tect in a world wh ere perfect ly non i nva s ive
s e a rches could be con du cted . Th ey did not establish a con s ti tuti on to app ly in all
po s s i ble worl d s . Th ey establ i s h ed a con s ti tuti on for their worl d . Wh en their worl d

1 5 0

d i f fers from ours in a way that reveals a ch oi ce they did not have to make , t h en we
n eed to make that ch oi ce .2 0

C O N T R O L L E D U S E

Two years ago I received in my mailbox a letter from AT&T. It was addressed to an
old gi rl f ri en d , but the let ter had not been forw a rded . The ad d ress was my then -
current apartment. AT&T wanted to offer her a new credit card. They were a bit late:
she and I had broken up eight years before. Since then,she had moved to Texas, and
I had moved to Chicago, to Washington,back to Chicago, on to New Haven, back to
Chicago, and finally to Boston, where I had moved twice. My peripateticism, however, did not deter AT & T. With great faith in my con s t a n c y, it bel i eved that livi n g
with me in this apar tment was a woman I had not even seen in three years.

How did AT&T maintain such a belief? Well, floating about in cyberspace is lots
of data about me. It has been collected ever since I began using credit cards, telephones, and who knows what else. The system continuously tries to update and refine this extraordinary data set—that is, it profiles who I am and, using that profile,
determines how it will interact with me.

What exactly should we think about this constant electronic monitoring?21
The lawyer's unthinking response might be this: it has always been possible for
people to be monitored and profiled. Governments do it all the time; so do corporations. More important, so do small communities. Not long ago most people lived
in communities that constantly monitored everyone's behavior. Your comings and
goings, who you were with, how much you spent at the market—all this was known
by your neighbors, nosey or not. There may have been no video camera wat ching
you wh en you went to the market to buy groceries e s . But som ething wors e — yo u r
neighbors—did. They saw when you went, and with whom, and they, unlike video
cameras, could gossip. So what we have now is just the same as what we had then.
Maybe more entities are able to monitor, and maybe more activity is monitored. But
the fact that monitoring goes on has not changed at all.

This type of a r g u m ent is ubi qu i tous in law — " i t's the same sort of thing as in
1791, so nothing is different"—and as an argument it is universally bad. The question is not whether there was something the n like what happens now. The question
is whether what happens now is substantially different. (A tiger is like a kitten, but
unlike a kitten a tiger is not a pet.) I f it is different, then we must ask whether we
ought to treat it differently.

The monitoring of modern life is indeed different in substance from the monitoring at the time of the founding. There is no doubt that life then was monitored,
that it was hard to hide yourself from others, but that monitoring was different. It
was done by people whose memories were imperfect and who were likely to notice
on ly beh avi or out of the ord i n a ry. These mem ori e s , m oreover, could not be
s e a rch ed , or co ll ected , or produ ced as record s . A priva te eye might interview ew the

1 5 1

neighbors to learn what they saw, but as any investigator knows, what people saw is
an extraordinarily imperfect record of what a ctually happened. Gossipy neighbors
might have watched, but their watching produced nothing as lasting or as reliable as
videotape, a toll booth's electronic records of when you entered and when you left,
a credit card sys tem's en endless co ll ecti on of data abo ut your purch a s e s , or the tel telephone system's records of who you called when and for how long.

Tod ay 's mon i toring is different because the tech n o l ogies of m on i tori n g — t h ei r
efficiency and their power—are different. In the 1790s the technology was humans;
now it is machines. Then the technology noticed only what was different;now it noti ces any tra n s acti on . Th en the default was that search a ble records were not co collected; now the default is that all monitoring produces searchable records.

These differen ces add up.2 2 Toget h er they con s ti tute mon i toring of po ten ti a lly
far gre a ter sign i f i c a n ce . What ex act ly is the threat po s ed by this gre a ter mon i tori n g ? Why is it tro u bling if a ll the inform a ti on in the world abo ut me is co ll ected ?
What po s s i ble harm could it do to me—assuming (and of co u rse you should assume this) that I have done nothing bad? What are the con s equ en ces of a perfect ly
m on i tora ble worl d ?

I am con s i dering here on ly co ll ecting that is perfect ly lega l . I am not talking
about breaking into someone's house and reading her diary, or stealing information
from bank records.I am not discussing invasions of privacy in the traditional sense.
My focus here is on the data co ll ected abo ut an indivi dual in day - to - d ay interactions,data that an individual,in a sense,displays to the world. What could be wrong
with collecting what is publicly displayed?

Arguments rage on both sides of this question, one side arguing that there is no

harm from this sort of monitoring, the other side arguing the opposite.

The latter argument assumes that the balance of privacy is stru ck at the line
where you reveal information about yourself to the public. Sure, information kept
behind closed doors, or written in a private diary y, should be protected by the law.
But when you go out in public, when you make transactions there or send material
t h ere , you give up any ri ght to privac y. Ot h ers now have the ri ght to co ll ect data
about your public behavior and do with it what it suits them to do.23

Why is that idea not troubling to these theorists? The reasons are many:

• F i rs t , the harm is actu a lly not very gre a t . You get a discount card at your loc a l
grocery store ; the store then co ll ects data abo ut what you buy. With that data,
the store may market different goods to you or fig u re out how bet ter to pri ce its
produ ct s ; it may even dec i de that it should of fer different mixes of d i s counts to
bet ter serve custom ers . These re s pon s e s , the argument goe s ,a re the likely on e s ,
because the store's business is on ly to sell groceries more ef fic i en t ly.
Second, it is an unfair burden to force others to ignore what you show them.
If data about you are not usable by others, then it is as if you were requiring
o t h ers to discard what you have depo s i ted on their land. If you do not like
others using information about you, do not put it in their hands.

•

1 5 2

• Third,these data actually do some good.I do not know why Nike thinks I am
a good person to tell about their latest sneakers, and I do not know why Keds
does not know to call. In both cases, I suspect the reason is bad data about
me. I would love it if Nike knew enough to leave me alone. And if these data
were better collected and sorted, it would.

• Finally, no one spends money collecting these data to a ctually learn anything
about you. They want to learn about people like you. They want to know your
type. In principle,they would be happy to know your type even if they could
not then learn who you are. What the merchants want is a way to discriminate a te — on ly in the sense of being able to tell the differen ce bet ween so rt s of
people.

The other side of this argument,however, also has a point.24 It begins,as we have
done elsewhere, by noticing the values that were originally protected by the imperfecti on of m on i toring tech n o l ogy. This imperfecti on hel ped pre s erve import a n t
su b s t a n tive va lu e s . One su ch va lue is the ben efit of i n n ocen ce . At any given ti m e ,
there are innocent facts about you that may appear, in a particular context or to a
p a rticular set , g u i l ty. Peter Lewis s , in a New Yo rk Ti m e s a rti cle call ed " For get Bi g
Brother," puts the point well:

Su rvei ll a n ce cameras fo ll owed the attractive young bl ond woman thro u gh the
lobby of the midtown Manhattan hotel, kept a glassy eye on her as she rode the
elevator up to the 23rd floor and peered discreetly down the hall as she knocked
at the door to my room.I have not seen the videotapes, but I can imagine the digital readout superimposed on the scenes,noting the exact time of the encounter.
That would come in handy if someone were to question later why this woman,
who is not my wife,was visiting my hotel room during a recent business trip. The
c a m eras later saw us heading of f to dinner and to the theater—a middle aged ,
married man from Texas with his arm around a pretty East Village woman young
enough to be his daughter.

"As a matter of fact," Lewis writes, "she is my daughter."25
One lesson of the story is the burden of these monitored facts. The burden is on
you, the monitored, first to establish your innocence, and second, to assure all who
might see these ambiguous facts that you are innocent. Both processes, however, are
imperfect; say what you want, doubts will remain. There are always some who will
not believe your plea of innocence.

Modern mon i toring on ly ex exacerbates a tes this probl em . Your life becomes an everincreasing record; your actions are forever held in storage, open to being revealed at
any time, and therefore at any time demanding a justification.

A second value follows directly from this modern capacity for archiving data. We
all desire to live in separate communities, or among or within separate normative
spaces. Privacy, or the ability to control data about yourself, supports this desire. It

1 5 3

enables these multiple communities and disables the power of one dominant community to norm others into oblivion. Think, for example,about a gay man in an intolerant small town.

The point comes thro u gh most cl e a rly wh en con tra s ted with an argument recently advanced by David Brin.26 Brin argues against this concern with privacy—at
least if privacy is defin ed as the need to bl ock the produ cti on and distri buti on of
data about others. He argues against it because he believes that such an end is impossible; the genie is out of the bottle. Better, he suggests, to find ways to ensure that
this data-gathering ability is generally available. The solution to your spying on me
is not to block your spying, but to let me spy on you—to hold you accountable, perhaps for spying, perhaps for whatever else you might be doing.

Th ere are two replies to this argumen t . One asks: Why do we have to ch oo s e ?
Why can't we both control spying and build in checks on the distribution of spying
techniques?

The other is more telling. Brin assumes that this counterspying would be useful
to hold others "accountable." But according to whose norms? "Accountable" is a benign term only so long as we have confidence in the community doing the accounting. When we live in multiple communities, accountability becomes a way for one
community to impose its view of propriety on another. And because we do not live
in a single community; we do not live by a single set of values;and perfect accountability can only undermine this mix of values.

The imp imperfection in present monitoring enables this multiplication of normative communities. The ability to get along without perfect recording enables a diversity that perfect knowledge would erase.

A third value arises from a concern about profiling. If you search on "mortgage"
in a web search engine, advertising for mortgages appears on your computer screen.
The same for sex and for cars. Advertising is linked to the search you submit. Data
about the search are collected—and not just about the search. The site collects every
bit of personal information about you that it can. 27

Data collection is the dominant activity of commercial web sites. Some 92 percent of them collect personal data fr om web users, which they then aggregate, sort,
and use.28 Oscar Gandy calls this the "panoptic sort"—a vast structure for collecting
data and discriminating on the basis of that data—and it is this discrimination, he
says,that ought to concern us.29

But why should it con cern us? Put aside an important class of probl em s — t h e
m i suse of the data—and focus inste ad on its ord i n a ry use. As I said earl i er, t h e
main ef fect is simply to make the market work more smoothly t h ly: produ cts are
m a tch ed to peop l e , and interests to peop l e , in a way that is bet ter targeted and less
i n tru s ive than what we have tod ay. Im a gine a world wh ere adverti s ers could tell
wh i ch venues paid and wh i ch did not; wh ere it was inef f i c i ent to advertise wi t h
bi ll boa rds and on broadc a s t s ; wh ere most advertising was targeted and spec i f i c .
Advertising would be more likely to go to those people for wh om it would be useful inform a ti on . Or so the argument goe s . This is discri m i n a ti on , no do u bt , but

1 5 4

not the discri m i n a ti on of Jim Crow. It is the won wonderful sort of d i s c ri m i n a ti on that
s p a res me Ni ke ad s .

But beyond a perhaps fleeting concern about how such data affect the individual,
profiling raises a more sustained collective concern about how it might affect a community.

That concern is about manipulation. You might be skeptical about the power of
television advertising to control p people's desires. Television is so obvious, the motives so clear. But what happens when the motive is not so obvious? When options
just seem to appear right when you happen to want them? When the system seems
to know what you want better and earlier than you do, how can you know where
these desires really come from?

Whether this possibility is a realistic one, or whether it should be a concern, are
hard and open questions. Steven Johnson argues quite effectively that in fact these
a gents of ch oi ce wi ll fac i l i t a te a mu ch gre a ter ra n ge and divers i ty — even , in part ,
ch a o s — of ch oi ce .3 0 But there's another po s s i bi l i ty as well — profiles wi ll begin to
normalize the population from which the norm is drawn. The observing will affect
the observed. The system watches what you do; it fits you into a pattern; the pattern
is then fed back to you in the form of options set by the pattern; the options reinforce the pattern; the cycle begins again.

A second concern is about equality. Profiling raises a question that was latent in
the market until quite recently. For much of the nineteenth century in the United
States economic thought was animated by an ideal of equality. In the civil space individuals were held to be equal. They could purchase and sell equally; they could approach others on equal terms. Facts about individuals might be known,and some of
these facts might disqualify them from some econ omic tra n s acti on s — your pri or
bankruptcy, for example, might inhibit your ability to make transactions in the future. But in the main, there were spaces of relative anonymity, and economic transactions could occur within that anonymity.31

Over time this space of equ a l i ty has been displaced by econ omic zon i n gs that
aim at segregation.32 They are laws,that is,that promote distinctions based on social
or economic criteria.33 The most telling example is zoning itself. It was not until this
century that local law was used to put people into segregated spaces.34 At first, this
law was racially based, but when racially based zoning was struck down, the techniques of zoning shifted.35

It is interesting to recall just how contentious this use of law was.36 To many, rich
and poor alike,it was an affront to the American ideal of equality to make where you
live depend on how much money you had. It always does, of course, when property
is something you must buy. But zoning laws add the support of law to the segregation imposed by the market. The effect is to re-create in law, and therefore in society, distinctions among people.

There was a time when we would have defined our country as a place that aimed
to erase these distinctions. The historian Gordon Wood describes this goal as an important element of the revolution that gave birth to the United States.37 The enemy

1 5 5

was social and legal hierarchy; the aim was a society of equality. The revolution was
an attack on hierarchies of social rank and the special privileges they might obtain.
All social hierarchies require information before they can make discriminations
of rank. Having enough information about people required,historically, fairly stable
social orders. Making fine class distinctions—knowing, for instance, whether a welldressed young man was the gentleman he claimed to be or only a dressed-up tradesman—required a knowledge of local fashions, accents,customs, and manners. Only
wh ere there was rel a tively little mobi l i ty could these sys tems of h i era rchy be imposed.

As mobility increased, then, these hierarchical systems were challenged. Beyond
the extremes of the very rich and very poor, the ability to make subtle distinctions of
rank disappeared as the mobility and fluidity of society made them too difficult t o
track.

Profiling changes all this. An efficient and effective system for monitoring makes
it po s s i ble on ce again to make these su subtle disti n cti ons of ra n k . Co ll ecting data
cheaply and efficiently will take us back to the past. Think about frequent flyer miles.
Everyone sees the obvious feature of frequent flyer miles—the free trips for people
who fly frequently. This rebate program is quite harmless on its own. The more interesting part is the power it gives to airlines to discriminate in their services.

When a frequent flyer makes a reservation, the reservation carries with it a customer profile. This profile might include information about which seat she prefers
or whether she likes vegetarian food. It also tells the reservation clerk how often this
person flies. Some airlines would then discriminate on the basis of this information.
The most obvious way is through seat location—frequent flyers get better seats. But
such information might also affect how food is allocated on the flight—the frequent
flyers with the most miles get first choice; those with the fewest may get no choice.
In the scheme of social justice, of course, this is small potatoes. But my point is
m ore gen era l . Frequ ent flyer sys tems permit the re - c re a ti on of s ys tems of s t a tu s .
They supply information about individuals that organizations might value,and use,
in dispensing services.38 They make discrimination possible because they restore inform a ti on that mobi l i ty de s troyed . Th ey are ways of defe a ting one ben efit of
anonymity—the benefit of equality.

Economists will argue that in many contexts this ability to discriminate—in effect, to offer goods at different prices to different people—is overall a benefit.39 On
average, people are better off if price discrimination occurs than if it does not. So we
are better off, these economists might say, if we facilitate such discrimination when
we can.

But these values are just one side of the equation. Weighed against them are the
values of equality. For us they may seem remote, but we should not assume that because they are remote now they were always remote.

Take tipping: as benign (if annoying) as you might consider the practice of tipping, there was a time at the turn of the century when the very idea was an insult. It
offended a free citizen's dignity. As Viviana Zelizer describes it:

1 5 6

In the early 1900s, as ti pping became incre a s i n gly pop u l a r, it provo ked gre a t
m oral and social con trovers y. In fact , t h ere were nati nationwide de ef fort s , s ome su ccessful, by state legislatures to abolish tipping by turning it into a punishable misdemeanor. In countless newspaper editorials and magazine articles, in etiquette
boo k s , and even in co u rt , tips were cl o s ely scruti n i zed with a mix of c u ri o s i ty,
amusement,and ambivalence—and often open hostility. When in 1907, the government officially sanctioned tipping by allowing commissioned officers and enl i s ted men of the Un i ted States Navy to inclu de tips as an item in their travel
expense vouchers,the decision was denounced as an illegitimate endorsement of
graft. Periodically, there were calls to organize anti-tipping leagues. 40

There is a conception of equality animating the history that Zelizer recounts that
would be corrupted by the efficiency that profiling embraces. In both cases, there is
a value that is weighed against efficiency. Although I believe this value is relatively
weak in American life, who am I to say? The important point is not about what is
strong or weak, but about the tension or conflict that lay dormant until revealed by
the emerging technology of profiling.

The pattern should be familiar by now, for the change is the change we have seen
el s ewh ere . O n ce aga i n , the code ch a n ge s , t h rowing into rel i ef a con fli ct of va lu e s .
Whereas before there was relative equality because the information that enabled discrimination was too costly to acquire, now it pays to discriminate. The difference—
what makes it pay—is the em er gen ce of a code . The code ch a n ge s , the beh avi or
changes, and a value latent in the prior regime is displaced.

We could react by hobbling the code,thus preserving this world. We could create
con s ti tuti onal or statutory re s tri cti ons that prevent a move to this worl d . Or we
could find ways to reconcile this emerging world with the values we think are fundamental.

S O L U T I O N S

I've identified two distinct threats to the values of privacy that we might imagine cyberspace presenting. No doubt there are others. And no doubt it is an open question
how seriously we will take these threats. But I want to end by considering a few responses. How might we,if convinced of the danger or committed to privacy values,
act to re s tore in the indivi dual a kind of con trol over these pers onal data that are
collected and searchable by the architectures of cyberspace?

The problems are of two sorts. The first is the question of "efficient invasion":
technologies now enable searching with none of the burdens that searches ordinarily ly en t a i l ed . Second is the qu e s ti on of m on i tori n g, and the con trol over data that
monitoring produces. These two problems invite different solutions.I touch on the
first, and then focus on the second.

1 5 7

One note in advance: even this distinction is ambiguous. It presumes some natural division between searching and monitoring. No doubt, given a particular archi -
tecture, there is such a division. But when architectures are plastic, the line between
monitoring and searching is plastic as well. An architecture can be designed to make
a certain behavior monitorable, or it can be designed to necessitate a search to find
that behavior.

Telephones are an easy example.One could design telephone networks to report
with each call who was called, where that person lives, how long the call lasted, and
from which line it was made. Indeed, this is how telephone networks today are des i gn ed . G iven this de s i gn , this inform a ti on is now m o n i to ra bl e , wh ereas under an
earlier design obtaining the same information required a search.

If ch a n ging the arch i tectu re can ch a n ge data from search a ble to mon i tora bl e ,
then the values that are being protected in both contexts must be consistent. My aim
in the next two sections is to articulate a structure that might support this consistency.

S E A R C H A B L E :

T H E P O W E R O F C O D E A N D T H E

P R O M I S E O F P R O C E D U R E

Remember the problem: systems that can invade, or search, without anyone knowing or being disturbed. To this (and any) problem, we might imagine two sorts of
solutions.One solution is code-based:make it harder to search effectively. The other
solution is law-based: add legal protections to inhibit improper searches. I consider
the code-based solution first, since it is the more familiar and more easily summarized.

Encryption. As we saw in chapter 4, the primary use of technologies of encryption is to hide your words from the eyes of others. Encrypted communication creates a p rivate language between the listener and the speaker. While arguments rage
about whether an encrypted communication can actually be cracked,41 for most of
what most of us would want to say, existing encryption is perfectly adequate.

But it is not common. Thus, one solution to improve privacy is a far greater dep l oym ent of en c rypti on code . This is alre ady happen i n g, t h o u gh the dep l oym en t
has been hampered by the government's efforts to control encryption. But slowly—
and again, as a (good) by-product of commerce—the Net is becoming encryption-rich.

But encryption will not solve the problem of privacy. Encrypted communication
would be harder for the government to overhear, but it would not disable the government's legitimate demands for data. If the government has the right to force you
to reveal the contents of a document,then it also has the right to force you to reveal
the key that locks the doc u m en t .4 2 Moreover, not all el ectronic com mu n i c a ti on is
easily encrypted. Some people therefore will demand a solution beyond code.

1 5 8

This soluti on should track two particular va lues pro tecting re a l - s p ace privac y.
First,any burden must be minimal,and any search that creates more than a minimal
burden must be justified by individualized suspicion.43 Second, any search must be
disclosed—individuals must be given notice that their space has been searched.44

It might be said that the principle behind the second idea is to ban all of these inoffensive and invisible searches. Perhaps that should be done. But if we understand
this second idea to be about checking the abuse of power (since by giving notice you
give someone opportunity to complain), then we might imagine substitutions that
pro tect the same va lue wi t h o ut sac sacrificing the ben efit these tech n o l ogies migh t
bring.

A tra n s l a ti on , t h erefore , m i ght well look like this. Al t h o u gh the tech n o l ogy
would enable these costless searches, they should be deployed only when adequate
and strong procedu ral limits have been met . And adequ a te and strong procedu ra l
limits would include the requirement that two branches of government (not just the
executive) concur before any invasion occurs.45

But what would invasion mean? Again, architectures could be designed to make
data acce s s i ble wi t h o ut an inva s i on ; t h ey could be de s i gn ed , that is, to make data
monitorable, so that a search of the records of monitoring would involve no invasion at all.

The choice we must make is between two conceptions of law enforcement that
tod ay are mixed . One con cepti on is re active , re s ponding to an even t ; the other is
preven tive , pred i cting an even t . The re active model would define inva s i on as any
sifting to identify a culprit; this sifting, the argument goes, should be allowed only
when there is cause to suspect. Scanning the innocent, on this view, would not be
permitted,though collecting data to enable a subsequent scan might be.

The preventive conception would allow constant monitoring. The values of procedu re here would simply con trol how mu ch you would have to know abo ut the
people you are mon i toring in order to com m en ce mon i tori n g ; but you could sti ll
design this space to enable monitoring, and you could monitor for patterns suggesting misbehavior.

For a re a l - s p ace example not far from pre s ent tech n o l ogy, think abo ut airport
s e a rch e s . Tech n o l ogy is now being devel oped to en a ble som ething call ed body
s c a n s . These would en a ble an official to peer thro u gh your clothes to see wh et h er
you are con cealing we a pon s . We might imagine any nu m ber of w ays to dep l oy this
tech n o l ogy. In a purely re active mode , we might say that on ly the suspicious can
be su bj ected to the body scan, t h o u gh a fear abo ut sel ective suspiciousness migh t
push us to make the scan gen era l . Th ere is no insult in being scanned , the argum ent goe s , i f everyone else is; t h ere is on ly an insult if you have been picked out
f rom the crowd .

But even if everyone were scanned, there would be questions about how the system should be designed. Would the officials see the people whose bodies they were
scanning? Im a gi n e , in one vers i on , of ficers watching people en ter a boo t h , s eei n g
what is under their clothes, and then watching (leering) as they leave. Contrast that

1 5 9

system with one in which the officers are located elsewhere, the images they see are
cut up by the computer, and though they still see what is under people's clothes,they
cannot automatically connect what they are seeing to particular individuals.

Whatever you think about this procedure in general,the second design is a more
effective balance of interests than the first. Still, even with this second design there
remains this latent question of how far we will push the preventive over the exceptional. Airports are exceptional, though this technology could be extended beyond
airports. Whether it should be is the choice pressed on us by these changes in code.

M O N I T O R I N G :

T H E R E - S O L U T I O N T H R O U G H

P R O P E R T Y

Control over the results of monitoring is a more ambitious project. The traditional
solution is to enact laws to deal with the problem. That has been Europe's solution,
for example—extensive and sustained support for legal protections against the misuse of data. The substance of such law is, I think, uncontroversial. Its values are essentially "notice" and "choice"—companies will inform consumers about how data
will be used and not use it for any other purpose. Its aim is to restore to the individual control over the use of data about herself.46

But in the United States we have turned to law less often. Although sensational
abuses have at times produced targeted eted federal laws, they have not led to comprehensive legal protection.47

This is not to say, of course, that we have no protections for privacy. As we have
seen throughout, there are other laws besides federal ones, as well as regulators bes i des the law. At times these other forms of pro tecti on may pro tect privacy bet ter
than law does. Obviously, if we want to understand the protections for privacy, we
should understand how these interventions matter.

The U. S . govern m ent has argued for a type of i n du s try "s el f - reg u l a ti on" expressed through industrial codes of conduct. An old idea strangely called "new"(the
same practices were popular during the New Deal),self-regulation lets industries set
the rules about how data ought to be protected. Once they set the rules, the argument goes, pressure from other members of the industry, or from the market itself,
could force a sustained compliance.

Of course, norms can be effective regulators. But a necessary condition of their
success is that the community of norm enforcers include those who bear the cost of
the behavior being regulated. And I confess to being skeptical that this is in fact happening here. The industry that would develop the norms to regulate itself does not
bear the rel evant costs of the use of the data it co ll ect s . That cost—the privac y
cost—is borne by individuals,not corporations; they are not part of the community
building the norm.

So rather than norms,I want to suggest a different regulatory mechanism—one
that relies on code rather than good behavior. In a world where the dimensions of

1 6 0

decision have been so r radically multiplied, we need a more effective way to control
what we collectively do.

The standard response to this question of data practices is choice—to give the
individual the right to choose how her data will be used. And the standard way we
have pushed individuals to choose is through text—through privacy statements that
report a site's privacy practices and then give the consumer the right to opt in or out
of those practices.48

But the processing costs for text are wildly high. No one has the time or patience
to re ad thro u gh cumbers ome doc u m ents de s c ri bing ob s c u re rules for con tro ll i n g
data. What is needed is a way for the machine to negotiate our privacy concerns for
us, a way to delegate the negotiating process to a smart agent—an electronic butler—who, like the butler, knows well what we like and what we do not like.

What is needed , that is, is a mach i n e - to - m achine pro tocol for nego ti a ting privacy protections.49 The user sets her preferences once—specifies how she would negotiate privacy and what she is willing to give up—and from that moment on, when
she enters a site, the site and her machine negotiate. Only if the machines can agree
will the site be able to obtain her personal data.

The kern el to this arch i tectu re is a proj ect spon s ored by the World Wi de Web
Consortium.50 Dubbed P3P, the project's aim is to facilitate an architecture within
which users can express their preferences and negotiate the use of data about them.
"P3P products will allow users to be informed of site practices (in both machine and
human readable formats), to delegate decisions to their computer when appropriate, and allow users to tailor their relationship to specific sites."51

My aim is not to endorse this particular privacy architecture. P3P has its probl em s , not all of t h em cl e a rly re s o lva bl e .5 2 My point inste ad is the same one made
throughout this book: we could imagine an architecture, tied to a market, that protects privacy ri ghts in a way that real space cannot, but that arch i tectu re wi ll not
emerge on its own. It needs the push of law.

The law would be a kind of property right in privacy. Individuals must have both
the ability to negotiate easily over privacy rights and the entitlement to privacy as a
default. That is property's purpose: it says to those who want, you must negotiate
before you can take. P3P is the architecture to facilitate that negotiation; the law is
the rule that says negotiation must occur.

But why property? What is the benefit of a property regime? Why is it superior

to a regime that simply enforces rules (as the Europeans do)?

A property regime is fundamentally different from what we have now.53 Privacy
now is protected through liability rules—if you invade someone's privacy, they can
sue you and you must then pay. There are two important differences between liability rules and property rules.

The first difference is that a property regime requires negotiation before taking;
a liability regime allows a taking, and payment later. The key to a property regime is
to give control, and power, to the person holding the property right; the key in a liability regime is to protect the right but facilitate the transfer of some asset from one

1 6 1

pers on to another. Th ere can be holdouts uts (people who wi ll not agree to tra n s fer )
with a property regime; there can be no holdouts in a liability regime. There is individual control or autonomy with a property regime, but not with a liability regime.
Property protects choice; liability protects transfer.

The second differen ce fo ll ows direct ly from the firs t . With a liabi l i ty ru l e , a co u rt ,
ju ry, or statute determines how va lu a ble certain privacy is to yo u . O rd i n a ri ly, you are
com pen s a ted on ly for what a re a s on a ble pers on would have su f fered . It is like a regi m e
for buying and selling cars in wh i ch , ra t h er than nego ti a ting up fron t ,
people simply take other peop l e's cars and a co u rt later determines what they must pay.
Property regimes work very differently. When you have a p roperty right, before
s om eone takes your property they must nego ti a te with you abo ut how mu ch it is
wort h . If you have a sen ti m ental attach m ent to your 1974 Nova , t h ere is little the
buyer can do about it. The car's market value might be $200, but if you will not sell
it for less than $1,000,the buyer is stuck. You cannot be forced to give up your Nova
unless you get your minimum price.

A property regime thus protects both those who value their privacy more than
others and those who value it less, by requiring that someone who wants to take a
given resource must ask. Such a regime gives us c confidence that if a trade occurs, it
will be at a price that makes neither party worse off.

Th ere are those, e s pec i a lly on the lef t , who are rad i c a lly skeptical abo ut a property regime to pro tect privac y.5 4 Property is said to com m od i f y, to marketize ze , to
m on eti ze rel a ti ons that are va lu a ble on a very different scale. The last thing we
n eed , these skeptics argue, is to have another sph ere of our lives ru l ed by the market .5 5

My impulse is to sympathize with this argument. But I am not convinced that
a nything is ulti m a tely ga i n ed by this insistence ce on theory. We are not deb a ti n g
whether to move into a world where data are collected, used, and sold. We already
live in that world. Given that we are here, how can we ensure that at least some control is granted to those whom these data are about? I advocate a property regime not
because of the sanctity of property as an ideal, but because of its utility in serving a
different but quite important ideal.

Those who take this ideal of privacy to an ex treme have a very different vi ew
about how the architecture should support it. The action group Privacy Now!, for
example,threatens terrorist action to disable the systems of data gathering and control.56 Marc Rotenberg of the Electronic Privacy Information Center (EPIC) argues
s tron gly against any arch i tectu re that en a bles the trading or exch a n ge of privac y
rights.57 Both groups view privacy as a kind of inalienable right—one whose dignity
deserves the respect that we give the right to vote or the freedom to engage in sexual
relations. They believe that none of these rights ought to be sold, and that exchange
of any of them should be criminalized.

We could certainly construct a world where privacy was so viewed, and we could
build walls that the po l i ce defen ded . But I do u bt that this ex treme is actu a lly our
view—or more important, that it ought to be.

1 6 2

A world where privacy is commodified in this sense might turn out to be radically inferior. Or it might be fine. My argument is not from first principles; it is intended only as a pragmatic response to an emerging issue. If the world turns out not
to our liking, then of course we should modify the architectures.

But the key is to see the relationship between these architectures and the possibilities for exchange. As Justice Breyer argued about intellectual property, it may well
be that constructing the architectures for exchange is all we need to do to ensure the
protection appropriate to the context.58 We will just have to see.

P R I V A C Y C O M P A R E D

The reader who was dissatisfied with my argument in the last chapter is likely to begin asking pointed questions."Didn't you reject in the last chapter the very regime
you are endorsing here? Didn't you reject an architecture that would facilitate perfect sale of intellectual property? Isn't that what you've created here?"

The charge is accurate enough. I have endorsed an architecture here that is ess en ti a lly the same arch i tectu re I qu e s ti on ed for intell ectual property. Both are
regimes for trading information; both make information "like" "real" property. Yet
with copyright, I argued against a fully privatized property regime; with privacy, I
am arguing in favor of it. What gives?

The difference is in the underlying values that inform, or that should inform,information in each context. In the context of intellectual property, our bias should be
for freedom. Who knows what "information wants";59 whatever it wants, we should
read the bargain that the law strikes with holders of intellectual property as narrowly
as we can. We should take a grudging attitude to property rights in intellectual property; we should support them only as much as necessary to build and support information regimes.

But (at least some kinds of) information about individuals should be treated differently. You do not strike a deal with the law about personal or private information.
The law does not of fer you a mon opo ly ri ght in exch a n ge for your publ i c a ti on of
these facts. That is what is distinct about privacy: individuals should be able to control information about themselves. We should be eager to help them protect that information by giving them the structures and the rights to do so. We value, or want,
our peace. And thus, a r egime that allows us such peace by giving us control over
priva te inform a ti on is a regime con s consonant with public va lu e s . It is a regime that
public authorities should support.

This conclusion is subject to important qualifications, only two of which I will

describe here.

The first is that nothing in my regime would give individuals final or complete
control over the kinds of data they can sell, or the kinds of privacy they can buy. The
P3P regime would in principle enable upstream control of privacy rights as well as
individual control. If we lived, for example, in a regime that identified individuals

1 6 3

based on jurisdiction, then transactions with the P3P regime could be limited based
on the rules for particular jurisdictions.

Second, there is no reason such a regime would have to protect all kinds of private data, and nothing in the scheme so far tells us what should and should not be
considered "private" information. There may be facts about yourself that you are not
permitted to hide; more important, there may be claims about yourself that you are
not permitted to make ("I am a lawyer," or, "Call me,I'm a doctor"). You should not
be permitted to engage in fraud or to do harm to others. This limitation is an analog to fair use in intellectual property—a limit to the space that privacy may protect.

I started this chapter by claiming that with privacy the cat is already out of the bag.
We already have architectures that deny individuals control over what others know
about them; the question is what we can do in response.

My response has been: look to the code. We must build into the architecture a capacity to enable choice—not choice by humans but by machines. The architecture
must enable machine-to-machine negotiations about privacy so that individuals can
instruct their machines about the privacy they want to protect.

But how will we get there? How can this architecture be erected? Individuals may
want cyberspace to p rotect their privacy, but what would push cyberspace to build
in the necessary architectures?

Not the market. The power of commerce is not behind any such change. Here,
the invisible hand would really be invisible. Collective action must be taken to bend
the arch i tectu res tow a rd this goa l , and co ll ective acti on is just what po l i tics is for.
Laissez-faire will not cut it.

T W E L V E

f r e e s p e e c h

Th e r i gh t t o f r ee speech is not t he r i gh t t o speak for f r ee . It is not t he r i gh t
to free access to television, or the right that people not hate you for what you have
to say. S tri ct ly spe a k i n g — l ega lly speaking—the ri ght to free speech in the Un i ted
States means the right to be free from punishment by the government in retaliation
for at least some (prob a bly most) speech . You cannot be ja i l ed for cri ticizing the
pre s i den t , t h o u gh you can be ja i l ed for thre a tening him; you cannot be fined for
prom o ting segrega ti on , t h o u gh you wi ll be shu n n ed if you do ; you cannot be
stopped from speaking in a public place,though you can be stopped from speaking
with an FM transmitter. Speech in the United States is protected—in a complex,and
at times convo luted , w ay — but its con s ti tuti onal pro tecti on is a pro tecti on aga i n s t
the government.

Nevertheless, a constitutional a account of free speech that thought only of government would be radically incomplete.1 Two societies could have the same "First
Am en d m en t"—the same pro tecti ons against govern m en t's wra t h — but if wi t h i n
one dissen ters are to l era ted while in the other they are shu n n ed , the two soc i eti e s
would be very different free speech soc i eti e s . More than govern m ent con s tra i n s
s peech , and more than govern m ent prote ct s f ree speech . A com p l ete account of
this—and any—right must consider the full range of burdens and protections.

Consider, for example,the "rights" of the disabled to protection against discrimination. The law protects the disabled; social norms don't, neither does the market,
and until the law intervened, neither did architectures. The net of these four modalities would describe the protection,in any particular context,that the disabled have.
Law might intervene to strengthen the protection—regulating architecture, for example, so that it better protects against discrimination in access. But for any given
mix we could understand these four modalities working together to protect (however slightly) the disabled from discrimination.

In the terms of chapter 7, we could then use the same four modalities to consider
within each context the protection from constraint, as well as the imposition of regfreed r e e s p e e c h

1 6 5

u l a tory con s tra i n t s . Mod a l i ties of con s traint (powers) functi on as a sword aga i n s t
the obj ect reg u l a ted ; m od a l i ties of pro tecti on (ri ghts) functi on as a shield for the
regulated against constraint. The following figure captures the point.

In the cen ter is the obj ect reg u l a ted—the pathetic dot from ch a pter 7. Su surrounding the indivi dual now is a shield of pro tecti on , the net of l aw / n orm s / m a rket / a rch i tectu re that limits the con s traints these mod a l i ties would otherwise place
on the individual. I have not separated the four in the sphere of the shield because
obvi o u s ly there is no direct match bet ween the mod a l i ty of con s traint and the
modality of protection. When law as protector conflicts with law as constraint, constitutional law overrides ordinary law.

These modalities function together. Some might undercut others, meaning that
the sum of protections might seem to be less significant than the parts. The "right"
to prom o te the dec ri m i n a l i z a ti on of d ru gs in the pre s ent con text of the war on
drugs is an example. The law protects your right to advocate the decriminalization
of drugs. The state cannot lock you up if,like George Soros, you start a campaign for
the dec ri m i n a l i z a ti on of m a rijuana or if, l i ke the Nobel Pri ze – winning econ om i s t
Milton Friedman or the federal judge Richard Posner, you write articles suggesting
it. If the First Amendment means anything, it means that the state cannot criminalize speech about law reform.

But that legal protection does not mean that I would suffer no consequences for
promoting legalization of drugs. My neighbors would be appalled at the idea, and
some no doubt would shun me. Nor would the market necessarily support me. It

1 6 6

would be quite difficult to buy time on television for a speech advocating such a reform. Television stations have the right to select their ads (within some limits); they
do not like con troversial or tasteless ad s .2 Mine would most likely be deem ed too
con trovers i a l . S t a ti ons also have the FCC—an active combatant in the war on
drugs—looking over their shoulders. And even if I were permitted to advertise,I am
not George Soros.I do not have millions to spend on such a campaign.I might mana ge a few off-hour spots on a local stati on , but I could not afford , for instance , a
campaign on the networks during prime time.

F i n a lly, a rch i tectu re wo u l d n't pro tect my speech very well ei t h er. In the Un i ted
S t a tes at least, t h ere are few places wh ere you can stand before the public and add ress them abo ut some matter of p u blic import wi t h o ut most people thinking yo u
a nut or a nu i s a n ce . Th ere is no spe a kers' corn er in every city; most towns do not
h ave a town meeti n g. "Am erica of f l i n e ," in this sen s e , is very mu ch like Am eri c a
Online—not de s i gn ed to give indivi duals access to a wi de audien ce to ad d re s s
p u blic matters . O n ly profe s s i professionals get to ad d ress Am ericans on public issu e s —
po l i ti c i a n s , s ch o l a rs , cel celebrities ti e s , j o u rn a l i s t s , and activi s t s , most of wh om are conf i n ed to single issu e s . The rest of us have a ch oi ce — l i s ten , or be dispatch ed to the
gulag of s ocial lu n ac y.

Thus, the protection for controversial speech is more conditional than a nar row
legal view would suggest. The right to be a dissenter is on balance less protected than
it could be when more than law is reckoned.

Let's take this example now to cyberspace. How is the "right" to promote the legalization of drugs in cyberspace protected? Here too, of course,the law protects my
ri ght of advoc acy—at least in the Un i ted State s . It is qu i te po s s i ble that the same
speech would be illegal elsewhere and that perhaps I could be prosecuted for uttering su ch speech in cybers p ace " i n" a n o t h er co u n try. S peech prom o ting the Na z i
Party, for example, is legal in the Unit ed States but not in Germany.3 Uttering such
speech in cyberspace may make one liable in German space as well.

The law therefore is an imperfect pro tecti on . Do norms help to pro tect
s peech? With the rel a tive anonym i ty of c ybers p ace and its growing size , n orms do
not functi on well there to re s train con troversial speech . Even in cybers p ace s
wh ere people know each other well , t h ey are likely to be more to l erant of d i s s ident vi ews wh en they know (or bel i eve , or hope) the dissident lives thousands of
miles aw ay.

The market provides a major protection to speech—relative to real space, market constraints on speech in cyberspace are tiny. Recall how easily Jake Baker became
a publisher, with a potential readership greater than the readership of all law books
(like this one) published in the last decade.

But on top of this list of protectors of speech in cyberspace is architecture. Relative anonym i ty, decen tra l i zed distri buti on , mu l tiple points of acce s s , no nece s s a ry
tie to geogra phy, no simple sys tem to iden tify con ten t , tools of en c rypti on4— a ll
these features and consequences of the Internet protocol make it difficult to control
speech in cyberspace. The architecture of cyberspace is the real protector of speech

1 6 7

there; it is the real "First Amendment in cyberspace," and this First Amendment is
no local ordinance.5

Just think about what this means. For over fifty years the United States has been
the exporter o f a certain political ideology, at its core a conception of free sp eech.
Many have criticized this conception:some found it too extreme,others not extreme
en o u gh . Repre s s ive regi m e s — Ch i n a , North Korea a — rej ected it direct ly; to l era n t
regi m e s — Fra n ce , Hu n ga ry — com p l a i n ed of c u l tu ral dec ay; ega l i t a rian regi m e s —
the Scandinavian countries—puzzled over how we could think of ourselves as free
when only the rich can speak and pornography is repressed.

This debate has gone on at the political level for a long time. And yet,as if under
cover of night, we have now wired these nations with an architecture of communication that builds within their borders a far stronger First Amendment than our ideology ever advanced. Nations wake up to find that their telephone lines are tools of
free expression,that e-mail carries news of their repression far beyond their borders,
that images are no longer the monopoly of state-run television stations but can be
transmitted from a simple modem. We have exported to the world, through the architecture of the Internet, a First Amendment in code more extreme than our own
First Amendment in law.

This chapter is about the regulation of speech and the protection of speech in cyberspace—and therefore also in real space. My aim is to obsess about the relationship bet ween arch i tectu re and the freedom it makes po s s i bl e , and abo ut the
significance of law in the construction of that architecture. It is to get you to see how
this freedom is built—the constitutional politics in the architectures of cyberspace.
I say "politics" because this building is not over. As I have argued (over and over
again), there is no single architecture for cyberspace; there is no given or necessary
structure to its design. The first-generation Internet might well have breached walls
of control. But there is no reason to believe that architects of the second generation
will do so, or not to expect a second generation to build in control. There is no reason to think,in other words,that this initial flash of freedom will not be short-lived.
And there is certainly no justification for acting as if it will not.

We can already see the beginnings of this reconstruction. Already the architecture is being remade to reregulate what real-space architecture before made regulable. Already the Net is changing from free to controlled.

Some of these steps to reregulate are inevitable; some shift back is unavoidable.
Before the change is complete, however, we must understand the freedoms the Net
now provides and determine which freedoms we mean to preserve.

And not just preserve. The architecture of the Internet, as it is right now, is perhaps the most important model of free speech since the founding. This model has
implications far beyond e-mail and web pages. Two hundred years after the framers
ratified the Constitution,the Net has taught us what the First Amendment means. If
we take this meaning seriously, then the First Amendment will require a fairly radical restructuring of the architectures of speech off the Net as well.

1 6 8

But all that is to get ahead of the story. In the balance of this chapter, I want to
tell three stori e s — one abo ut publ i c a ti on , one abo ut acce s s , and one abo ut distribution. With each, I want to consider how "free speech" is regulated.

These stories do not all have the same constitutional significance. My aim in the
f i rst is to illu s tra te a rel a ti onship bet ween arch i tectu res and insti tuti ons of f ree
speech; the second identifies another latent ambiguity in our constitutional regime;
and the third is a straightforward translation of the framing design. It is the third
story that, if correct, would prove the most fundamental, though all three illustrate
the relationship between values, architectures, and the choices they now present.

T H E R E G U L A T O R S O F S P E E C H :

P U B L I C A T I O N

Floyd Abrams is one of America's leading First Amendment lawyers. In 1971 he was
a young partner at the law firm of Cahill, Gordon.6 Late in the evening of Monday,
June 14, he received a call from James Goodale, in-house counsel for the New York
Ti m e s . G Goodale asked Abra m s , toget h er with Al ex a n der Bi ckel , a Yale Law Sch oo l
professor, to defend the New York Times in a lawsuit that was to be filed the very next
day.

The New York Times had just refused the government's request that it cease all
publication of what we now know as the "Pentagon Papers" and return the source
doc u m ents to the Dep a rtm ent of Defen s e .7 These papers , m o s t ly from the Pen t Pentagon "History of U.S. Decision Making Process on Vietnam Policy," evaluated U.S.
policy during the Vietnam War.8 Their evaluation was extremely negative, and their
conclusions were devastating. The papers made the government look extremely bad
and made the war seem unwinnable.

The papers had been given to the New York Times by someone who did think the
war was unwinnable; who had worked in the Pentagon and helped write the report;
who at first did not believe the war was unwinnable but who over time had come to
see the impossibility that the Vietnam War was.

This someone was Daniel Ellsberg. Ellsberg smuggled one of the fifteen copies of
the papers from a safe at the RAND Corporation to an offsite photocopier. There,he
and a co ll e a g u e , An t h ony Ru s s o, ph o tocop i ed the papers over a peri od of s evera l
wee k s .9 E ll s berg tri ed wi t h o ut su success to make the papers public by having them
read into the Congressional Record. He eventually contacted the New York Times reporter Neil Sheehan in the hope that the Times would publish them. Ellsberg knew
that this was a criminal act, but for him the war itself was a criminal act;his aim was
to let the American people see just what kind of a crime it was.

For two and a half months the Times editors pored over the pap ers, working to
verify their authenticity and accuracy. After an extensive review, the editors determined that they were authentic and resolved to publish the first of a ten-part series
of excerpts and stories on Sunday, June 13, 1971.10

1 6 9

On Mon d ay afternoon oon , one day after the first install m ent appe a red , At torn ey

General John Mitchell sent a telegraph to the New York Times stating:

I respectfully request that you publish no further information of this character
and advise me that you have made ar rangements for the return of these documents to the Department of Defense.11

When the Times failed to comply, the government filed papers to enjoin the paper
from continuing to publish stories and excerpts from the documents.12

The govern m en t's claims were simple: these papers con t a i n ed govern m ent sec ret s ; t h ey were sto l en from the po s s e s s i on of the govern m en t ; to publish them
would put many American soldiers at risk and embarrass the United States in the
eyes of the world. This concern about embarrassment was more than mere vanity:
embarrassment, the government argued, would weaken our bargaining position in
the efforts to negotiate a peace. Because of the harm that would come from further
publication, the Court should step in to stop it.

The argument was not unprecedented. Past courts had stopped the publication
of life-threatening texts, especially in the context of war. As the Supreme Court said
in Near v Minnesota, for example, "no one would question but that a government
might prevent actual obstruction to its recruiting service or the publication of the
sailing dates of transports or the number and location of troops."13

Yet the qu e s ti on was not easily re s o lved . Standing against precedent was an inc re a s i n gly clear com m a n d : i f the First Am en d m ent meant anything h i n g, it meant that
the govern m ent gen era lly cannot exercise the power of pri or re s tra i n t .1 4 " Pri or res tra i n t" is wh en the govern m ent gets a co u rt to stop publ i c a ti on of s ome materi a l ,
ra t h er than punish the publ i s h er later for what was ill ega lly publ i s h ed . Su ch a
power is thought to pre s ent mu ch gre a ter risks to a sys tem of f ree speech .1 5 At torn ey Gen eral Mi tch ell was asking the Co u rt to exercise this power of pri or res tra i n t .

The Court struggled with the question, but resolved it quickly. It struggled because the costs seemed so high, 16 but when it resolved the question, it did so quite
squarely against the government. In the Court's reading, the Constitution gave the
New York Times the right to publish without the threat of prior restraint.

The Pentagon Papers is a First Amendment classic—a striking reminder of how
powerful a constitution can be. But even classics get old. In a recent speech, Abrams
asked an incredible question: Is the case really important anymore?

For the government to succeed in a claim that a printing should be stopped, it
must show "irreparable harm"—harm so significant and irreversible that the Court
must intervene to prevent it.17 But the showing depends on the publication not occurring—if the Pentagon Papers had already been published by the Chicago Tribune,
the government would have claimed no compelling interest to stop its publication in
the New York Times. When the cat is already out of the bag, preventing further publication cannot prevent the cat from getting out of the bag.

1 7 0

This point is made clear in a case that came after New York Times—a case that
could have been invented by a law professor. The Progressive was a left-wing magazine that in the late 1970s commissioned an article by Howard Morland about the
workings of an H-bomb. The Progressive first submitted the manuscript to the Department of Energy, and the government in turn brought an injunction to block its
publication. The government's claim was compelling: to give to the world the secrets
of how to build a bomb would make it possible for any terrorist to annihilate any
city. On March 26, 1979, Judge Robert Warren of the Western District of Wisconsin
a greed and issu ed a tem pora ry re s training order en j oining The Pro gre s s ive f rom
publishing the article.18

Unlike the Pentagon Papers case, this case stewed, no doubt in part because the
district judge hearing the case understood the great risk this publication presented.
The judge did stop the publication while he thought through the case. And for two
and a half months he thought. The publishers went to the Court o f Appeals, and to
the Supreme Court, asking each to hurry the thinking along. No one did anything.
Un til Chu ck Ha n s en , a com p uter progra m m er, ran a " De s i gn Your Own H-
Bom b" con test and circ u l a ted an ei gh teen - p a ge let ter in wh i ch he det a i l ed his understanding of h ow an H-Bomb work s . On Septem ber 16, 1 9 7 9 , the Pre s s - Co n n e cti o n of
Mad i s on , Wi s con s i n , p u bl i s h ed the let ter. The next day the govern m ent moved to
wi t h d raw its case, con ceding that it was now moo t . The com pelling interest of t h e
govern m ent en ded on ce the sec ret was out .1 9

Note what this sequence implies. There is a need for the constitutional protection that the Pentagon Papers case represents only because there is a real constraint
on publishing. Publishing requires a publisher, and a publisher can be punished by
the state. But if the essence or facts of the publication are published elsewhere first,
then the need for constitutional protection disappears. Once the piece is published,
there is no further legal justification for suppressing it.

So, Abrams asks, would the case be important today? Is the constitutional protection of the Pentagon Papers case still essential?

Surprisingly, Floyd Abrams suggests not.20 Today there's a way to ensure that the
government never has a compelling interest in asking a court to suppress publication. If the New York Times wanted to publish the Pentagon Papers today, it could
ensure that the papers had been previously published simply by leaking them to a
USENET newsgroup. More quickly than its own newspaper is distributed, the papers would then be published in millions of places across the world. The need for
the constitutional protection would be erased, because the architecture of the system
gives anyone the power to publish, quickly and anonymously.

The architecture of the Net, Abrams argues, eliminates the need for the constituti onal pro tecti on ; even bet ter, the Net pro tects against pri or re s traint just as the
Constitution did—by ensuring that strong controls on information can no longer
be achieved. Abrams argues that the Net does what publication of the Pentagon Papers was designed to do—ensure that the truth does not remain hidden.

1 7 1

But there's a second side to this story.
On Ju ly 17, 1 9 9 6 , TWA Flight 800 fell from the sky ten miles of f the southern h ern
coast of Cen ter Mori ch e s , New York . Two hu n d red and thirty people were kill ed .
Immediately after the accident the United States launched the largest investigation
of an airplane crash in the history of the Na ti onal Tra n s port a ti on Sa Safety Boa rd
(NTSB), spending $27 million to discover the cause of the crash, which eventually
was determined to have been a mechanical failure.21

This was not, however, the view o f the Internet. From the beginning stories circ u l a ted abo ut missiles—people said they saw a streaking light shoot tow a rd the
plane just before it went down. There were also stories about missile tests conducted
by the Navy seven ty miles from the crash site .2 2 And then there were reports of a
cover-up by the U.S. government to hide its involvement in one of the worst civil air
disasters in American history.

The govern m ent den i ed these report s , yet the more the govern m ent den i ed
them, the more contrary "evidence" appeared on the Net.23 There were repeated reports of sightings of missiles by witnesses on the ground. These reports, writers on
the Net cl a i m ed , were being "su ppre s s ed " by the govern m en t . The wi witnesses were
being silenced. And then,as a final straw in the story, there was a report,purportedly
by a government insider, claiming that indeed there was a conspiracy— because evidence suggested that friendly fire had shot down TWA 800.24

A former press secretary to President John F. Kennedy believed it. In a speech in
France, Pierre Salinger announced that his government was hiding the facts of the
case, and that he had the proof.

I rem em ber this event well . I was talking to a co lleague just after I heard
Salinger's report. I recounted Salinger's report to this colleague, a leading c constitutional onal scholar from one of the top Am erican law sch oo l s . We both were at a loss
about what to believe. There were cross-cutting intuitions about credibility. Salinger
was no nut, but the story was certainly loony.

Salinger, it turns out,had been caught by the Net. He had been tricked by the flip
side of the point that everyone can publish. In a world where everyone can publish,
it is very hard to know what to believe. For publishers are also editors, and editors
make decisions about what to publish—decisions that ordinarily are driven at least
in part by the question, is it true? Statements cannot verify themselves. We cannot
always tell, from a sentence reporting a fact about the world, whether that sentence
is true.25 So in addition to our own experience and knowledge of the world, we must
rely on structures of reputation that build credibility. When something is published,
we associate the claim with the publisher. If the New York Times says that aliens have
k i d n a pped the pre s i den t , that is a different story from a story with the iden ti c a l
words published in the National Enquirer.

When a new technology comes along, however, we are likely to lose our bearings.
This is nothing new. It is said that the word phony comes from the birth of the telephone—the phony was the con artist who used the phone to trick people who were

1 7 2

familiar with face-to-face communication only. We should expect the same uncertainty in cyberspace,and expect that it too, at first, will shake expectations of credibility.

Abrams's argument then depends on a feature of the Net that we cannot take for
granted. If there were credibility on the Net, the importance of the Pentagon Papers
would indeed be diminished. But if speech on the Net lacks credibility, the protections of the Constitution again become important.

"Credibility," however, is not a quality that is legislated; nor is it coded. It comes
f rom insti tuti ons of trust that help the re ader sep a ra te rel i a ble from unreliable i a bl e
sources. Flight 800 thus raises an important question: How can we reestablish credibility in this space so that it is not lost to the loons?26

Two solutions are possible.One,a top-down solution, would empower editors—
people who select what should be published based on a host of considerations, including the truth of what is said. The other, bo t tom - u p, would fac i l i t a te the
construction of reputation—a measure of the significance of the speech that turns
on who is actually uttering it. In real space, of course, the two go together—editing
goes with publishing, and hence, because of the selections made by the editors at the
New York Times, the reputation of the New York Times is different from the reputation of the National Enquirer. We might have thought that the New York Times sold
newspapers. But cyberspace is teaching us that it sells editing services that happen to
be delivered on paper.

In cyberspace, these two functions could be distinct. Editing could be separate
f rom distri buti on , wh i ch means that there could be a gre a ter com peti ti on amon g
editors. And credibility would be one of the values that editing services would sell.
Traditionally such credibility has been created by an institution of some stability ty—the New Yo rk Ti m e s , for ex a m p l e — s erving a creden credentialing functi on . Bei n g
hired as a reporter by the New York Times says something important about your status; the Times then has an interest in policing you—your misadventures would ref l ect nega tively on the Ti m e s . The public gets the ben efit of a clear stru ctu re of
responsibility.

We could see just this kind of reintermediation—restoration of intermediaries—
on the Net.27 But it could happen in other ways too. Imagine a kind of rating service
that, as with bonds or with medical malpractice insurance, rates the reputation of
each reporter and source through some formula of its own determination. We could
i m a gine any nu m ber of su ch agen c i e s , e ach providing reporters with ra ti n gs that
s erve as their creden ti a l . The reporter 's ra ting would become part of every story
published on the Net. And the same with any source, anonymous or not, since any
source could also receive a rating.

In this example, an architecture of trust would replace institutions of trust.28 A
reporter could gain credibility as a good and accurate reporter whether employed by
the New York Times or not. Hence, reintermediation on the Net need not involve the
re-creation of the relatively few trusted publishers in real space but instead could fof r e e s p e e c h

1 7 3

cus on the relocation of the credentialing service from the publisher to independent
agencies.

The difference between these regulations is a difference in the power of institutions. Without preferring one over the other, we may note the trade-off between
an architecture and a market structure.

T H E R E G U L A T O R S O F S P E E C H : A C C E S S

Porn ogra phy, in real space , is reg u l a ted ex ten s ively. Porn—not ob s cen i ty and not
child porn, but what the Supreme Court calls sexually explicit speech that is "harmful to minors."29 Obscenity and child porn are regulated too, but their regulation is
different from that of porn. Obscenity and child porn are banned for all people in
real space (United States); porn is banned only for kids.

We can understand porn's regulation by considering the four modalities of regulation. All four are directed to a common end: to keep porn away from kids while
(sometimes) ensuring adults' access to it.

First, laws do this. Laws in many jurisdictions require that porn not be sold to
kids.30 Since at least 1968, when the Supreme Court decided Ginsberg v New York,31
such regulation has been consistently upheld. States can require vendors of porn to
sell it only to adults; they can also require vendors to check the ID of buyers.

But not on ly laws ch a n n el. Social norms do as well . Norms re s tri ct the sale of
porn gen era lly — s oc i ety for the most part sneers at con su m ers of porn , and this
sneer undoubtedly inhibits its sale. Norms also sup port the policy of keeping porn
away from kids. Porn dealers don't like to think of themselves as people who corrupt. Selling porn to kids is universally seen as corrupting, and this is an important
constraint on dealers, as on anyone else.

The market too keeps porn away from kids. Porn in real space costs money. Kids,
on average, do not have much money. Because sellers discriminate on the basis of
who can pay, they thus help to discourage children from getting porn.

But the regulations of law, market,and norms all presuppose another regulation
that makes the first three possible: the regulation of real-space architecture. In real
s p ace it is hard to hide that you are a ch i l d . A kid can don a mu s t ache and cl i m b
onto stilts, but it would still be pretty hard for him to convince a salesperson that
he's not a kid. Thus, because a kid cannot hide his age, and because porn is largely
sold face to face,the architectures of real space make it relatively cheap for laws and
norms to be effective.

This constellation of regulations in real space has the effect of controlling, to a
reasonable degree, the distribution of porn to kids. It is not perfect—any child who
really wants the stuff can get it—but regulation does not need to be perfect to be effective. It is enough that these regulations make porn generally unavailable—as they
do in real space.

1 7 4

In cyberspace the regulation of porn is different. The first difference is the market . In real space porn costs mon ey, but in cybers p ace it need not—at least not
much. If you want to distribute one million pictures of "the girl next door" in real
space,it is not unreasonable to say that distribution will cost close to $1,000,000. In
cyberspace distribution is practically free. So long as you have access to cyberspace
and a scanner, you can scan a picture of "the girl next door"and then distribute the
d i gital image ac ross U S E N E T to many more than one mill i on people for just the
cost of an Internet connection.

With this market for supply, much more porn can be produced for cy berspace
than for real space. But there is also the market for demand. Porn in cyberspace can
be retrieved—often and in many places—for free. Not from commercial porn sites,
but from USENET servers, for example. Thus, the constraint of the market is absent
in cyberspace.

More imp ortant than the market, however, is the difference in architectures. A
c rucial fe a tu re that makes reg u l a ti on in real space po s s i ble is the diffic u l ty of d i disguising who you are. In cyberspace there is no fact about your identity to disguise.
You en ter wi t h o ut an iden ti ty, and you iden tify on ly what you want to iden ti f y.
Thus, a kid in cyberspace need not disclose that he is a kid. And therefore he need
not suffer the discriminations applied to a child in real space. No one needs to know
that Jon is Jonny; therefore no one needs to know the necessary preconditions for
applying the restrictions of law, norms, and the market.

The result is what we all know: there are few limits on the distribution of porn

to children in cyberspace. And this fact, in turn, gave birth to the "porn scare."32

Just about the time the Net was coming into the popular consciousness, a parti c u l a rly seedy part of the Net came into vi ew firs t . This was the ex tra ord i n a ry
growth of sex available on the Net. This concern became widespread in the United
States early in 1995.33 Its source was an extraordinary rise in the number of ordinary
users of the Net, and therefore a rise in use by kids and an even more extraordinary
rise in the availability of what many call porn on the Net. An extremely controversial (and deeply flawed) study published in the Georgetown University L aw Review
reported that the Net was awash in porn.34 Time ran a cover story about its availability bi l i ty.3 5 Sen a tors and con gre s s m en were bom b a rded with demands to do som ething to regulate "cybersmut."

Congress responded in 1996 with the Communications Decency Act (CDA). A
law of extraordinary stupidity, it practically impaled itself on the First Amendment.
The law made it a felony to t ransmit "indecent" material on the Net to a minor, or
to a place wh ere a minor could ob s erve it. But it gave spe a kers on the Net a defense—if they took good-faith, "reasonable, effective" steps to screen out children,
then they could speak "indecently."36

There were at least three problems with the CDA, any one of which should have
doomed it to well-deserved extinction.37 The first was the scope of the speech it addressed:"indecency"is not a category of speech that Congress has the power to regulate (at least not outside the context of broadcasting.)38 As I have already described,

1 7 5

Con gress c a n reg u l a te speech that is "h a harmful to minors ," or G i n s berg s peech , but
that is very different from speech called "indecent." Thus,the first strike against the
statute was that it reached too far.

Strike two was vagueness.39 The form of the allowable defenses was clear: so long
as there was an architecture for screening out kids, the speech would be permitted.
But the architectures that existed at the time for screening out children were relatively crude,and in some cases quite expensive. It was unclear whether, to satisfy the
statute,they had to be extremely effective or just reasonably effective given the state
of the technology. If the former, then the defenses were no defense at all, because an
extremely effective block was extremely expensive; the cost of a reasonably effective
block would not have been so high.

S tri ke three was the govern m en t's own doi n g. In arguing its case before the
Su preme Co u rt in 1997, the govern m ent did little ei t h er to narrow the scope of
the speech being regulated or to expand the scope of the defenses. It stuck with the
hopelessly vague, overbroad definition Congress had given it,and it displayed a poor
understanding of how the technology might have provided a d defense. As the Court
considered the case, there seemed to be no way that an identification system could
satisfy the statute without creating an extreme burden on Internet speakers.

But let's step back from the CDA for a moment and clarify just what is possible
in a regulation of this kind. Since the case of Ginsberg v New York, it has been assumed that there is a class of speech that adults have a right to but children do not.
States can regulate that class to ensure that such speech is channeled to the proper
user.

Con ceptu a lly, t h en , before su ch a reg u l a ti on could be app l i ed , t wo qu e s ti on s

must be answered:

1.
2.

Is this speech within the class of "regulable" speech?
Is this listener under a minimum age?

Clearly, the sender is in a better position to answer question one,and the receiver
is in a better position to answer question two. Yet the CDA imposed the full burden
of the regulation on the sender—he must determine both whether his speech is subject to regulation and whether the recipient is above the minimum age.

An alternative would be to place the burden on the receiver—or more precisely,
on his parents. Parents know whether they have children who should be protected
from porn; if they do, they arguably should take steps to block out speech they consider inappropriate for their children.

Both solutions—placing the burden on the recipient or on the sender—require
a new architecture for the Net,not at the level of the TCP/IP protocol, but in the app l i c a ti on space (see ch a pter 8). Both requ i re that ch a n ges be built into the most
common suite of applications in a way that users can depend on.

What might these app l i c a ti ons look like? Let's call the first a zo n i n g s o luti on .
Speakers are zoned into a space from which children are excluded. The second is a

1 7 6

filtering solution. Listeners are empowered to block speech they want to block. We
could describe each as a version of the other—with zoning, people are filtered; with
f i l teri n g, the listen er zones speech . But let's keep the kinds disti n ct and con s i der
what each would require.

A r c h i t e c t u r e s T h a t Z o n e S p e e c h

Two kinds of zoning solutions are conceptually equivalent, but constitutionally distinct. One, that is, is constitutional; the other, not. Both solutions require a change
in the architecture of the Net to facilitate the production of a certain kind of information. One solution requires a signal that the user is a kid (call this a "kids-ID").
The other requires a signal that the user is an adult (call this an "adult-ID").

The difference is crucial, but let's see first how each might work. With the kids-
ID solution, we could imagine the government requiring browser manufacturers to
modify their browsers to p permit users to set up profiles. One option in that profile
would be a check-off box where the user signals that he is a minor. If this check-off
box is sel ected in a profile on a given mach i n e , the other profiles on the mach i n e
would require a password. Many people could share a single machine, but if any of
them were minors,the adult profiles would be secured with a password.

Take an example from a hypothetical family. Say a family of three shares a single
computer. One member of that family is a minor. Using this modified browser, the
adults would set up a profile for each member of the family. With the child's profile,
the kids-ID box would be checked,and a password would be used to access that profile. Any member of the family using the system would select his or her o wn profile
and browse according to the rules of that profile. (Netscape already provides something close to this. With Navigator Communicator 4.5, for example, you can set up
profiles just as I have described, though they do not have a kids-ID option.)

Armed with such a browser, a kid-identified user would then transmit this fact to
a web site when accessing the site. This scheme would require that the web site block
Ginsberg speech to any self-identified minor.40 The burden on the child (or more accurately, the burden on his parents) would be slight, and the burden on the web site
would also be slight.

That is one kind of zoning solution. A second would require the opposite identification: rather than guaranteeing everyone access except those who identify themselves elves as ch i l d ren , this vers i on would grant access to adult material on ly to those
users who could certify that they were adults.

We have seen such a system already: an architecture of digital certificates. Users
wanting to enter a regulable site would have their credentials checked automatically.
Those holding the right certificate would be permitted to enter; those without one
would be denied entry. Web sites would then bear the burden of verifying that certificates were authentic, and would also bear the burden of determining which elements, if any, of their speech were regulable. But they would bear this burden only
when the site had Ginsberg speech.

1 7 7

This second zoning solution is the model of the first CDA and Congress's more
recent (and constitutionally troubled) Child Online Protection Act (COPA).41 The
burden is placed on both the adult site and the adult who wants adult speech. He
must secure an ID; the site must verify the ID.

These two ID systems both effect zoning, but at different costs. One burdens the
p a rents of ch i l d ren sligh t ly and web sites practi c a lly not at all ; the other bu rden s
adults significantly and web sites significantly as w ell.

This difference should be constitutionally significant. It should incline the Court
against upholding a statute like COPA, while disposing it to uphold a statute that requires kid-IDs. If a zoning solution is selected,the Court should uphold the solution
that imposes the least cost on free speech interests.

But both statutes are different from a fil tering soluti on . Both zone the Net according to features of the users.A filtering solution zones the Net according to features res of the speech . Would a zoning soluti on impose fewer costs on free speech
interests than a filtering solution?

A r c h i t e c t u r e s T h a t F i l t e r S p e e c h

The filtering system is a bit more complex, though a rea dy model exists: the architecture of the World Wide Web Consortium's platform for Internet content selection
(PICS).42

We have already seen a relative (actually, a child) of PICS in the chapter abou t
privacy. P3P, like PICS, is a protocol for rating and filtering content on the Net. In
the context of privacy, the content was assertions about privacy practices, and the
regime was designed to help individuals negotiate those practices.

With online speech the idea is mu ch the same. PICS divi des the probl em of fil tering into two part s — l a beling (ra ting con tent) and then fil tering the con tent accord i n g
to those label s . Sof t w a re aut h ors would com pete to wri te sof t w a re that could fil ter according to the ra ti n gs ; con tent provi ders and ra ting or ga n i z a ti ons would com pete to
ra te con ten t . Us ers would then pick their fil tering sof t w a re and ra ting sys tem . If yo u
w a n ted the ra ti n gs of the Ch ri s tian Ri gh t , for ex a m p l e , you could sel ect its ra ting system ; i f I wanted the ra ti n gs of the At h Atheist Lef t , I could sel ect that. By picking our
ra ters , we would pick the con tent we wanted the sof t w a re to fil ter.

This regime requ i res a few assu m pti on s . F i rs t , s of t w a re manu f actu rers wo u l d
h ave to wri te the code nece s s a ry to fil ter materi a l . (This has alre ady been don e —
both Netscape and Microsoft have PICS-compliant filters within their browser software a re.) Secon d , ra ting or ga n i z a ti ons would actively have to ra te the Net . Th i s , of
course, would be no simple task; organizations are only slowly taking up the challenge.43 Third, organizations that rated the Net in a way that allowed for a simple
translation from one rating system to another would have a competitive advantage
over other raters. They could, for example, sell a rating system to the government of
Ta iwan and then easily devel op a sligh t ly different ra ting sys tem for the "government" of IBM.

1 7 8

If all three assumptions held true,any number of ratings could be applied to the
Net. As envisioned by its authors, PICS would be neutral among ratings and neutral
among filters; the system would simply provide a language with which content on
the Net could be rated, and with which decisions about how to use that rated material could be made from machine to machine.44

Neutra l i ty sounds like a good thing. It sounds like an idea that po l i c ym a kers
should embrace. Your speech is not my speech; we are both free to speak and listen
as we want. We should establish regimes that protect that freedom; PICS seems to be
just such a regime.

But PICS contains more "neutrality" than we might like. PICS is not just hori -
horizontally neutral—allowing individuals to choose from a range of rating systems the
one he or she wants; PICS is also verti c a lly n neutral l — a ll owing the filter to be impo s ed at any level in the distri buti onal ch a i n . Most people who first en dors ed the
system imagined the PICS filter sitting on a user's computer, filtering according to
the desires of that individual. But nothing in the design of PICS prevents organizations that provide access to the Net from filtering content as well. Filtering can occur at any level in the distributional chain—the user, the company through which
the user gains acce s s , the ISP, or even the ju ri s d i cti on within wh i ch the user live s .
Nothing in the design of PICS requires that such filters announce themselves.Filtering in an architecture like PICS can be invisible, and indeed, in some of its implementations invisibility is part of its design.45

From a free speech perspective, how should we evaluate these two architectures?
One regi m e — ei t h er the zoning regime of the CDA or the altern a tive kids-ID
regime—requires those who have zonable speech to place that speech behind walls;
the second regime permits listeners to adopt filters that block offending speech. The
blockings of the first follow requirements in a law; the filterings of the second, while
perhaps indu ced by law, fo ll ow from indivi dual ch oi ce . One (zoning) looks like
"censorship"; the other looks like "choice" (PICS). Thus, most p eople emb race the
second while trashing the first.46

But from a free speech perspective, this is exa ctly backward. As a (p perhaps) uni n ten ded con s equ en ce , the PICS regime not on ly en a bles non tra n s p a rent fil teri n g
but, by producing a market in filtering technology, engenders filters for much more
than Ginsberg speech. That, of course, was the complaint against the original CDA.
But here the market, whose tastes are the tastes of the community, facilitates the filtering. Built into the filter are the norms of a community, which are broader than
the narrow filter of Ginsberg. The filtering system can expand as broadly as the users
want, or as far upstream as sources want.

The zoning soluti on is narrower. Th ere would be no incen tive for spe a kers to
block out listeners; the incentive of a speaker is to have more, not fewer, listeners.
The only requirements to filter out listeners would be those that may constitutionally lly be impo s ed —G i n s berg s peech requ i rem en t s . Si n ce they would be impo s ed by
the state , these requ i rem ents could be te s ted against the Con s ti tuti on , and if t h e
state were found to have reached too far, it could be checked.

1 7 9

The difference,then,is in the generalizability of the regimes. The filtering regime
would establish an architecture that could be used to filter any kind of speech, and
the de s i res for filtering then could be ex pected to re ach beyond a con s ti tuti on a l
m i n i mu m ; the zoning regime would establish an arch i tectu re for bl ocking that
would not have this more general purpose.

Which regime should we prefer?
Notice the values implicit in each regime. Both are general solutions to particular problems. The filtering regime does not limit itself to Ginsberg speech; it can be
used to rate,and filter, any Internet content. And the zoning regime is not limited to
facilitating zoning only for Ginsberg speech. The CDA zoning solution could be used
to certify any nu m ber of a t tri butes of the user—not on ly age but citi zenship or
credit-worthiness. The kids-ID zoning solution could be used to advance other child
protective schemes. Both have applications far beyond the specifics of porn on the
Net.

In principle at least. We should be asking, however, what the incentives are to extend the solution beyond the problem. In addition, what resistance is this extended
solution likely to encounter?

Here we begin to see an important differen ce bet ween the two regi m e s . Wh en
your access is bl ocked because of a certi fic a te you are holding, you want to know
why. Wh en you are told you cannot en ter a certain site , the claim to exclu de is
checked at least by the person being excluded. Sometimes the exclusion is justified,
but when it is not, it can be challenged. Zoning, then, builds into itself a system for
its own limitation. A site cannot block someone from the site without that individual knowing it.47

Filtering is different. If you cannot see the content, you cannot know what is being bl ocked . In principle at least, con tent could be fil tered by a PICS fil ter som ewhere upstream and you would not necessarily know this was happening. Nothing
in the PICS de s i gn requ i res truth in bl ocking in the way that the zoning soluti on
does. Thus, upstream filtering becomes easier, less transparent, and less costly with
PICS.

This effect is even clearer if we take apart the components of the filtering process.
Recall the two elements of filtering solutions—labeling content, and then blocking
based on that labeling. We might well argue that the labeling is the more dangerous
of the two el em en t s . If con tent is label ed , t h en it is po s s i ble to mon i tor who get s
what wi t h o ut even bl ocking acce s s . That might well raise gre a ter con cerns than
blocking, since blocking at least puts the user on notice.

These possibilities should trouble us only if we have reason to question the value
of filtering generally, and upstream filtering in particular. I believe we do. But I must
confess that my concern grows out of yet another latent ambiguity in our constitutional past.

Th ere is an undeniable i a ble va lue in fil teri n g. We all fil ter out mu ch more than we
process, and in general it is better if we can select our filters rather than have others
select them for us. If I read the New York Times rather than the Wall Street Journal, I

1 8 0

am selecting a filter according to my understanding of the values both newspapers
bring to the process of filtering. Obviously, in any particular case, there cannot be a
problem with this.

But there is also a value in confronting the unfiltered. We individually may want
to avoid issues of poverty or of inequality, and so we might prefer to tune those facts
out of our universe. But from the standpoint of society, it would be terrible if citizens could simply tune out problems that were not theirs. Those same citizens have
to select leaders to manage these very problems.48

In real space we do not have to worry about this problem too much because filtering is usually imperfect. However much I'd like to ignore homelessness, I cannot
go to my bank without confronting homeless people on the street; however much
I'd like to ignore inequality, I cannot drive to the airport without passing through
n ei gh borh oods that remind me of h ow unequal a nati on the Un i ted States is. All
sorts of issues I'd rather not think about force themselves on me. They demand my
attention in real space, regardless of my filtering choices.

This is not true for everyon e . The very ri ch can cut them s elves of f f rom wh a t
they do not want to see. Think of the butler on a nineteenth-century English estate,
answering the door and sending away those he thinks should not trouble his master.
Those people lived perfectly filtered lives. And so do some today.

But on balance,most of us do not. We must confront the problems of others and
think abo ut probl ems that affect our soc i ety. This ex po su re makes us bet ter citizens.49 We can better deliberate and vote on issues that affect others if we have some
sense of the problems they face.

What happens,then,if the imperfections of filtering disappear? What happens if
everyone can,in effect,have a butler? Would such a world be consistent with the values of the First Amendment?

Some bel i eve that it would not be . Cass Su n s tei n , for ex a m p l e , has argued qu i te
forcefully u lly that the fra m ers em braced what he calls a " Mad i s on i a n" con cepti on of t h e
F i rst Am en d m en t .5 0 This Mad i s onian con cepti on rej ects the noti on that the mix of
s peech we see should solely be a functi on of i n d ivi dual ch oi ce . It insists, Su n s tei n
cl a i m s , on en su ring that we are ex po s ed to the ra n ge of i s sues we need to unders t a n d
i f we are to functi on as citi zen s . It therefore would rej ect any arch i tectu re that make s
con su m er ch oi ce tru m p. Ch oi ce is not a bad circ u m s t a n ce in the Mad i s onian sch em e ,
but it is not the end of the matter. It h i el de Sola Pool makes a very similar poi n t :

What wi ll it mean if a u d i en ces are incre a s i n gly fracti on a ted into small gro u p s
with special interests? What will it mean if the agenda of national fads and concerns is no lon ger ef fectively set by a few mass media to wh i ch everyone is exposed? Such a trend raises for society the reverse problems from those posed by
mass conformism. The cohesion and effective functioning of a democratic society depends upon some sort of public agora in which everyone participates and
where all deal with a common agenda of problems, however much they may argue over the solutions.51

1 8 1

On the other side are scholars such as Geoffrey Stone, who insists just as strongly
that any such paternalistic ideal is nowhere found in the conception of free speech
embraced by our framers.52 The amendment, he says, is merely concerned with banning state control of private choice. Since enabling private choice is no problem under this regime, perfect filtering is likewise no problem.

This is another latent ambiguity, and as with others,I do not think we get far by
appealing to Madison. To use Sunstein against Sunstein, the framers' First Amendm ent was an incom p l etely theori zed agreem en t , and it is bet ter simply to con fe s s
that it did not cover the case of perfect filtering.53 The framers couldn't imagine a
PI C S - en a bl ed worl d ; t h ey cert a i n ly didn't agree upon it. If we are to su pport on e
regime over another, we must do so by asserting the va lues we want to em brace
rather than claiming they have already been embraced.

So what va lues should we ch oose? In my vi ew, we should not opt for perfect fil teri n g. We should not de s i gn for the most ef fic i ent sys tem of cen s ori n g — or at least, we
should not do this in a way that all ows invi s i ble upstream fil teri n g. Nor should we opt
for perfect fil tering so long as the ten dency worl dwi de is to overfilter ter speech . If t h ere is
s peech the govern m ent has an interest in con tro ll i n g, t h en let that con trol be obvi o u s
to the users . O n ly wh en reg u l a ti on is tra n s p a rent is a po l i tical re s ponse po s s i bl e .

Thus, between the two, my vote is for the least transformative regime. A zoning
regime that en a bles ch i l d ren to sel f - i den tify is less tra n s form a tive than a filtering n g
regime that in effect requires all speech to be labeled. A zoning regime is not only
less transformative but less enabling (of other regulation)—it requires the smallest
change to the existing architecture of the Net and does not easily generalize to a far
more significant regulation.

I would opt for a zoning regime even if it required a law and the filtering solution required only private choice. If the state is pushing for a change in the mix of
l aw and arch i tectu re , I do not care that it is pushing with law in one con text and
with norms in the other. From my pers pective , the qu e s ti on is the re su l t , not the
means—does the regime produced by these changes protect free speech values?

Others are obsessed with this distinction between law and private action. They
view regulation by the state as universally suspect and regulation by private actors as
beyond the scope of constitutional review. And, to their credit, most constitutional
law is on their side.

But as I've hinted before, and defend more below, I do not think we should get
caught up in the lines that lawyers draw. Our question should be the values we want
cyberspace to protect. The lawyers will figure out how.

The annoying skeptic who keeps noting my "inconsistencies" will like to pester me
again at this point. In the last chapter, I embraced an architecture for privacy that is
in essen ce the arch i tectu re of PI C S . P 3 P, l i ke PI C S , would en a ble mach i n e - to -
m achine nego ti a ti on abo ut con ten t . With P3P the con tent is rules abo ut privac y
practices,and with PICS it is rules about content. But how, the skeptic asks,can I oppose one yet favor the other?

1 8 2

The answer is the same as before: the values of speech are different from the values of privacy; the control we want to vest over speech is less than the control we
want to vest over privacy. For the same reasons that we disable some of the control
over intellectual property, we should disable some of the control over content.A little bit of messiness, or friction, is a value, not a cost.54

But are these values different just because I say they are? No. They are only different if we say they are different. In real space we treat them as different, and my
only argument is that we choose what we want in cyberspace.

T H E R E G U L A T O R S O F S P E E C H :

D I S T R I B U T I O N

So far my arguments abo ut arch i tectu res have been abo ut arch i tectu res in cyberspace. In this final story, I blur the borders a bit.I want to use the architecture of cyberspace to show something important about the regulation of broadcasting.

The Federal Com mu n i c a ti ons Com m i s s i on reg u l a tes speech . If I wanted to
broadcast a political speech on FM radio at a frequency of 98.6 MHz in Boston, the
FCC would have me prosecuted.55 To speak on 98.6 in Boston I need a license; I do
not have such a license; to speak without a license is a crime. It is a crime despite the
fact that the Constitution says, "Congress shall make no law . . . abridging the freedom of speech, or of the press." What gives?

The answer rests on a deeply held assumption at the core of our jurisprudence
governing broadcasting technologies: only a fixed amount of spectrum is available
for broadcasting, and the only way to facilitate broadcasting is to allocate slices of
the spectrum to users, who are then solely entitled to use their allocated spectrum.
Without allocation, there would be chaos, in which event there would be no broadcasting.

This view first came on the constitutional scene after Congress passed the Radio
Act of 1927.56 In 1926 Secretary of Commerce Herbert Hoover gave up the practice
of con tro lling broadc a s ting after a nu m ber of c i rcuit co u rts held that he did not
h ave the power to do so. If he did not have the power, he said, t h en the invi s i bl e
hand would have to govern. But Hoover was no friend of the invisible hand. He predicted what would happen if radio were left to the invisible hand (chaos), and some
suggest that he helped bring about what he predicted.Stations would override other
s t a ti on s , he said; broadc a s ting would be a mess. Wh en some con f u s i on did ari s e ,
Hoover used this to justify new federal regulation.57

Congress then rode to the rescue by authorizing the FCC to regulate in a mass ively inva s ive way. O n ly the licen s ed could spe a k ; what they said would be contro ll ed by their licen s e ; t h ey had to speak in the public intere s t ; t h ey had to share
their resource with their opponents. In short, Congress said, broadcasting had to be
reg u l a ted in the same way the Sovi et Un i on reg u l a ted its econ omy.5 8 We had no

1 8 3

choice. As Justice Felix Frankfurter said in upholding the regime, it was compelled
by the "nature" of broadcasting.59

From the beginning, however, there have been skeptics—not about the idea that
s pectrum must be reg u l a ted but abo ut the means by wh i ch it is reg u l a ted . Was it
n ece s s a ry to have a cen tral agency to all oc a te property? The com m on law, t h e s e
s keptics argued , h ad done just fine.6 0 Ronald Coase in 1959 propo s ed that if t h e
spectrum were auctioned rather than licensed, it would be allocated to the highest value users.61 Coase's idea caught on—fifty years later. In the United States the FCC
has just begun to auction huge chunks of the broadcasting spectrum. Soon much of
the decision about who gets to say what will be made by private interests—but private interests backed by the force of the state.

Think for a second abo ut the arch i tectu re implied by this devel opm en t . If s pectrum must be all oc a ted , the argument goe s , a govern m ental body should do the all oc a ti on . If this body licen s e s , t h en its ri ght to do so must be ex ten s ive and powerful as
it revi ews the practi ces of l i cen s ees and all oc a tes ren renewals accord i n gly. But even if t h e
govern m ent simply auctions ons spectru m , it must sti ll do ex ten s ive po l i c i n g. Ch a n n el s
must be kept cl e a r; i n interlopers opers must be punished . Un der ei t h er regi m e — l i censing or
a u cti on i n g — both strong govern m ent and a great deal of priva te power are requ i red .
Th ey are ju s ti fied — i n deed com pell ed — by the natu re of broadc a s ting tech n o l ogy.

Many have noticed how different this architecture is from that of the press at the
founding. The "press" in 1791 was not the New York Times or the Wall Street Journal.
It did not comprise large organizations of private interests, with millions of readers
associated with each organization. Rather, the press then was much like the Internet
tod ay. The cost of a pri n ting press was low, the re adership was sligh t , and anyon e
( within re a s on) could become a publ i s h er—and in fact an ex tra ord i n a ry nu m ber
did.62 When the Constitution speaks of the rights of the "press," the architecture it
has in mind is the architecture of the Internet.63

The market has erased this architecture in the print press;nature, we are told,has
eliminated it in broadcasting. And so we are left with a world where the dominant
architectures of free speech are fundamentally different from those the framers embraced.

In chapter 4,I said that architectures could differ both in the values they embrace
and in the regulability of behavior within their space. But here we see a third way in
which architectures differ. As the example of broadcasting shows, architectures differ in the justifications of regulation that they entail. Given an architecture of spectrum all oc a ti on , m ore reg u l a ti on is ju s ti f i ed , s i n ce som eone must make ch oi ce s
about allocation.

So we have an architecture for broadcasting that is fundamentally different from
the framers' design. It justifies a massive amount of state regulation over core areas
of speech. Yet it is an architecture, we are told, that we are compelled to a accept because nature gives us no other choice.Spectrum must be allocated if broadcasting is
to occur.

1 8 4

But what if this assumption were no longer true?64 Whatever the state of radio
technology was in 1927, there's an emerging view that broadcasting today does not
require spectrum allocation. There is a second architecture for broadcasting (which
I will call "Spread Spectrum"—it has a few different names) that would not require
any spectrum allocation at all.65 If broadcasting were done through this technology,
the extensive governmental regulation would no longer be justified.

How could this be? Your intuition about broadcasting is likely to that when two
transmitters transmit on the same frequency, the signals "interfere" with each other
in the sense that both are distorted. But in fact, the distortion we hear is caused by
dumb receivers, not by conflicting signals.A dumb receiver needs a clear channel—
or a clear difference between the channel it is receiving and everything else. If it does
not receive a clear channel, then it does not know which signal to focus on. Thus, it
sounds as if it were moving between the two, as if the transmissions were themselves
mixed.

But a smart receiver could distinguish the tra n s m i s s i on s . It could tell wh i ch it
was to receive and ignore all others, without any coordination of the transmissions.
The only requirement would be an agreement about the protocols for receivers. Receivers would wait until they received the proper packet, and only then would they
open it.

This is the arch i tectu re of the In tern et . Machines have ad d re s s e s ; t h ey co ll ect
f rom the Net packets ad d re s s ed to that mach i n e .6 6 No one all oc a tes a parti c u l a r
channel to your machine; your machine shares the Net with every other machine on
the Net. But the Net has a protocol about sharing this commons. Once this protocol
is agreed on,no further regulation is required.

Broadcasting, many now argue, could be set up the same way. Broadcasts could
be made using a spread spectrum design, and no one would have to allocate a particular bit of s pectrum to a particular sen der. Al t h o u gh this arch i tectu re in ef fect
turns spectrum into a commons, there would be no tragedy of the commons since
the tech n o l ogy of the receivers would reg u l a te their use depending on gl obal demand. Everyone could be a broadcaster.

So here we have an alternative architecture for broadcasting, one that does not
require massive government regulation or state-supported oligopolies like NBC. It is
an arch i tectu re that would fac i l i t a te far wi der use of broadcast spectru m , and it
would put those uses in com peti ti on with other ways of tra n s m i t ting packet s —
copper and gl a s s . All modes of tra n s m i s s i on would com pete with each other, a n d
speakers would have the benefit of the most competitive mode.

Two architectures (spread spectrum and spectrum allocation), two structures of
regulation (small and large), and two structures for industry (small and large broadcasters): Which, we might ask, is more consistent with the First Amendment's design?

Here, finally, we have an example of a translation that works. We have a choice
between an architecture that is the functional equivalent of the architecture of the
American framing and an architecture equivalent to the Soviet framing. One architecture r e e s p e e c h

1 8 5

tectu re distri butes power and fac i l i t a tes speech ; the other con cen tra tes power and
raises the price of speech. Between these two choices, the American framers made a
choice. The state was not to be in the business of licensing speakers either directly or
indirectly. Yet that is just the business that spectrum allocation allows.

A faithful reading of the framers' Constitution, my colleague Yochai Benkler and
I have argued, 67 would strike down the regime of spectrum allocation. 68 A faithful
reading would reject an architecture that so strongly concentrates power. The model
for sp eech that the framers embraced was the model of the Internet—distributed,
noncentralized,fully free and diverse.Of course, we should choose whether we want
a faithful reading—translation does not provide its own normative support. But if
fidelity is our aim, this is its answer.

S P E E C H L E S S O N S

What I de s c ri bed at the start of the book as mod a l i ties of con s traint I have redescribed in this chapter as modalities of protection. While modalities of constraint
can be used as swords against the individual (powers), modalities of protection can
be used as shields (rights).

In principle we might think about how the four modalities protect speech, but I
have focused here on architectures. Which architectures protect what speech? How
does changing an architecture change the kind of speech being protected?

I have not tri ed to be com preh en s ive . But I have pushed for a vi ew that ad d re s s e s
the rel a ti onship bet ween arch i tectu res and speech gl ob a lly and uses con s ti tuti onal va lues to think not just abo ut what is perm i t ted , given a particular arch i tectu re , but also
a bo ut wh i ch arch i tectu res are perm i t ted . Our re a l - s p ace con s ti tuti on should inform
the va lues of our cybers p ace con s ti tuti on . At the least, it should con s train the state in
its ef forts to arch i tect cybers p ace in ways that are incon s i s tent with those va lu e s .

T H I R T E E N

i n t e r l u d e

Let 's pause f or a moment and l ook back over t h ese t h r ee ch apt er s. Th er e is
a pattern to the problems they present—a way of understanding how all three problems are the same.

In one sense,each has asked: How much control should we allow over information, and by whom should this control be exercised? There is a battle between code
that pro tects intell ectual property and fair use; t h ere is a battle bet ween code that
might make a market for privacy and the right to report facts about individuals regardless of that market; there is a battle between code that enables perfect filtering
and architectures that ensure some messiness about who gets what. Each case calls
for a balance between control and no control.

My vote in each context may seem to vary. With respect to intellectual property,
I argue against code that tracks reading and in favor of code that guarantees a large
space for an intellectual commons. In the context of privacy, I argue in favor of code
that en a bles indivi dual ch oi ce — both to en c rypt and to ex press preferen ces abo ut
what personal data is colle cted by others. Code would enable that choice; law could
inspire that code. In the context of free speech, however, I argue against code that
would perfect ly fil ter speech—it is too dangero u s , I cl a i m , to all ow perfect ch oi ce
there. Better choice, of course, is better, so code that would empower better systems
of reputation is good,and code that would widen the legitimate range of broadcasting is also good.

The aim in all three contexts is to work against centralized structures of choice.
In the context of filtering, however, the aim is to work against structures that are too
individualized as well.

You may ask whether these choices are consistent. I think they are, but it 's not
i m portant that you agree . You may bel i eve that a different balance makes sen s e —
more control for intellectual property or filtering perhaps, and less for privacy. My
real interest is in conveying the necessity of such balancing and of the values implicit

i n t e r l u d e

1 8 7

in the claim that we will always require a balance. Always there is a competition bet ween the public and priva te ; a lw ays the ri ghts of the priva te must be balanced
against the interests of the public. Always a choice must be made about how far each
side will be allowed to reach. These questions are inherently questions of public law:
How will a particular constellation of constitutional values be reckoned? How will a
balance be struck in particular factual contexts?

I have argued this point while neglecting ecting to specify who is re s pon s i ble for any
given imbalance. There are those who would say that there is too much filtering, or
not enough privacy, or too much control over intellectual property, but these are not
public concerns unless the government is responsible for these imbalances. Constitutional value in the United States extends only so far as state action extends. And I
have not shown just how state action extends to these contexts.

I do not intend to. In my view, our tradition reveals at least an ambiguity about
how far constitutional values are to extend. In a world where only governments are
regulators, keeping the Constitution's authority limited to state action makes some
s en s e . But wh en the mod a l i ties of reg u l a ti on are mu l ti p l i ed , t h ere is no re a s on to
limit the re ach of con s ti tuti onal va lu e s . Our fra m ers made no ch oi ce abo ut this;
t h ere is no re a s on why reg u l a ti on thro u gh code cannot be inform ed by con s ti tutional values. No argument has been made for why this part of our life should be cut
off from the limitations and protections traditionally provided by the Constitution.
Code stri kes the balance bet ween indivi dual and co ll ective ri ghts that I have
highlighted so far. In the final chapter of part 3, a different balance is struck—one
again made salient by code. However, this time the balance is not between the state
and the individual but between the state and the implicit regulations of the architectures res of c ybers p ace . Now the threat is to a trad i ti onal soverei gn ty. How do we
translate that tradition to fit a world where code is law?

F O U R T E E N

s o v e r e i g n t y

Vi et nam is a Com mu n i st nat i on — one of t h e few r em a i n i n g , and of co u r s e
not anything like the communism that gave birth to the cold war, but nonetheless,it
is a sovereign nation that still links its identity to Marx and Lenin (through Chairman Ho).

The United States is not a Communist nation. Defeated by Vietnam yet a vic tor
in the cold war, we are a nation that in large part defines itself in opposition to the
i deo l ogy of Ma rx and Len i n .1 Vi etnam sets as its ideal the state in servi ce of t h e
withering of the state; the United States sets as its ideal the withered state in the servi ce of l i berty. Con trol is the model of com mu n i s m ; f reedom is the model of t h e
United States.

Or so we are to think.
I confess a certain fascination with Communist states. In the early 1980s I wandered through every European Communist state that would let me in.I spent much
of the summer of 1996 wandering through Vietnam. Alone and e-mail-free, I tried
to understand this place that in my ch i l d h ood fell vi ctim to my nati on's ex ported
struggle with the cold war.

I 've been to many place s — traveling is a hobby of m i n e — but never to a place
more spectacular. One is always overwhelmed by forgiveness,and an American can't
h elp being overwhelmed el m ed by this nati on's warmth and wel com e . Perhaps had we
" won" the war for giveness would not be so fort h com i n g. But it app a ren t ly com e s
easily to those who did win.

I was not there to understand forgiveness,however, but to learn something about
how the place ran. I wanted to understand how this state exercises control over its
citizens; how it continues to regulate; how it qualifies as one of the last remaining
Communist states. So I spent time talking to lawyers, businessmen,and managers of
the em er ging Net in Vi etnam ("Net Na m" ) . Very qu i ck ly, a su surprising pictu re
emerged.

1 8 9

Though Vietnam is a "Communist" state whose ideology, as understood in the
West, admits very little limitation on the power of the state; though the Vietnamese
state sets as its ideal a common good rather than the good of individuals or individual liberty; though on paper there is no "liberty"in Vietnam in the sense that we in
the West like to imagine it—though all this is true,I could not escape the feeling that
people in Vietnam, in their day-to-day existence, are far less "regulated"than people
in the United States. Not all people, of course: political opponents undoubtedly feel
the power of the state quite forcefully. But I sensed that ordinary people in their ordinary lives, many running small shops, had no conception of the control that govern m ent can exerc i s e ; no ex peri en ce of h aving their wages reported to a cen tra l
bu re a u c racy on ce a qu a rter; no understanding of what it is like to live under the
(relative) efficiency of the regulation we have here.Life there is remarkably free from
governmental control. It was hard to imagine how it would have been different had
Nixon won the war. Pornography was banned and hippies were harassed, but in the
m a i n , people and business got on with very little direct or ef fective reg u l a ti on by
government.

This fact (if you'll allow random observations of an untrained anthropologist to
count as fact) is not hard to understand. The "law" on the books in Vietnam may or
may not be a stricter or more extensive regulator than the "law"in the United States.
But the architecture of life in Vietnam clearly makes any real regulation by the state
impossible. There is no infrastructure ructure of control—there is barely any infrastructure
at all . Wh a tever the reg u l a ti ons of the state may be , t h ere is no arch i tectu re that
could make them ef fective . Even if t h ere is more reg u l a ti on there than here (and
frankly I doubt that there is), Vietnam has an effective "freedom."

This makes perfect sense. The power to regulate is a function of architecture as
much as of ideology; architectures enable regulation as well as constrain it. To understand the power a government might have, we must understand the architectures
within which it governs.

The preceding chapters have all been about this very point. We can have an idea
of sovereign power—the right of the sovereign to regulate or control behavior—but
our idea is meaningful only when we place it within a particular regulatory context,
or within particular arch i tectu res of con tro l . The state's power may be "a b s o lute ,"
but if the architecture does not support regulation,the state's effective power is quite
slight. On the other hand, the state's power may be limited, but if the architectures
of control are very efficient, this limited power can be extraordinarily extensive. To
understand a state's power to regulate we must ask: How well does its infrastructure
support a structure of regulation?

This is the qu e s ti on we should ask abo ut the reg u l a ti on of c ybers p ace — a bo ut
sovereignty there. We should ask this question first about real-space governments:
What power do they have to regulate life in cyberspace? How does the architecture
of cyberspace support the regulation of real-space governments there? And then we
should ask it about the "sovereignty" of cyberspace itself.

1 9 0

In the end,I want to argue that there is a sovereignty in cyberspace; that this sovereignty competes with real-space sovereigns; and that control of that sovereign is
essential if we are to achieve democratic control over an extraordinarily important
aspect of real-space life. Real-space life, not just cyberspace life,since in the end,and
in the beginning, life there is always also life here.

T H E S O V E R E I G N O F T H E S P A C E

Cyberspace is a place. People live there. They experience all the sorts of things that
they experience in real space there. Some experience more. They experience this not
as isolated individuals playing some high-tech computer game. They experience it in
gro u p s , in com mu n i ti e s , a m ong stra n gers , and among people they come to know
and sometimes like—or love.

While they are in that place, cyberspace, they are also here. They are at a terminal screen, eating chips, ignoring the phone. They are downstairs on the computer,
late at night, while their husbands are asleep. They are at work,at cyber-cafés,and in
computer labs. They live this life there, while here,and then at some point in the day
they jack out and are only here. They rise from the machine,in a bit of a daze, and
turn around. They have returned.

So where are they when they are in cyberspace?
We have this desire to pick. We want to say that they are either in cyberspace or
in real space. We have this desire because we want to know which space is responsible. Which space has jurisdiction over them? Which space rules?

The answer is both. Whenever anyone is in cyberspace, she is also here, in real
space. Whenever one is subject to the norms of a cyberspace community, one is also
l iving within a com mu n i ty in real space . You are alw ays in both places if you are
there, and the norms of both places apply. The problem for law is to work out how
the norms of the two communities are to apply given that the subject to whom they
apply may be in both places at once.

Think again about Jake Baker. The problem with Jake was not that he went to a
different place where the norms were different. The problem was that he was simultaneously in a Michigan dorm room and on the Net. He was subject to the norm of
civility in the dorm, and he was subject to the norm of indecency in cyberspace. He
was subject, that is, to two sets of norms as he sat in that single chair.

So whose norms would apply? How would real-space governments deal with the

conflict between these two communities?

Some examples might help. Ordinarily, when you go to Europe you do not bring
the federal government with you.You do not carry along a set of rules for Americans
while in Europe. In Germany you are generally subject to German law. The United
S t a tes ord i n a ri ly has very little re a s on to worry abo ut reg u l a ting your beh avi or
there—so long, at least, as you are there.

1 9 1

But sometimes the U.S. government does have a reason to regulate American citizens abroad. When it does, nothing in international law can stop it.2 For example,
there are jurisdictions where pedophilia is not regulated. For a time they became target to u rist spots for pedophiles from around the worl d . The U. S . govern m en t , i n
1994,passed a law to forbid Americans from engaging in child sex while outside the
United States, even in jurisdictions where child sex is permitted.3

What justification could the re have been for such a law? Obviously, the sense of
Congress was that if a person engages in such behavior in a foreign country, they are
more likely to do it here as well. If they visit a community where the norms permit
such behavior, they are more likely to carry those norms back to their life here. Thus,
while the American government generally doesn't much care what you do elsewhere,
it does begin to care wh en what you do el s ewh ere has an ef fect on your life here .
When it does, it will regulate your life elsewhere.

Regulations like this are the exception, of course, but only because the threat of
these altern a tive com mu n i ties is rel a tively sligh t . The fri cti ons of re a l - s p ace life
make it less likely that the norms of an alien culture will bleed into our own; the distance between us and alien cultures is so great that very few can afford to have a life
in both places.

But the Net changes this. As the Baker case suggests,and as any number of other
cases will press, with cyberspace these other communities are no longer elsewhere.
They can be brought home, and real-space communities no longer have the buffer
of friction to protect them. Another community can now capture the attention of
their citizens without their citizens' ever leaving. People may be in both places at the
same time. The question for government is how far to allow this alien force to go.

In an important sense,this is a very old story. Cultures at one time isolated are later
invaded when the barriers to invasion fall. Think about the plea from Europeans to
stop the invasion of American culture, which pours over satellite television into the
living rooms of European citizens.4 Or even more extreme, the Middle East. These
are places that have for some time been thinking about the barriers they might erect
to protect their culture from the invasions of an alien culture.

S ti ll , t h ere is a differen ce here . The inva s i ons these cultu res resist are rel a tively
passive. Dallas and Baywatch5 are not sets of rules that people in Hungary or Singapore must follow. They display a certain (im)moral universe, which Hungarians and
Singaporeans are able to see. But they don't draw people into a different form of life.
The alternatives offered by TV are alternatives of the imagination. But the interactive life of cyberspace offers more than watching: it offers alternative ways of living
(or at least some cyberspaces do).

Thu s , the story is old, but as with each latent ambi g u i ty, the twist is new. Th e
question now is not just about what powers a state should have given that its citizens
can travel; the question is about what power a state should have given that its citizens can live in two places at once.

1 9 2

How can govern m ents accept these altern a tive ways of l iving while the peop l e

living them are also living within the jurisdiction of these governments?

We should begin by putting the problem in context.

"Soverei gn ty " is the soverei sovereign's power to set rules that govern the beh avi or of
people rightfully within its reach. The power to set rules—for of course I could affect people's behavior simply by stalling a bus in a busy intersection. And the power
rightfully to set rules—for an invading army might set rules, but that wouldn't necessarily make the invader a sovereign.

Beyond this minimu m , the con cept has under gone significant ch a n ge . At on e
time "logic" said that you could be subject to only one sovereign at a time.6 Anything
el s e , it was though t , vi o l a ted the very idea of "s overei gn ty." But the Un i ted State s
changed that. In the United States, citizens are subject to two sovereigns at the same
time—the nation and the state.Dual sovereignty is our contribution to the theory of
sovereignty. However radical it was at the founding, it is now quite commonplace in
sovereignty talk.

But dual sovereignty creates its own problems. How do dual sovereigns deal with
the probl em of con f l i cting aut h ori ty? In matters of ju s ti ce as well as of con s ti tuti onal po l i ti c s , dual soverei gns must have a simple way to re s o lve con f l i cts in authority.

In the United States these conflicts are resolved by the principle of supremacy:
when proper laws of the federal government conflict with proper laws of the states,
the federal laws prevail.7 By design, these conflicts were to be infrequent, but if in
practice they emerged, the U.S. Constitution provided a simple resolution.

But as conflicts among laws from outside a single sovereign (or outside a structure re of dual soverei gn ty) grow in nu m ber and sign i f i c a n ce , a n o t h er probl em
emerges. People have never really been subject to the laws of only one sovereign. Behavior across borders, or behavior that had effects across borders, has always risked
running afoul of com peting ru l e s . As the integra ti on of i n tern a ti onal life has inc re a s ed , so have these con f l i ct s . Beh avi or has ef fects in many place s ; h ow many
p l aces legi ti m a tely have a claim to reg u l a te in these spaces? How, in other word s ,
could it be just that a single act is subject to the control of many sovereigns?8

Cyberspace has exploded this third stage of the debate. What was once the exception will become the rule. Behavior was once governed ordinarily within one juri s d i cti on , or within two coord i n a ting ju ri s d i cti on s . Now it wi ll sys tem a ti c a lly be
governed within multiple, noncoordinating jurisdictions. How can law handle this?
This question has produced a ferocious argument between two extremes. At one
end is the work of David Post and David Johnson. Johnson and Post argue that the
mu l ti p l i c i ty of ju ri s d i cti ons in wh i ch your beh avi or is su bj ect to reg u l a ti on (since
a nything you do in cybers p ace has an ef fect in every other con text) should mean
that much behavior is presumptively not subject to regulation anywhere. Anywhere,
that is, save cyberspace.9 The inconsistency of any other solution, they argue, would

1 9 3

be absu rd . Ra t h er than em bracing the absu rd , we should em brace som ething far
more sensible: life in cyberspace, as Milan Kundera might put it, is life elsewhere.

At the other extreme is the work of scholars such as Jack Goldsmith, who claims
there is nothing new here.10 For many years the law has worked through these conflicts cts of a ut h ori ty. Cybers p ace may increase the inciden ce of these con fli ct s , but it
does not change their nature. Old structures may have to be molded to fit this new
form, but the pattern of the old will suffice.

While both sides embrace partial truths,in my view both are mistaken. It is true,
as Johnson and Post argue, that there is something new here. But what is new is not
a difference in kind, only a difference in degree. And it is true, as Goldsmith argues,
that we have always had disputes of this form. But we have not had conflicts at this
level of actor. We have not had a time when we could say that people are actually living in two places at once, with no principle of supremacy between them. This is the
challenge that we will face in the future.

This du a l i ty is a probl em because the legal tools we have used to re s o lve these
questions before were not designed to deal with conflicts among citizens. They were
designed to deal with conflicts among institutions, or relatively sophisticated actors.
They are rules made for businesses interacting with businesses, or businesses interacting with governments. They were not designed for disputes between citizens.

Jessica Litman makes an analogous point in her work on copyright.11 For much
of the last century, Litman argues, copyright has worked fairly well as a compromise
between publishers and authors. It is a law that has largely been applied to instituti on s . In d ivi duals were essen ti a lly out s i de copyri gh t's purview ew since indivi duals
didn't really "publish."

The Internet, of course, changes all this. Now everyone is a publisher. And Litman argues (convi n c i n gly, in my vi ew) that copyri gh t's rules do not nece s s a ri ly
work well when applied to individuals.12 More precisely, the ideal rules for individuals would not necessarily be the ideal rules for institutions. The rules of copyright
n eed to be reform ed to make them bet ter su i ted to a world wh ere indivi duals are
publishers.

The same is true of con f l i cts bet ween soverei gn s . The rules for dealing wi t h
these con f l i cts work well wh en the parties are repeat players — corpora ti ons that
must do business in two place s , for ex a m p l e , or indivi duals who con s t a n t ly travel
bet ween two place s . These people can take steps to con form their beh avi or to the
l i m i ted ra n ge of con texts in wh i ch they live , and the ex i s ting rules help them to
that en d . But it does not fo ll ow (as it does not fo ll ow in the con text of copyri gh t )
that the same mix of rules would work best in a world wh ere anyone could be a
mu l ti n a ti on a l .

The solution to this change will not come from insisting either that everything is
the same or that everything is different. It will take more work than that. When a
large number of citizens live in two different places,and when one of those places is
not solely within the jurisdiction of a particular sovereign,then what kinds of claims

1 9 4

should one sovereign be able to make on others, and what kinds of claims can these
sovereigns make on cyberspace?

This question is not yet answered. It is another latent ambiguity in our Constitution's past—but in this case there is no founding international constitutional moment that could have answered the question. Even if there had been, it would not
have answered this question. At the founding ordinary people were not routinely living in multiple noncoordinating jurisdictions. This is something new.

Th ere are alre ady some examples of h ow the law deals with con fli cts bet ween the
norms of the virtual community and the rules of the real-space community. What
lesson can we learn from these?

"Hackers" are an obvious first example.Originally, hackers were relatively harmless cyber-snoops whose behavior was governed by the norms of the hacker community.13 A hacker was not to steal; he was not to do damage;he was to explore,and
if he found a hole in a system's security, he was to leave a card indicating the problem.14 He was a bit more invasive than a security guard, who checks office doors to
make sure they are locked. The hacker of this earlier era not only checked the locks
but let himself in, took a quick peek around, and left a cute (or sarcastic) note saying, in effect,"Hey, stupid, you left your door open."

All this may seem qu i te bi z a rre to yo u . But you have to put yo u rs el f i n to the cultu re
of the early Net to understand (and hen ce to have the ri ght to ju d ge) this beh avi or. At
this early stage the Net was a world of open sof t w a re and open sys tem s . The basic opera ting sys tem was some flavor of U N I X , an open (as in tra n s p a rent) sys tem that had
m a ny different vers i ons brewing on different parts of the Net .1 5 As in any evo luti on a ry
m odel , these vers i ons were gen eti c a lly rel a ted but sligh t ly differen t . Hackers took on
the role of s n snooping abo ut to sniff o ut probl ems with the evo lving gen etic code .

This was also a world where terribly valuable stuff was not really "on the Net."
Sep a ra te net works for defense and fin a n ce were not part of the In tern et proper.1 6
While some famous efforts were made to hack those places, most hacking was benign.17 People within the hacking community understood the benefit of their naggingly smart invasions.

That was the world that was. It didn't take much to see that this world would not
survive for long. This community of people who thought it fair to test the locks, enter someone else's machine if they could, and snoop their file structure—this commu n i ty was not going to mesh with a Net wh ere com m erce could su rvive . It may
have been fine to play these games in a world of geeks, but when money came online a better system of security was inevitable.

As these cultu res came into con f l i ct , re a l - s p ace law qu i ck ly took side s . L aw
worked rut h l e s s ly to kill a certain kind of online com mu n i ty. The law made the
hackers' behavior a "crime," and the government took aggressive steps to combat it.
A few prom i n ent and well - p u bl i c i zed cases were used to redefine the hackers'
"h a harmless beh avi or " i n to what the law would call "c ri m i n a l ." The law thus era s ed
any ambiguity about the "good"in hacking.

1 9 5

A good example of this is the story of Robert Tappin Morris, a graduate student
at Corn ell .1 8 Morris was stu dying In tern et mail—the pro tocols that govern the
transfer of mail between two computers on the Net—when he discovered,and then
exploited, flaws in two programs that were and still are widely used to transfer mail
and information about users: Sendmail and Fingerdaemon. Morris was convinced
that both left open certain doors on the system, thereby allowing people to use the
pro tocols for improper purpo s e s . The pro tocols govern ed , for ex a m p l e , wh en a
computer would open its d oor to allow mail to be deposited onto its disk, but they
had no good way to distinguish between knocks on the door by postmen and knocks
by burglars.

In real space , i f you discover that the door of the local bank is unlocked , yo u
m i ght simply call the bank (if yo u're a decent sort ) , or maybe the po l i ce , and let
t h em know. If you discover a certain flaw in sof t w a re made by Novell , you migh t
send a letter to Novell. But when you discover a flaw in Sendmail, it's not so clear
what to do. Sen d m a i l , the dominant program for distri buting mail on the Net , i s
free.19 Sites have an incentive to keep the program up to date, but because doing so
can be difficult and ti m e - con su m i n g, most do not update the program until they
h ave had a scare . And a scare comes best from a dem on s tra ti on . A sel f - re s respecting n g
h acker d em o n s tra te s a probl em , but in a very particular way. He shows what is
wrong, but without doing any harm.

That was Morris's aim. He used a worm—which, you remember, is a bit of code
spit onto the Net and designed to copy itself over and over, without affecting the operation of anyone's machine. Its purpose is simply self-replication. It does not aim to
do any particular damage . It simply attaches itsel f to e-mail messages and thu s
copies itself everywhere,so that at a certain point its author can declare: "See, I told
you. There's a hole in Sendmail and in Fingerdaemon."

But things didn't quite go as planned. The worm was not as harmless as Morris
thought. He had made it multiply much too fast, and very soon it was clogging the
whole Net. It had c opied itself so many times that it froze the ma chines exposed to
its spread. Machines by the hundreds were taken down, and thousands of dollars of
damage incurred. Morris tried quickly to stop the mess he had started, but he didn't
start quickly enough. The worm won; Morris lost.

It was not hard to find the culprit; too many people knew of Morris's plan. He
was charged with violation of the Computer Fraud and Abuse Act of 1986, a federal
law that made it illegal to access intentionally "federal interest computers" without
authorization if that access damages or prevents authorized use of those computers
causing a loss of more than $1,000.20 Morris was convicted and sentenced to three
years' probation, four hundred hours of community service, and a fine of $10,050
plus the costs of his supervision.21

The government had an objective—to vilify the hacker. Its aim was to turn the
hacker into a criminal. And thus, rather than reading any lenity into the statute, the
government insisted that it be applied strictly—not only against Morris but against
a scad of other high-profile hackers as well. This was a war whose aim was to remake

1 9 6

the hacker community into outlaws. Phiber Optik,22 David LaMaccia,23Steve Jackson Games,24 and others were the victims of this war. Real-space communities could
not tolerate these sorts in their midst. So the hackers were banished.25

Should this be our standard response? Does life in cyberspace have no legitimacy
against the view of real-space sovereigns? Does it have no claim? If it should, how
could it make its claim? What would be its power?

The fate of the hackers is an example of real-space law taking over when cyberspace
and real-space communities conflict. The example se ems to say that real space will
necessarily win this conflict—that cyberspace cannot bend the rules of real space. I
don't believe that is true. Cyberspace will have an effect. For all the prominence of
these efforts at reclaiming real-space sovereign authority, they are dwarfed by the examples of real-space sovereigns losing regulatory power and effect. Real-space soverei gns are in com peti ti on with cybers p ace and, l ong before they re a l i ze it,
cyberspace will have won.

To see how, we must look to how emerging architectures in cyberspace change
effective regulation. The simplest example, but not the most significant, is one we
have seen in the context of free speech. A nation in 1980 might have had fairly effective control over what was published within its borders. The government, for example, might be fairly confident that no newspapers would be too critical, since it
could effectively punish its critics. State television would be under government contro l . The state could not re a lly con trol what people said on tel eph on e s , but tel eph ones were too cru de , and the audien ce too small , to matter. The mix of
architecture and law in this hypothesized state kept speech effectively regulated.

The Internet changed this mix. Now there can be speech critical of the government without governmental sanction. Publishing can go on without government interven ti on . The ef fective reg u l a ti on of s peech has ch a n ged . The va lues of t h e
Internet—the free speech built into its architecture—now trump the values of control that our hypothetical nation embraced.

But this is just the most obvious example. Consider some others.
Im a gine a nati on with a well - devel oped balance of ri ghts built into its law of
contract. These rights protect consumers in some cases; they set the terms for business relations in others. Some of these rights are default,in the sense that the parties
could agree to change them. But some are mandatory for a certain class of contractor or for a certain kind of contract.26 (Many U.S. cities, for example, require a standard landlord-tenant agreement for apartment rentals.)

These rules of contract law would be effective in real space to define the rights of
one individual making a claim against another. The enforcement of any contract in
this space would be subject to these rules.

Enter cyberspace, where the architecture of interaction, or the architecture of a
p a rticular cybers p ace , determines a host of rules abo ut con tract s . These ru l e s —
a bo ut how an of fer is accepted , wh en it is ef fective , h ow it can be cancel ed , wh a t
terms must be bargained for, whether terms are enforceable, whether there must be

1 9 7

a wri t ten agreem en t , and so on — m ay or may not be con s i s tent with the con tract
rules of a particular jurisdiction. But a citizen from a particular jurisdiction can now
en ter into an agreem ent su bj ect to these term s . These terms governing the agreement are the effective rules of contract for that particular agreement,and if they are
inconsistent with the rules of the local jurisdiction from which the person comes,
t h en so mu ch the worse for the local ru l e s . The terms of the con tract are those
agreed to in the text of the agreement, or implicit in the architecture that regulates
dealings about the agreement.

One might say this is nothing new. One might say, fo ll owing Goldsmith, t h a t
people have always been able to enter into international agreements.27 These agreements have always implied a choice of law, and the law chosen may or may not be
consistent with local law. If it is inconsistent,then there are restrictions on a local jurisdiction's ability to enforce it against a local citizen. So the same structure would
constrain in this context.

But this analytical similarity should not obscure a substantive difference. Again,
i n tern a ti onal agreem ents for the most part are agreem ents bet ween soph i s ti c a ted
actors. Before cyberspace, ordinary consumers were not international actors. We can
assume that sophisticated actors are able to defend themselves against rules inconsistent with their interest, or with the requirements of their local jurisdictions. Consu m ers , i n d ivi du a l s , and ord i n a ry cyber- con tractors are not in the same po s i ti on .
When people lack the competence or advice to negotiate effectively, the effect is to
shift control over such agreements from local courts and administrators to whatever
rule is built into the code. Thus, local governments lose control over the rules and
the effective rule-maker shifts to cyberspace.

A third example pushes the public law dimension of this conflict more strongly.
Think again about copyright law. The law of copyright establishes a set of rights that
individuals have against the copyright owner. We have seen these described in chapter 10, but for convenience, we can lump them under the label "fair use." There is
some controversy in the Unit ed States about the extent to which fair use rights can
legitimately be modified by contract. In an important opinion, Judge Easterbrook of
the 7th Circuit Court of Appeals said,in effect,that these rights can plainly be modified through contract.28 Thus, if you buy a piece of copyrighted work and promise
to waive your rights of fair use,that promise, on this theory, can be held against you.
E a s terbroo k's con clu s i on might well make sense in real space , wh ere there are
real costs to contracting. In real space these costs prevent most copyrighted material
from being wrapped in these anti–fair use agreements. The cost of real-space contracting creates a balance, tilting the result toward the protection of fair use.

But in cyberspace—especially when we consider the international dimensions to
cyberspace—this balance is again skewed. If it becomes one of the rules of the space
to click away fair use rights, then the balance of property and fair use so important
to copyright's very design becomes skewed. Again, the architecture, and the rules it
makes possible, conflict with real-space regimes. Once again, real-space sovereigns
must decide how far they will allow this conflict to reach.

1 9 8

Con tract and copyri ght are not the on ly laws that wi ll com pete with the code of c ybers p ace . Think abo ut the rules of access thro u gh the mail, and its equ iva l ent in cybers p ace ,e - m a i l . In real space , even in ga ted com mu n i ti e s , the mail gets thro u gh . Yo u
can send adverti s em ents or po l i tical com m en t a ry to people within these com mu n i ti e s .
Rules abo ut trespass and priva te property might bl ock you from en tering the com mun i ty and leafleting door to door.2 9 But in real space you can use the mail.3 0

In cy berspace gated communities are different. The code of AOL, for example,
gives su b s c ri bers tools that filter adverti s em ents or bl ock messages from certain
people or servers. The rules about access in that space are different from the rules
about access in this space.

So what? Again, the skeptic insists, the rules of contract law in Denmark are not
the same as in Dallas. Why should the fact that two places have different rules mat -
ter any more, or less?

The key again is simultaneity, and here again, the metaphor of space is confusing. Ordinarily, you are in one space at a time, and when there are two sets of rules,
this real-space rule offers an acceptable resolution. The rules for gambling are different in Nevada and in New Mex i co ; c i ti zens from New Mex i co must travel to
Nevada to spend an evening subject to Nevada's rules. From the perspective of New
Mexico, that might not be ideal, but it is not terrible.On balance,the opportunity to
escape is not without cost,so there will not be so many of these escapes as to offend
New Mexico's regulatory objectives.

But recall Jake Baker. The problem with Baker was that while he was in one place,
he was living under the rules o f a second. While in Ann Arbor, he was living within
the norms of a radical community in cyberspace.Or forget Jake Baker (what a relief
that would be); think about the wife having an affair with someone "in cyberspace."
Can she really say to her husband,"That is there,this is here"? Couldn't he rightfully
say—"Look, even if you are there, you are also here." Should we really view the effect
of life in cyberspace as irrelevant to life here?31

To the extent that architectures in cyberspace are rules that affect behavior, the space
is sovereign.32 In the sense that any set of normative commitments is sovereign, cybers p ace is soverei gn . But this soverei gn ty produ ces perpetual com peti ti on . Th e
rules that govern cyberspace may be different from those that govern real space. As
the rules that govern real space compete, cyberspace increasingly wins out. It is the
norms, the freedom, the rules, and the law of the place that in an increasingly large
range of cases govern the norms, the freedom, the rules, and the law of people also
living here.

Th ere is little qu e s ti on abo ut how re a l - s p ace soverei gns wi ll re s pond to this.
They will come to see that the power of another sovereign is wired into their telephones,and they will struggle (as the United States has done with the hackers) as the
rules and norms of this other sovereign affect the behavior of their citizens in their
s p ace . Th ey have the tools at their disposal to resist the arch i tectu re of the Net to
protect their regulatory power.

1 9 9

But now I want to make a stronger claim: not only can the government take these
steps to reassert rt its power to regulate, but that it should. Government should push
the architecture of the Net to facilitate its regulation, or else it will suffer what can
only be described as a loss of sovereignty.

This is not some blind paean to government. In fact, I am not concerned about
"government" at all. My concern is accountability—these architectures and the values they em bed should be arch i tectu res and va lues that we have ch o s en . Th ey are
political in the most ordinary way: they are structures that order real life, and they
ought therefore to be structures that we have in some sense chosen.

In some sense—but which sense? From the bottom up or the top down?33 From
el ected officials dict a ting the terms of code? Or from wi red indivi duals ch oo s i n g
their own sets of code? Here ultimately is the hardest problem that cyberspace will
present. But to see its complexity, we must put it in context.

Our history of self-government has a particular form, with two importantly contingent fe a tu re s . Before our fo u n d i n g, l i fe was geogra ph i c a lly based—a nati on was a
society located in a physical space, with a single sovereign allegiance. As I've mentioned, the conceptual revolution of the American republic was that citizens could
h ave two soverei gn s — m ore prec i s ely, that they (as the ulti m a te soverei gn) co u l d
vest their soverei gn power in two different del ega te s . Th eir state govern m ent was
one delegate, the federal government was another; individuals living in a single geogra phic loc a ti on could be citi zens of both govern m en t s . That was the idea of t h e
founding document, and the Fourteenth Amendment made it explicit: "All persons
born or naturalized in the United States,and subject to the jurisdiction thereof, are
citizens of the United States and of the State wherein they reside."

Citizenship in this sense did not always mean a right to contribute to the selfgovernment of whatever community you were a citizen of.34 Even today children are
citizens but they have no right to vote. For those recognized as members of civil and
political society, citizenship is an entitlement: it is a right to participate in the governing of the po l i tical com mu n i ty of wh i ch they are mem bers . As a citi zen of t h e
United States,I have the right to vote in U.S. elections; as a citizen of Massachusetts,
I have the right to vote in Commonwealth of Massachusetts ele ctions. And I have
both rights at the same time.

At this level,the link between entitlement and geography makes sense. But as we
work down the hierarchy of "communities," it makes less sense. As we move down
the ch a i n , wh ere I live seems less and less determ i n a tive of m em bers h i p. I am a
member of the Boston community, yet because I live in Cambridge,I have no right
to parti c i p a te in the govern a n ce of Bo s ton . If I moved aw ay from Ca m bri d ge yet
continued to work here, I would have given up my right to participate in the governance of Cambridge, even though I would continue to have an extremely strong interest in Cambridge and its development.

Po l i tical theorists have noted this probl em for some ti m e .3 5 S ch o l a rs su ch as
Richard Ford have contributed significantly to the view that we need a way to un-

2 0 0

derstand com mu n i ty and the ri ght to parti c i p a te in its govern a n ce that is not directly tied to geography.

These troubles with geography at the local level are nothing, however, compared
with the problem in cyberspace. No one really lives in cyberspace; people who are
"in" cyberspace are always also "in" real space. That they are in cyberspace should
entitle them to some say over its architectures, and that they are in real space should
give their real-space communities a right to some control over the architectures in
cyberspace, at least to the extent that cyberspace architectures have an effect on the
citizens in real space.

But why? Why do real-space citizens need to have any control over cyber-places
or their architectures? You might spend most of your life in a mall, but no one would
say you have a right to control the mall's architecture.Or you might like to visit Disney World every w eekend, but it would be odd to claim that you therefore have a
right to regulate Disney World. Why isn't cyberspace like a mall or a theme park?

Your relationship to a mall, or to Disney World, is the relationship of consumer
to merchant a n t . If you don't like two - a ll - beef - p a t ti e s - s pec i a l - s a u ce - l et tu ce - ch ee s e -
pickles-onions-on-a-sesame-seed-bun,then you can go to Burger King; McDonald's
has no duty to let you vote on its hamburgers. If you don't like the local mall, you
can go to another. The power you have over these institutions is your ability to exit.
Th ey com pete for your atten ti on , your custom , and your loya l ty; i f t h ey com pete
well , you wi ll give them your custom ; i f t h ey don't , you wi ll go som ewh ere el s e .
What makes this sys tem work , t h en , is the com peti ti on among these po ten ti a l
sources for your custom.

This part of our life is cru c i a l ; it is wh ere we spend most of our ti m e . Most peop l e
a re more sati s fied with this part of t h eir lives than they are with the part within wh i ch
t h ey get to vo te . In a sen s e , a ll these places are govern m en t s ; t h ey all impose rules on
u s . But our reco u rse under the rules of the market is to take our business el s ewh ere .

Still, an important part of our life is not like this. There are no states that say to
their citizens—you have no right to vote here; if you don't like it, leave. At least no
democratic state does this.Our role in relation to our governments is that of a stakeholder with a voice. We have a right—if the government is to be called democratic—
to participate in its structuring.

And not just governments. It would be an odd university that gave its faculty no
right to vote on issues central to the university (though it is an odd corporation that
gives its employees a right to vote on issues related to employment). It would be an
odd social club that did not give members some control over its functions—though
again, there are such clubs, just as there are nondemocratic governments. The point
is not that we have this relationship with most of the organizations in our lives, or
even with the most important ones. The point is that much of our lives are spent in
these two alternative modes—either as consumers, or as members.

Some theorists have tried to collapse these two modes into one. Some have tried
to carry the member model into every sphere of social life—the workplace,the mall,
the local pub.36 Others have tried to carry the consumer model into every sphere of

2 0 1

social life—followers of Charles Tiebout, for example,have tried to explain competi ti on among govern m ents along the lines of the ch oi ces we make among too t toothpastes.37 But even if we cannot articulate perfectly the justifications for treating these
choices differently, it would be a mistake to collapse these different spheres into one.
It would be hell to have to vote on the design of toothpaste, and tyranny if our only
recourse against a government we didn't like was to move to a different land.

Some have non et h eless urged that we think of c ybers p ace in the con su m er
mode. If we don't like a particular cyber community, we can move—far more easily,
in fact, than we can in real space. Because exit is so cheap, we should use exit as our
ballot. Some communities in cyberspace can choose to make members, others not;
architectures in cyberspace can be constructed with little worry about sanction from
real space. The world of cyberspace would become a vir tual menu, and if you don't
like one selection, you simply pick something else.

The best work in this line are the writings of David Post and his sometime coauthor David Johnson.38 Post's article "Anarchy, State, and the Internet" best sets the
stage here. Communities in cyberspace, Post argues, are governed by "rule-sets." We
can understand these rule-sets to be the requirements, whether embedded in the architecture or promulgated in a set of rules, that constrain behavior in a particular
place. The world of cyberspace, he argues, will be composed of these rule-sets. Individuals will choose to enter one rule-set or another. As rule-sets compete for our atten ti on , the world of c ybers p ace wi ll come to be def i n ed by this com peti ti on of
sovereigns for customers.

Post's argument rests on an important insight about the nature of governmental
power. He views government's power in the same sense in which we now understand
a firm's market power in anti trust law. By "m a rket power " a n ti trust law yers and
economists mean a firm's ability to raise prices profitably. In a perfectly competitive
market, a firm with no market power is the one that cannot raise its prices because
it would lose so much in sales as to make the increase not worth it.39 The firm that
does have market power can raise prices and see its profits increase. The firm with
market power also has the ability to force consumers to accept a price for a good that
is higher than the price in a competitive market.

We might imagine an analogous con s traint opera ting on govern m en t . G overn m en t s , l i ke firm s , can get aw ay with on ly so mu ch . As they become more repre s s ive , or as they reg u l a te more harshly h ly, o t h er govern m en t s , or other ru l e - s et s ,
become com peti tors . At some point it is easier for citi zens to leave than to put up
with the bu rdens of reg u l a ti on ,4 0 or easier to evade the law than to com p ly wi t h
i t .

Because in real space such moves are costly, governments—or rule-sets—at least
in the short run can get away with a lot. In cyberspace,the claim is,moving is not so
hard. If you do not like the rule-set of your ISP, you can change ISPs. If you do not
like the amount of advertising on one Internet portal, then in two seconds you can
change your default portal. Life in cyberspace is about joining without ever leaving
your home. If the group you join does not t reat you as you want to be treated, you

2 0 2

can leave . Because com peti tive pre s su re is gre a ter in cybers p ace , govern m ents and
other propagators of rule-sets must behave like firms in a competitive market.

This is an important con cepti on of govern a n ce in cybers p ace . It argues for a
world of volunteers, one where rules are not imposed but selected. It is a world that
minimizes the power of any particular government, by making governments competi tors for citi zen s . It is govern m ent like Mc Don a l d 's or Coc a - Co l a — e a ger to
please, fearful of revolt.

Nonetheless, I have disagreements. I want to question the model—by questioning first its positive and then,its normative claims.

First, consider the claim that exit costs are lower in cyberspace than in real space;
in d oing so, we should distinguish between commodities and communities. When
you switch to a different ISP or Internet portal, you no doubt confront a different set
of "rules." And these rules no doubt compete for your attention. This is just like going from one restaurant or shopping mall to another. There are competing rule-sets;
they are among several fa ctors you consider in choosing an ISP; and to the extent
that there is easy movement among these rule-sets,this movement is undoubtedly a
competition among them.

Communities are different. Consider the "competition" among, say, MUDs. You
join a MUD and spend months building a character in that community. At the end
of this time, you have probably become well known in that community—you have
well-developed social capital. That social capital—the set of experiences and understandings that individuals in that space have of you—is built through time and repeated interactions.

You have social capital in real space too. You have the set of relationships that define your friendships, your reputation,and your status. But you also have other capital—a house perhaps, a car, a savings account. When you move in real space, you
can, for the most part, transfer your assets. You can sell your house and then buy another in the place you are moving to; you can move your money from one bank to
another; if you move into a community as, for example,a doctor, you have a certain
status based on that.

In cybers p ace no assets are tra n s fera bl e . You can move from one com mu n i ty to ano t h er, but with each move you must start over aga i n .4 1 You do not en ter a MUD wi t h
m on ey or social statu s . You en ter as a ch a racter wh om you must then con s tru ct .

Paradoxically, then, we might say that it is harder to change communities in cyberspace than it is in real space. It is harder because you must give up everything in
a move from one cyber-community to another, whereas in real space you can bring
much of it with you.42 Communities in cyberspace, then, may in the short run have
more power over their citizens than real-space communities do.

This suggests a picture of competing rule-sets in cyberspace that is more complex than Post believes. It is not clear that markets will function more competitively
there (since it is easier to build in these loyalty programs).43 Nor is it clear that communities will function more competitively there (since it is harder to transfer social
capital).44

2 0 3

There is a second, more fundamental criticism. Even if we could construct cyberspace on the model of the market—so that we relate to spaces in cyberspace the
way we relate to toothpaste in real space—we should not want to do it. An important and long-standing trad i ti on argues that beyond their role as con su m ers humans need to increase the con texts wh ere they are mem bers . Both as a matter of
justice and as a matter of human flourishing, we need these parts of our lives where
we have control over the architectures under which we live.

In at least some ways ,t h en , we should rel a te to cybers p ace as mem bers ra t h er than
as custom ers . In an odd but wh o lly familiar sen s e , we need to take re s pon s i bi l i ty for
what cybers p ace is; we must become citi zens of c ybers p ace just as we are simu l t a n eo u s ly citi zens of , s ay, the Un i ted States and Ma s s Massachusetts s et t s . Being all three at on ce wi ll
force us to work out how these va rious po l i tical com mu n i ties should interact .

At times these different roles will conflict, but this is a conflict we in the United
States know well.A conscientious white southerner in the 1960s, for example, must
have felt the conflict between being an American citizen and a citizen of a southern
state. The vision of equality in these two different communities differed,and a white
citizen had to select the one to which he would be loyal.

But how then do we act in these multiple roles as citizen? How do we respect the

multiple roles while permitting the different jurisdictions to flourish?

One way of thinking abo ut this probl em is what in legal ja r gon is call ed su bs i d i a ri ty.4 5 Su b s i d i a ri ty su ggests that local issues should be dealt with loc a lly, a n d
that multiple jurisdictions should respect other jurisdictions dealing with whatever
issues are properly their own. A community has the right to regulate its members,
but only insofar as its regulation affects their membership in that community. Regulation should not extend beyond that narrow range.

But subsidiarity is not a determinative concept; there is no independent way of
deciding what is "local."46 A community and a state could both have the objective of
providing "equal and excellent" education for their citizens, but nothing in the concept of subsidiarity tells us at which le vel this objective should be pursued.

The same will be the case in cyberspace. What Arab states consider "local"is not
what Americans will see as local; what poor nations see as universal access will be
more comprehensive than what many rich ones see as universal access. Subsidiarity
alone will not determine the proper scope of political action. Political decisions have
to do that.

Therefore, we need to be able to make political decisions at the level of the Net.
A political judgment needs to be made about the kind of freedom that will be built
into the Net. Our problem is imagining how that decision could be made.

In a sen s e , as I argued in ch a pter 3, the dec i s i on was made wh en the Net was
built. The Net imposed on the world an architecture of freedom that was more robust and important than any political structure the United States had ever exported.
Some would call this a kind of i m perialism—the impo s i ti on of our va lues on
o t h er nati ons—and insist that we cre a te an arch i tectu re that does not impose the
First Amendment on the world. Who are we to insist on free speech as a worldwide

2 0 4

value? Or on free markets as the organizing structure for economies the world over?
Isn't this just the sort of decision that local governments ought to make? Why are we
making it for them?

Th ere was a time wh en the Un i ted States was re a lly "these united State s ," a ti m e
when the dominant political reality was local and there were real differences of culture and values between New York and Virginia. Despite these differences, in 1789
these states united to establish a relatively thin national government. This government was to be minimal and limited; it had a number of narrow, strictly articulated
purposes. Beyond them, the national government was not to go.

These limits made sense in the limited community that the United States was. At
the time there was very little that the states shared as a nation. They shared a history
of defeating the strongest army in the world,47 and a pur pose of growing across an
almost endless continent. But they did not share a social or political life.Life was local, exchange was rare,and in such a world limited national government made sense.
Nevertheless, there were national questions to be articulated and resolved. Slavery, for example, was a mark on our country as a whole, even though the practice
was limited to a few state s . Th ere had been arguments at the founding abo ut
whether slavery should be left to local regulation.

But the Constitution was founded on a compromise about that question. Congress was not permitted to address the question of the "importation" of slaves until
1808.48 After that, it could,and people, increasingly, said that it should. Slavery continued, however, to be a stain on the moral standing of our nation. Congress could
eliminate it in the territories at least, and some argued that it should do so in the
southern states as well.

Opponents to this call for Congress to cleanse our nation of slavery were of two
s ort s . One type su supported the insti tuti on of s l avery and bel i eved it was cen tral to
southern life. They are not my focus here. My focus is a second type—those who,
with perfect integrity ty and candor, a r g u ed that slavery was a local issu e , not a national issue; that the framers had understood it not to be a national issue; and that
the national government should let it alone.

However true that claim might have been in 1791 or 1828,it became less plausible over time. As the nation became socially and economically more integrated, the
plausibility of saying, "I am a Virginian first," declined,and the significance of being
a citizen of the nation as a whole increased.49

This change came about not through some political decision but as a result of a
ch a n ging econ omic and social re a l i ty. Our sense of being mem bers of a nati on a l
community increased until, at a certain stage, it became impossible to deny our national citizenship. The Fourteenth Amendment wrote it into the Constitution; economic and social intercourse made it completely real. And as this change took hold,
the claim that issues like slavery were local became absurd.

The very same process is hap pening to us now, internationally, and it is making
an important cybers p ace con tri buti on . It has been slowly gaining mom en tu m , of

2 0 5

co u rs e , s i n ce the end of World War II, but the In tern et has wi l dly accelerated era ted the
p ace . O rd i n a ry citi zens are con n ected intern a ti on a lly and can make intern a ti on a l
transactions as never before. The presence of a community that is beyond any individual state is increasingly undeniable.

As this international community develops in cyberspace, its citizens will find it
increasingly difficult to stand neutral in this international space. Just as a principled
sort of citizen in 1791 might have said that slavery in Virginia was irrelevant to a citizen in Maine, so in 1991 the control of speech in Singapore may have been irrelevant to a citi zen of the Un i ted State s . But just as the claim abo ut slavery 's loc a l
rel eva n ce became implausible in the co u rse of the nineteenth cen tu ry, the cl a i m
about speech on the Net will become equally implausible in the next century. Cyberspace is an international community; there are constitutional questions for it to
answer; and increasingly, we cannot simply stand back from this international space
and say that these questions are local issues.

At least, we could not say that on ce we ef fectively invaded this intern a ti on a l
s p ace with the In tern et of 1 9 9 5 . We put into the world an arch i tectu re that fac i l it a ted ex tra ord i n a ri ly free speech and ex tra ord i n a ry privac y; that en a bl ed sec u re
com mu n i c a ti ons thro u gh a pro tocol that perm i t ted en c rypti on ; and that en co u raged free communications through a protocol that resisted censorship. That was the
speech architecture that the Net gave the world—that we gave the world.

Now we are changing that architecture. We are enabling commerce in a way we
did not before; we are contemplating the regulation of encryption; we are facilitating iden ti ty and con tent con tro l . We are remaking the va lues of the Net , and the
question is: Can we commit ourselves to neutrality in this reconstruction of the architecture of the Net?50

I don't think that we can. Or should. Or will. We can no more stand neutral on
the qu e s ti on of wh et h er the Net should en a ble cen tra l i zed con trol of s peech than
Americans could stand neutral on the question of slavery in 1861. We should understand that we are part of a worldwide political battle; that we have views about
what rights should be guaranteed to all humans, regardless of their nationality; and
that we should be ready to press these views in this new political space opened up by
the Net.

I am not arguing for world government. Indeed,the impossibility of such an idea
is the focus of much of the next chapter. My argument instead is that we must take
responsibility for the politics we are building into this architecture because this architecture is a kind of sovereign governing the community that lives in that space.
We must consider the politics of the architectures of the life there.

I have argued that we should understand the code in cyberspace to be its own sort
of regulatory regime, and that this code can sometimes be in competition with the
law's regulatory regime. In copyright, for example, we saw how copyright law could
be inconsistent with the regulatory regime of trusted systems. My argument is that
we should understand these to be two regulatory regimes in competition with each

2 0 6

o t h er. We need a way to ch oose bet ween them . We need a way to dec i de wh i ch
should prevail.

As this sys tem of reg u l a ti on by code devel op s , it wi ll contain its own norm s ,
which it will express in its st ructures or in the rules it imposes. If the predictions of
law and economics are correct,these norms will no doubt be efficient, and they may
well be just. But to the extent that justice does not track efficiency, they will be efficient and unjust. The question will then be: How do we react to this gap?

There is an important pattern in this competition between code and law. Law, at
least as it regulates international relations, is the product of extended negotiations.
Countries must come to an agreement about how law will regulate and about any
norms that they will impose on private ordering. As their work relates to cyberspace
in parti c u l a r, this agreem ent is qu i te sign i fic a n t . It wi ll requ i re the nati ons of t h e
world to come to a common understanding about this space and to develop a common strategy for dealing with its regulation.

Me a nwh i l e , of co u rs e , the space is reg u l a ting itsel f . While nati ons argue abo ut
what regulation there should be,the code of cyberspace continues to develop with a
certain kind of s overei gn aut h ori ty. Its reg u l a ti ons need fewer agreem en t s , and its
structure alone admits new protocols.

What we wi ll see , I su gge s t , is the em er gen ce of a fairly unified reg u l a ti on
through code while law remains in flux. This development will cause a shift in effective regulatory power—from law to code, from sovereigns to software. Just as there
was a push toward convergence on a simple set of network protocols,there will be a
push toward convergence on a uniform set of rules to govern network transactions.
This set of rules will include not the law of trademark that many nations have, but a
unified system of trademark, enforced by a single committee;51 not a diverse set of
policies governing privacy, but a single set of rules,implicit in the architecture of Internet protocols;not a range of contract law policies, implemented in different ways
according to the values of different states, but a single, implicit set of rules decided
through click-wrap ag agreements and enforced where the agreement says. As Walter
Wri s ton , the form er Ci tibank ch a i rman and aut h or of The Twi l i ght of S overei gn ty,
puts it, "The government can't do much about it. It's another thing slipping through
their fingers."52

We should pause to consider just what this will mean.
We have governments for a purpose—in democratic states, we might even say,
for good purpose. For much of human history governments could do very little. The
cost of doing anything was, on the margin, extremely high. Much of the world operated under an effective laissez-faire; little of the world was really regulated.

The nineteenth and twentieth centuries were the centuries of government. For
the first time,and brutally in many cases, government took control of both itself and
the market. It became activist, focused on changing the status quo, antilibertarian. It
could take control this way in large part because of the economies of its regulation
and the diseconomies of escaping its regulations. Borders keep people in, and hence
governments could regulate.

2 0 7

Cyberspace und ermines this balance. Regulation does not become more costly,
but escape from regulation becomes easier. The shift is away from the power of government to regulate,and toward the power of individuals to escape government regulation.

Effective regulation then shifts from lawmakers to code writers. The question for
us is wh et h er this shift should be unch ecked . And the answer should depend firs t
u pon who the code wri ters are , and second upon what va lues they bring to thei r
work.

We are just leaving a time wh en the code wri ters are a rel a tively indepen den t
body of experts and code is the product of a consensus formed in forums like the Intern et Engi n eering Task Force (IETF). These were reg u l a tory bodies whose stand a rds set po l i c y, but they were in one sense disinterested s ted in the outcom e s : t h ey
wanted to produce nothing more than code that would work.

We are entering a very different world where code is w ritten within companies;
where standards are the product of competition; where standards tied to a dominant
s t a n d a rd have adva n t a ge s . We are en tering a world wh ere code is corpora te in a
commercial sense, and leaving a world where code was corporate in a very different
sense.

To the extent that this code is law, to the extent that it is a chosen structure of
constraint, we should worry about how it is structured and whose interests may define its constraint, just as we worry when any lawmaking power is assumed by a private body. If code is law, who are the lawmakers? What values are being embedded
into the code?

Both qu e s ti ons are fundamen t a lly abo ut soverei gn ty. Who should be bu i l d i n g
this world,and who should be specifying the values that this world will build into itself?

We have already seen one response to this shift.I have argued that local rules will become less significant because it is hard to enforce local rules relative to global rules.
But doing so is hard only because the architecture makes it hard. We do not have a
simple system for distinguishing natives of Canada from natives of New York, so it
is burdensome to apply different rules to each.

But as I discussed in chapter 5, local rules need not be difficult to enforce.A certificate-rich Internet, for example, would enable sovereigns to reclaim some of their
authority. In a cy berspace where everyone carried citizenship IDs, the Net could be
zoned to apply citizen-specific rules. If you come from the United States and are under the age of seventeen,a Swedish server could block you;if you come from Russia,
it could not. A world wh ere certi fic a tes were gen era lly ava i l a ble would be a worl d
where states could again insist that their rules be applied, not the rules of the dominant nation (the United States) or the Net.

Sovereigns will get this. 53 They will come to understand that there is a different
architecture for the Net that would re-enable their own control. When they do, they
will push to facilitate the predicate to this architecture of regulability—certificates.

2 0 8

And when they do, we again will ha ve to decide whether this architecture of regulability is creating the cyberspace we want.

A choice.
A need to make a choice.
My claim in part 1 was that commerce would help make this choice. Commerce,
I argued, will push for a certificate architecture that would enable its own form of
control. That architecture would enable some forms of state control. But the precise
control would depend on the architecture.

I have not argued against government. I have not said that we should architect
the space to disable collective control. Indeed,I have argued just the opposite.I have
marked myself as one of those loons who actually thinks that collective choice can
do some good.

But I am not a statist. I don't think the best of us is given to us from top-down.
There is a proper space for collective life, and an important space for private life. A
good constitution helps us navigate that balance.

We could arch i tect the sys tem of i den ti f i c a ti on in cybers p ace to en a ble som e
forms of local control; we could build it so that some forms of local control would
matter. But the simple answers here are not answers: it would be a disaster if cybers p ace became a place wh ere loc a l i ties again com p l etely con tro ll ed — i f geogra phy,
that is, were simply mapped onto the space—just as it would be a disaster if no local (and hence no collective) control existed.
The answer steers a different course.

The last four chapters have told the story of a certain kind of displacement. In each,
a type of liberty has been transformed. In the first three,the liberty is displaced by a
more efficient architecture of control: fair use is coded away; privacy becomes too
cumbersome; filters become predominant. Architectures emerge that displace a liberty that had been sustained simply by the inefficiency of doing anything different.
In the last story, the liberty of the state to regulate is displaced by a more efficient
architecture of mobility. Here efficiency works on the side of freedom from regulation. Under this architecture, it becomes too costly to track and control citizens; it
becomes too easy for citizens to live subject to a different set of rules. Local control
declines; the Net's control increases.

The key is to see that these different changes are structurally the same. In each
case, the increase in a kind of efficiency throws into relief a value that had been latent. The conflict is between that efficiency (different in each case) and the value latent in the less efficient regime. This is not a value in inefficiency but instead a value
made possible by a particular inefficiency.

I don't mean this as a criticism of the notion of efficiency. To identify a value that
has been lost by efficiency is only to raise the question of whether in fact the "efficient i en t" is ef f i c i en t , or ef f i c i ent to a particular en d . The qu e s ti on is what the en d
should be. If the value that is lost is of value, then it may no longer be efficient to

2 0 9

sacrifice it. Compare: driving on highways is a quicker way to get between two cities,
but you lose a sense o f the countryside when you drive only on interstate highways.
Nor do I mean to claim that this argument is new. It is practically trite to remark
the values of a slower and quieter time, displaced by the rush of modern life. But to
remark these values is not to say that they should be accorded infinite weight. The
mad rush of modern life has no doubt moved many people out of poverty. That is
an undoubted good,and one that weighs heavily against the "loss" of a quieter time.
But the values at stake in these four applications are at the core of who we are
and who we understand ourselves to be, both as a people and as individuals. If we
bel i eve that the reg u l a ti ons of c ybers p ace wi ll displace these va lu e s , t h en the ef ficiency o f these regulations in gaining some ends may be inefficient in gaining the
ends we collectively want. 54 The decision then is not about choosing between efficiency and something else, but about which values should be efficiently pursued. My
claim in each of these cases is that to pre s erve the va lues we want, we must act
against what cyberspace otherwise will become. The invisible hand, in other words,
will produce a different world. And we should choose whether this world is one we
want.

How we go about making these choices is the question of part 4. It is the pathology of modern politics that we have become so disgusted with self-government that
our automatic response to government is criticism. Freedom is always freedom from
govern m en t ; l i berty is alw ays liberty from what govern m ent would otherwise do.
These were also the thoughts of the people who suffered under the most oppressive
govern m ents of our time—the people of po s t - Com munist Eu rope . Th ey too, ju s t
a f ter the fall of com mu n i s m , were keen to find ways to minimize govern m en t , to
create spaces not regulated by government.

But their lessons should be our lessons. What they learned was that liberty does
not necessarily follow from having a space of no government. Freedom from governmental tyranny may be a necessary condition for liberty, but it is not sufficient.
More important, government is necessary to help establish the conditions necessary
for liberty to exist. This is because there are collective values that, acting as individu a l s , we wi ll not re a l i ze . These co ll ective va lues are som etimes va lues of l i berty,
wh i ch govern m ents can act to establish and su pport . The freedom to con tract , to
own property, to travel , to vo te — a ll of these ri ghts requ i re massive govern m en t a l
support.

Som etimes these co ll ective va lues deny or re s tri ct liberty in the name of s om e
o t h er va lue that is wei gh ed more stron gly than liberty. The examples that fo ll ow
canvass both kinds of values,and the threat that cyberspace will present to each. The
l e s s on that should em er ge from the co ll ecti on is a lesson abo ut how to re s pon d :
what disciplines we must relearn if we are to preserve these values against changes
that we now only imperfectly control.

P A R T F O U R

r e s p o n s e s

The lesson of part 1 was that the Net won't take care of itself. There is no nature that
will protect cyberspace against change, and there is a tremendous amount of pressure for cyberspace to change. If the change continues along the lines it has taken so
far, it will become a highly regulable space—not the locus of liberty, not a space of
no control, but a technology of government and commercial power wired into every
aspect of our lives.

But that's just one po s s i ble spin. The aim of p a rt 2 was to su ggest others . Th e
built environments of cyberspace could be many, because the choices are many. And
the po ten tial power of govern m ent over these ch oi ces is gre a t . G overn m ent has
m a ny tools with wh i ch to ben d , or perfect , the arch i tectu res of this space . It has
m a ny tech n i ques with wh i ch to make cybers p ace what it wants cybers p ace to be .
These powers , h owever, a re con s tra i n ed — s om etimes by law, m ore import a n t ly by
the code itself. Open code is one such constraint. But the possibilities of constraint
are not themselves constraints. The message of part 2 was that little is determined,
and much is possible. Choice is possible.

Part 3 exercised that choice. I began with a traditional legal technique for deciding how to go on — l et the fra m ers dec i de . Th o u gh the fra m ers knew little abo ut
TC P / I P, the argument was that they establ i s h ed a trad i ti on that can be tra n s l a ted
into the context of cyberspace. They gave us the values,and our task is to carry those
values into cyberspace.

But translation does not deal well with latent ambiguities. My argument in the
balance of part 3 was that there are many such ambiguities. In four crucial areas of

2 1 2

social and political life in cyberspace, the words of the framers will not carry us far
in making the nece s s a ry ch oi ce s . Wh ere tra n s l a ti on gives out , a ch oi ce must be
made.

The question for this part is whether we're capable of that choice. My argument
is that we're not. We have so completely passed off questions of principle to the judicial branch,and so completely corrupted our legislative process with the backhand
of handouts, that we confront this moment of extraordinary importance incapable
of making any useful decisions. We have been caught off-guard,drunk on the political indulgence of an era, and the most we may be able to do is stay on our feet until we have time to sober up.

F I F T E E N

t h e p r o b l e m s w e f a c e

I've ar gued t h at t h er e is a ch oice about h ow cyber space sh oul d be, but t h at
we're disabled from making that choice. We are disabled for three very different reasons.One is tied to the limits we place on courts,the second to the limits we have realized in legislatures, and the third to the limits in our thinking about code. If choice
must be made,these limits mean we will not be making that choice. We are at a time
when the most significant decisions about what this space will be must be made, yet
we haven't the institutions, or practice, to make them.

In part 4,I describe these problems,and in chapter 16,I sketch three types of solutions to them. Neither part will be complete, but both should be suggestive. The
problems that cyberspace reveals are not problems with cyberspace. They are realspace problems that cyberspace shows us we must now resolve.

P R O B L E M S W I T H C O U R T S

Th ere are two types of con s ti tuti on s , one we could call cod i f yi n g , and the other
transformative. A codifying constitution tries to preserve something essential from
the con s ti tuti onal or legal cultu re in wh i ch it is en acted — to pro tect that cultu re
against changes in the future. A transformative constitution (or amendment) does
the opposite: it tries to change something essential in the constitutional or legal culture in which it is enacted—to make life different in the future, to remake some part
of the culture. The symbol of the codifying regime is Ulysses tied to the mast; the
symbol of the transformative is revolutionary France.

Our Constitution has both regimes within it. The Constitution of 1789—before
the first ten amendments—was a transformative constitution. It "called into life" a
new form of government and gave birth to a nation.1 The Constitution of 1791—
the Bill of Rights—was a codifying constitution. Against the background of the new
constitution, it sought to entrench certain values against future change.2 The Civil

2 1 4

War amendments were transformative again. They aimed to remake part of what the
American social and legal culture had become—to rip out from the American soul
a tradition of inequality and replace it with a tradition and practice of equality.3

Of these two regimes, the transformative is clearly the more difficult to realize. A
codifying regime at least has inertia on its side; a transformative regime must fight.
The codifying regime has a moment of self-affirmation; the transformative regime
is haunted with self-doubt. Constitutional moments die, and when they do, the ins ti tuti ons ch a r ged with en forcing their com m a n d s , su ch as co u rt s , f ace incre a s i n g
political resistance.Flashes of enlightenment notwithstanding, the people go back to
their old ways, and courts find it hard to resist.

Our own constitutional history reveals just this pattern. The extraordinary moment after the Civil War—when three amendments committed to civil equality were
c a rved into our Con s ti tuti on's soul—had passed by 1875. The nati on gave up the
struggle for equality and turned to the excitement of the industrial revolution.Laws
enforcing segregation were upheld;4 the right of African Americans to vote was denied;5 laws enforcing what was later seen to be a new kind of slavery were allowed.6
Only after one hundred years of continued inequality did the Supreme Court again
take up the cause of the Civil War amendments. It would not be until Brown v Board
of Education, in 1954,that the Court again recognized the transformative idea of the
Civil War amendments.7

One could cri ti c i ze the Co u rt for this cen tu ry of we a k n e s s . I think it is more important to understand its source . Co u rts opera te within a po l i tical con tex t . Th ey are
the we a weakest bra n ch of re s i s t a n ce within that po l i tical con tex t . For a time they may be
a ble to insist on a principle gre a ter than the mom en t . But that time wi ll pass. If t h e
world retu rns to its racist ways , even a strong statem ent of principle en acted wi t h i n
our Con s ti tuti on's text permits a co u rt on ly so mu ch freedom to re s i s t . Co u rts are su bj ect to the con s traints of what "everyon e" bel i eves is ri gh t , even if what "everyon e" bel i eves is incon s i s tent with basic con s ti tuti onal tex t s .

Life is easier with a codifying constitution. For here there is a tradition that the
text is just meant to entrench. If this tradition is long-standing, then there is hope
that it will remain solid as well.

But even a cod i f ying con s ti tuti on faces diffic u l ti e s . Cod i fic a ti on notwi t h s t a n ding, if the passions of a nation become strong enough,there is often little a court can
do. The clarity of the First Amendment's protection of freedom of speech notwithstanding, when the speech was that of communists and anarchists, the government
was all owed the power to punish.8 The pre su m pti on of i n n ocen ce and equ a l i ty
notwithstanding, when Japan bombed Pearl Harbor, the government was allowed to
shuttle every West Coast American of Japanese descent into concentration camps.9
These are the realities of courts in a democratic system. We lawyers like to romanticize the courts, to imagine them as above influence. But they have never been
s o, com p l etely, or forever. Th ey are su bj ect to a po l i tical con s traint that matters .
They are an institution within a democracy. No institution within a democracy can
be the enemy of the people for long.

t h e p r o b l e m s w e f a c e

2 1 5

It is against this background that we should think about the problems raised in
p a rt 3. In each case, my argument was that we wi ll need to ch oose the va lues we
want cyberspace to embrace. These questions are not addressed by any clear constitutional text or tradition. In the main,they are questions affecting the codifying part
of our tradition, but they are also cases of latent ambiguity. There is no "answer" to
them in the sense of a judgment that seems to have been made and that a court can
simply report. An answer must be fixed upon,not found;made,not discovered; chosen, not reported.

This cre a tes difficulties for an Am erican co u rt . We live in the shadow of t h e
Supreme Court of Chief Justice Earl Warren. Many people think (but I am not one
of this crowd) that his was a wildly activist court, that it "made up" constitutional
law and imposed its own "personal values" onto the political and legal system. Many
view the Rehnquist Court as providing a balance to this activism of old.

I think this view is wrong. The Warren Court was not "activist" in any sense inconsistent with a principle of interpretive fidelity, and the Rehnquist Court is no less
activist than the Wa rren Co u rt . The qu e s ti on , h owever, is not what was tru e ; t h e
question is what people believe. What we believe is that the past was marked by activism,and that this activism was wrong.

Wrong for a court, at least. The opponents of the Warren Court are not just conservatives. Some are liberals who believe that the Court was not acting judicially.10
These oppon ents bel i eve that the Co u rt was making, not finding, con s ti tuti on a l
law—that it was guided by nothing more than whether it could muster a majority.
Any co u rt risks seeming like a "Wa rren Co u rt" wh en it makes ju d gm ents that
don't se em to flow plainly or obvi o u s ly from a legal tex t . Any co u rt is vu l n era bl e
when its judgments seem political. Against the background of history, our Supreme
Court is particularly vulnerable to this view. The Court will feel the reaction when
its actions seem political.

My point is not that the Court fears retaliation; our Court is secure within our
constitutional regime.11 The Court feels the reaction to its seemingly political decisions because of its own image of its proper role. In its view, its role is not to be "political"; its conception is that it is to be a faithful agent, simply preserving founding
commitments until they have changed.12

But wh en—as in the cases of l a tent ambi g u i ty — t h ere are no founding com m i tm ents to pre s erve , t h en any attem pt at tra n s l a ti on wi ll seem to be som ething more .
And wh en ever it seems as if the Co u rt is doing more than simply pre s erving fo u n d i n g
com m i tm en t s , the perception on is cre a ted that the Co u rt is simply acting to ra tify its
own vi ews of a proper con s ti tuti onal regime ra t h er than en forcing ju d gm ents that
h ave been con s ti tuti on a l i zed by others .1 3 In a word , it seems to be acting "po l i ti c a lly."
But what does "political" mean here? It does not mean simply that the Court is
making value or policy choices.The claim is not that values are improper reasons for
a court to decide a case. To the contrary: value choices or policy choices, properly rat -
ified by the political process, are appropriate for judicial enforcement. (The problem
with the choices in cases of latent ambiguity is that they do not seem to have been

2 1 6

properly ratified by the political process. They reflect values, but the values do not
seem to be taken from the Constitution.)

"Political"thus refers to judgments not clearly ratified and presently contested.14
When the very foundations of a judgment are seen to be fundamentally contested,
and when there is no reason to believe that the Constitution takes a position on this
contest, then enforcing a particular outcome of translation will appear, in that context, political.15

Cyberspace will press this problem intensely. When a framing value can be translated with some clarity or certainty, the Court can act in a way that resists present
majorities in the name of founding commitments. But when ambiguities are latent
and a choice really seems to be a choice, translation will not suffice. My claim is that
the Court will not be the locus for that choice.

This might seem overly pessimistic, especially when we consider the success in
striking down the Communications Decency Act.16 But that case itself reveals the instability that I fear will soon resolve itself into passivity.

Throughout both lower court opinions, the courts spoke as if they were "finding" facts about the nature of cyberspace. The "findings" determined the constitutional result, and both courts reported their findings with a confidence that made
them seem set in stone.

These fin d i n gs , for the most part , were excepti on a lly good de s c ri pti ons of wh ere
c ybers p ace was in 1996. But they did not tell us anything abo ut wh ere cybers p ace is going or what it could be . The co u rts spo ke as if t h ey were telling us abo ut the n a tu re of
c ybers p ace , but as we've seen ,c ybers p ace has no intrinsic natu re . It is as it is de s i gn ed .
By striking down Con gre s s's ef forts to zone cybers p ace , the co u rts were not telling us
what cybers p ace i s but what it s h ould be . Th ey were making, not fin d i n g, the natu re of
c ybers p ace ; t h eir dec i s i ons are in part re s pon s i ble for what cybers p ace wi ll becom e .

At first it will not seem this way. When we confront something new, it is hard to
know what is natural, or given about it,and what part can be changed. But over time
courts will see that there is little in cyberspace that is "natural." Limits on the architecture of cyberspace that they have reported as findings in one opinion will be seen
to have been "design choices" later on. What was "impossible" will later become possible, and as these shifts in the possible occur, courts will more and more feel that
t h ey cannot re a lly say what cybers p ace is. Th ey wi ll see that their findings affect
what they find. They will see that they are in part responsible for what cyberspace
has become.

This is Heisenberg applied to constitutional law. And as courts notice it, as they
h ave in other are a s , t h ey wi ll incre a s i n gly defer to the po l i tical bra n ch e s : i f t h e s e
judgments are policy, they will be left to policy makers, not judges.17

One can hardly blame ju d ges for this. In deed , in some cases their deferen ce
should be encouraged.18 But we should not underestimate its consequences. In the
f utu re legi s l a tu res wi ll act rel a tively uncon s tra i n ed by co u rt s ; the va lues that we
might call constitutional—whether enacted into our Constitution or not—will constrain these legislatures only if they choose to take them into account.

t h e p r o b l e m s w e f a c e

2 1 7

Before we tu rn to what we might ex pect from legi s l a tu re s , con s i der one other
problem with courts—specifically, the problem confronting our constitutional tradition as the Constitution moves into the context of cyberspace. This is the problem
of "state action."

Architectures constitute cyberspace;these architectures are varied; they variously
embed political values; some of these values have constitutional import. Yet for the
most part—and fortunately—these architectures are private. They are constructed
by universities or corporations and implemented on wires no longer funded by the
Defense Department. They are private and therefore traditionally outside the scope
of con s ti tuti onal revi ew. The con s ti tuti onal va lues of privac y, acce s s , ri ghts of
anonymity, and e quality need not trouble this new world, since this world is "private" and the Constitution is concerned only with "state action."

Why this should be is not clear to me. If code functions as law, then we are creating the most significant new jurisdiction since the Louisiana Purchase, yet we are
building it just outside the Constitution's review. Indeed, we are building it just so
that the Constitution will not govern—as if we want to be free of the constraints of
value embedded by that tradition.

So far in this book,I have not relied very much on this private/public distinction.
You might say I have ignored it. But I have ignored it not because it makes no sense,
but because I don't know how it could be carried over to the regulation of cyberspace. The concept of state action itself presents a latent ambiguity, and I don't think
we have a clear idea of how to resolve it.

The ambiguity is this: the Constitution was drawn at a time when basic architectures were set. The framers found the laws of nature,the laws of economics,the "natural law" of man; they were not made by government or man.

These arch i tectu res con s tra i n ed , of co u rs e , and their con s traint was a "reg u l ation." But the degree to which they could be used as tools of self-conscious control
was limited. Town planning was not limited,19 but beyond laying out a space, there
was little these founders could do about the rules that would govern the built environment of this space.

Cyberspace, however, has different architectures, whose regulatory power is not
so limited. An extraordinary amount of control can be built into the environment
that people know there . What data can be co ll ected , what anonym i ty is po s s i bl e ,
what access is granted, what speech will be heard—all these are choices, not "facts."
All these are designed, not found.

Our context, therefore, is very different. That the scope of constitutional review
was limited in the first context does not compel it to be similarly limited in the second. It could be, but we cannot know that merely from its being so limited in a very
different context.

We have no answer from the framers, then, about the scope of state action. We
must decide on our own what makes better sense of our constitutional tradition. Is
it more faithful to our tradition to allow these structures of control, the functional
equivalent of law, to develop outside the scope o f constitutional review? Or to ex-

2 1 8

tend constitutional review to the structures of private regulation, to preserve those
fundamental values within our t radition?

These are hard qu e s ti on s ,t h o u gh it is useful to note that they are not as hard to ask
in other con s ti tuti onal regi m e s . The German trad i ti on , for ex a m p l e , would have less
tro u ble with the idea that priva te stru ctu res of power must ulti m a tely be ch ecked
a gainst fundamental con s ti tuti onal va lu e s .2 0 The German trad i ti on , of co u rs e , is not
our own . But the fact that they have su s t a i n ed this vi ew su ggests that we may make
s p ace for the con s traint of the Con s ti tuti on wi t h o ut tu rning everything into a con s constitutional onal dispute . Nevert h el e s s , it wi ll take a revo luti on in Am erican con s ti tuti onal law
for the Co u rt , s el f - con s c i o u s ly at least, to move beyond the limits of s t a te acti on .

It is in these two ways then that courts are stuck. They cannot be seen to be creative, and the scope of their constitutional review has been narrowed (artificially, I
believe) to exclude the most important aspect of cyberspace's law—code. If there are
decisions about where we should go, and choices about the values this space will include,then these are choices we can't expect our courts to make.

P R O B L E M S W I T H L E G I S L A T O R S

At a con feren ce in form er Sovi et Geor gi a , s pon s ored by some We s tern agency of
democracy, an Irish lawyer was trying to explain to the Georgians what was so great
about a system of judicial review—the system by which courts can strike down the
acts of a parliament i a m en t . " Judicial revi ew," he en t hu s ed , "is won wonderful u l . Wh en ever the
court strikes down an act of parliament, the people naturally align themselves with
the court,against the parliament. The parliament, people believe,is just political; the
supreme court, they think, is principled." A Georgian friend, puppy-democrat that
he is,asked, "So why is it that in a democracy the people are loyal to a nondemocratic institution and repulsed by the democratic institution in the system?" "You just
don't understand democracy," said the lawyer.

Wh en we think abo ut the qu e s ti on of governing cybers p ace — wh en we think
about the questions of choice I've sketched, especially those raised in part 3—we are
likely to get a sinking feeling. This seems impossibly difficult, this idea of governing
cyberspace. Who is cyberspace? Where would it vote? The very idea seems abhorrent
to cyberspace itself. As John Perry Barlow put it in his "Declaration of the Independence of Cyberspace":

Governments of the Industrial World, you weary giants of flesh and steel, I come
from Cyberspace, the new home of Mind. On b behalf of the future, I ask you of
the past to leave us alon e . You are not wel come among us. You have no sovereignty where we gather.

But our probl em is not with govern a n ce in cybers pa ce . Our probl em is simply
with governance. There is no special set of dilemmas that cyberspace will present;

t h e p r o b l e m s w e f a c e

2 1 9

t h ere are on ly the familiar dilemmas of m odern govern a n ce , but in a new place .
Some things are different;the target of governance is different; the scope of international concerns is different. But the difficulty with governance will not come from
this different target; the difficulty comes from our problem with governance.

Throughout this book, I've worked to identify the choices that cyberspace will
present.I've argued that its very architecture is up for grabs and that, depending on
who grabs it, there are several different ways it could turn out. Clearly some of these
choices are collective—about how we collectively will live in this space. One would
have thought that collective choices were problems of governance. Yet very few of us
would want government to make these choices. Government seems the solution to
no problem we have, and we should understand why this is. We should understand
the Irish in us.

Our skepticism is not a point about principle. Most of us are not libertarians. We
m ay be anti govern m en t , but for the most part we bel i eve that there are co ll ective
values that ought to regulate private action. We are also committed to the idea that
collective values should regulate the emerging technical world. Our problem is that
we do not know how it should be regulated, or by whom.

Like the Irish, we are weary of governments. We are profoundly skeptical about
the product of democratic processes. We believe, rightly or not, that these processes
have been captured by special interests more concerned with individual than collective values. Although we believe that there is a role for collective judgments, we are
repulsed by the idea of placing the design of something as important as the Internet
into the hands of governments.

The examples here are many, and the pattern arresting. The single unifying message in the government's own description of its role in cyberspace is that it should
simply get out of the way. In the area of Internet commerce, the government says,
commerce should take care of itself.(At the same time, of course,the government is
passing all sorts of laws to increase the protections for intellectual property.)

A perfect example of this point is the government's recent hand-off of control of
the management of the domain name system.21 For some time the government had
been thinking about how best to continue the governance or control of the domain
name system. It had originally farmed the work out under National Science Foundation contracts, first to a California nonprofit organized by the late Jon Postel, and
then to a private for-profit corporation, Network Solutions.

The contracts were due to lapse in 1998, however, and for a year the government
thought in earnest about what it should do. In June 1998 it released a White Paper
calling for the establishment of a nonprofit corporation devoted to the collective interest of the Internet as a whole and charged with deciding the policy questions relating to governing the domain name system. Policy-making power was to be taken
away from government and placed with an organization outside its control.

Think about the kinds of questions my Georgian friend might ask. A "nonprofit
corpora ti on devo ted to the co ll ective intere s t"? Is n't that just what govern m ent is
supposed to be? A board composed of representative stakeholders? Isn't that what a

2 2 0

Congress is? Indeed, my Georgian friend might observe that this corporate structure
differs from government in only one salient way—there is no ongoing requirement
of elections.

This is policy making vested in what is in effect an independent agency, but one
wholly outside the democratic process. And what does this say about us? What does
it mean when our natural instinct is to put policy-making power in bodies outside
the democratic process?

First, it reflects the pathetic resignation that most of us feel about the products
of ordinary government. We have lost faith in the idea that the product of representative government might be something more than mere interest—that, to steal the
opening line from Justice Marshall's last Supreme Court opinion, power, not reason,
is the currency of deliberative democracy.22 We have lost the idea that ordinary government might work, and so deep is this despair that not even government thinks
the government should have a role in governing cyberspace.

I understand this resignation, but it is something we must overcome. We must
isolate the cause and separate it from the effect. If we hate government, it is not b ecause the idea o f collective values is anathema. If we hate government, it is because
we have grown tired of our own government. We have grown weary of its betrayals,
of its games, of the interests that control it. We must find a way to get over it.

We stand on the ed ge of an era that demands we make fundamental ch oi ce s
a bo ut what life in this space , and therefore life in real space , wi ll be like . Th e s e
choices will be made; there is no nature here to discover. And when they are made,
the values we hold sacred will either influence our choices or be ignored. The values
of free speech, privacy, due process, and equality define who we are. If there is no
government to insist on these values, who will do it?

When government steps aside,it is not as if nothing takes its place. Paradise does
not prevail. It's not as if private interests have no interests,as if private interests don't
have ends they will then pursue. To push the antigovernment button is not to teleport us to Eden . Wh en the interests of govern m ent are gon e , o t h er interests take
their place. Do we know what those interests are? Are we so certain they are better?
If there are choices to be made,they will be made. The question is only by whom.
If there is a decision to be made about how cyberspace will grow, then that decision
wi ll be made . The on ly qu e s ti on is by wh om . We can stand by and do nothing as
these choices are made—by others, by those who will not simply stand by. Or we can
try to imagine a world where choice can again be made collectively, and responsibly.

P R O B L E M S W I T H C O D E

At a recent workshop, Jean Camp, a Harvard computer scientist who teaches in the
Kennedy School of Government,said that I had missed the point. The problem, she
s a i d , is not that "code is law " or that "code reg u l a te s ." The probl em is that " we
haven't had a conversation about how code regulates." And then to the rest of the aut h e p r o b l e m s w e f a c e

2 2 1

d i en ce , she said, " Did all of you like the deb a te we had abo ut wh et h er Mi c ro s of t
Word documents would carry in them a unique identifying number? Was that a satisfying debate?"23

Her irony carri ed with it an important insight t , and an intere s ting mistake . O f
course, for the computer scientist code is law. And if code is law, then obviously the
question we should ask is: Who are the lawmakers? Who writes this law that regulates us? What role do we have in defining this regulation? What right do we have to
know of the regulation? And how might we intervene to check it?

All that is perfect ly obvious for som eone who thinks and breathes the reg u l ations of code. But to a lawyer, both Camp and I, throughout this book,have made a
very basic mistake. Code is not law, any more than the design of an airplane is law.
Code does not regulate, any more than buildings regulate. Code is not public, any
more than a television is public. Being able to debate and decide is an opportunity
we require of public regulation,not of private action.

Camp's mistake is a good one. It is a mistake more of us should make more of
the time. Because while of course code is private, and of course different from the
U.S. Code, its diff erences don't mean there are not similarities as well."East Coast
Code"—law—regulates by enabling and limiting the options that individuals have,
to the end of persuading them to behave in a certain way. "West Coast Code" does
the same.East Coast Code does this by increasing the cost to those who would deviate from the rules r equired by the code. West Coast Code does the same. And while
we might argue that East Coast Code is more prevalent—that it regulates and controls a far larger part of our lives—that is a difference in degree, not kind. It's a reason to be balanced in our concern, not to be unconcerned.

Of course there are differences between law and code. I don't think that everything is necessarily public, or that the Constitution should regulate every aspect of
private life.I don't think it is a constitutional issue when I turn off Rush Limbaugh.
But to say that there should be a difference is not to say that the difference should be
as dra m a tic or absolute as pre s ent con s ti tuti onal thinking makes it. Wh en we
l aw yers tell the Jean Camps of the world that they are simply making a "m i s t a ke"
when they bring to code the values of public law, it is we who are making the mistake. Whether code should be tested with these constraints of public value is a question, not a conclusion. It needs to be decided by argument,not definition.

The formalism in American law, which puts beyond review these structures of
control,is a third pathology that inhibits choice. Courts are disabled,legislatures pathetic,and code untouchable. That is our present condition. It is a combination that
is deadly for action—a mix that guarantees that little good gets done.

S I X T E E N

We n eed a pl a n . I 've t ol d a da r k st or y a bo ut t h e ch oi ces t h at a ch a n gi n g
c ybers p ace wi ll pre s en t , and abo ut our inability l i ty to re s pond to these ch oi ce s . I 've
linked this inability to three features of our present legal and political culture. In this
short chapter, I consider three responses. Of necessity these responses are nothing
more than sketches, but they should be enough to suggest the nature of the changes
we need to make.

R E S P O N S E S O F A J U D I C I A R Y

I've said that we should understand the courts' hesitancy as grounded in prudence.
Wh en so mu ch seems po s s i bl e , and wh en a rule is not cl e a rly set , it is hard for a
court to look like a court as it decides what policies seem best.1

Al t h o u gh I agree with this ideal of pru den ce in gen era l , we need to move its
co u n s el alon g — to place it in con text and limit its re ach . We should isolate the
source of the judge's difficulty. Sometimes a certain hesitation before resolving the
questions of the Constitution in cyberspace finally, or firmly, or with any pretense to
perm a n en ce , is en ti rely appropri a te . But in other cases, ju d ge s — e s pec i a lly lower
co u rt ju d ges—should be stron ger. Lower co u rt ju d ge s , because there are many of
t h em and because many are ex tra ord i n a ri ly talented ted and cre a tive . Th eir voi ce s
would teach us something here, even if their rulings were temporary or limited in
scope.

In cases of simple tra n s l a ti on (wh ere there are no latent ambi g u i ties and our trad i ti on seems to speak cl e a rly ) , ju d ges should firm ly adva n ce arguments that seek to
pre s erve ori ginal va lues of l i berty in a new con tex t . In these cases there is an important space for activi s m . Ju d ges should iden tify our va lues and defend them , not nece s s a ri ly because these va lues are ri gh t , but because if we are to ign ore them , we should
do so on ly because they have been rej ected—not by a co u rt but by the peop l e .

2 2 3

In cases where translation is not so simple (cases that have latent ambiguities),
judges,especially lower court judges, have a different role. In these cases, judges (espec i a lly lower co u rt ju d ges) should kvetch . Th ey should talk abo ut the qu e s ti on s
these changes raise, and they should identify the competing values at stake. Even if
the decision they must adopt in a particular case is deferential or passive, it should
be deferential in protest. These cases may well be a place for prudence, but to justify
their passivity and compensate for allowing rights claims to fail, judges should raise
before the legal culture the conflict presented by them. Hard cases need not make
bad law, but neither should they be treated as if they were easy.

That is the simplest re s ponse to the probl em of l a tent ambi g u i ty. But it is incomplete. It forces us to confront questions of constitutional value and to choose. A
better solution would help resolve these questions. While it will never be the job of
the courts to make final choices on questions of value, by raising these questions the
courts may inspire others to decide them.

This is the idea behind the doctrine of a second loo k ,o ut l i n ed twen ty ye a rs ago by
Gu i do Ca l a bre s i , a profe s s or at the time who is now a ju d ge .2 Brut a lly simplified , t h e
i dea is this: wh en the Su preme Co u rt con f ronts qu e s ti ons that pre s ent open , yet fund a m ental qu e s ti ons of va lu e , it should be open abo ut the con fli ct and ack n owl ed ge
that it is not plainly re s o lved by the Con s ti tuti on . But the Co u rt should non et h el e s s
proceed to re s o lve it in the way most likely to indu ce dem oc ra tic revi ew of the re s o luti on . If the re s o luti on indu ces the proper revi ew, the Co u rt should let stand the re su l t s
of that revi ew. The most the Co u rt should do in su ch cases is en su re that dem oc rac y
has its say; its job is not to su b s ti tute its va lues for the vi ews of dem oc ra t s .

Ma ny ridicule this soluti on .3 Ma ny argue that the fra m ers cl e a rly had nothing
like this in mind when they established a Supreme Court and permitted judicial review. Of course they did not have this in mind. The doctrine of a second look is not
designed for the problems the framers had in mind. As a resp onse to the problems
of latent ambiguities, it itself reveals a latent ambiguity.

We might deny this ambiguity. We might argue that the framers envisioned that
the Court would do nothing at all about latent ambiguities; that in such contexts the
democratic process, through Article V, would step in to correct a misapplication or
to re s pond to a ch a n ged circ u m s t a n ce . That may well have been their vi ew. But I
don't think this intent is clear en o u gh to foreclose our con s i dera ti on of h ow we
might best confront the coming series of questions on the application of constitutional value to cyberspace.I would rather err on the side of harmless activism than
on the side of debilitating passivity. It is a tiny role for courts to play in the much
larger conversation we need to have—but to date have not started.

R E S P O N S E S F O R C O D E

A second challenge is confronting the law in code—resolving, that is, just how we
think about the regulatory power of code. Here are a number of ideas that together

2 2 4

would push us toward a world where regulation imposed through code would have
to satisfy constitutional norms.

Here again is the link to open code . In ch a pter 8, wh en I de s c ri bed a kind of ch eck
that open code would impose on govern m ent reg u l a ti on , I argued that it was harder
for govern m ent to hide its reg u l a ti ons in open code , and easier for adopters to disabl e
a ny reg u l a ti ons the govern m ent impo s ed . The movem ent from cl o s ed to open code
was a movem ent from reg u l a ble to less reg u l a bl e . Unless you are simply com m i t ted to
d i s a bling govern m en t's power, this ch a n ge cannot be unambiguously g u o u s ly good .

But there are two parts to the con s traint that open code might impo s e ; one is
cert a i n ly good , and the other is not nece s s a ri ly terri bl e . The first part is tra n sp a rency—the reg u l a ti ons would be known . The second part is re s i s t a n ce — t h a t
known regulations could be more easily resisted. The se cond part need not follow
from the first, and it need not be debilitating. It may be easier to disable the regulations of code if the code is in the open. But if the regulation is legitimate, the state
can require that it not be disabled. If it wants,it can punish those who disobey.

Compare the regulation of seatbelts. For a time the federal government required
that new cars have autom a tic seatbel t s . This was the reg u l a ti on of code—the car
would be made safer by regulating the code to force people to use seatbelts. Many
people hated seatbel t s , and some disabl ed them . But the vi rtue of the autom a ti c
seatbelt was that its regulation was transparent. No one doubted who was responsible for the rule the seatbelt imposed. If the state didn't like it when people disabled
their seatbelts, it was free to pass laws to punish them. In the end the government
did not press the issue—not because it co u l d n't , but because the po l i tical co s t s
would have been too high . Po l i tics ch ecked the govern m en t's reg u l a ti on , just as it
should.

This is the most we can expect of the regulation of code in cyberspace. There is
a trade-off between transparency and effectiveness. Code regulation in the context
of open code is more tra n s p a rent but also less bi n d i n g. G overn m en t's power to
achieve regulatory ends would be constrained by open code.

But there is a benefit as well. Closed code would make it easier for the government to hide its regulation and thus achieve an illicit regulatory end. Thus, there is
no simple defeat of government's ends but instead a trade-off—between publicity
and power, between the rules' transparency and people's obedience. It is an important ch eck on govern m ent power to say that the on ly rules it should impose are
those that would be obeyed if imposed transparently.

Does this mean that we should push for open rather than closed code? Does it

mean that we should ban closed code?

No. It does not follow from these observations that we should ban closed code or
that we must have a world with only open code. But they do point to the values we
should insist on for any code that regulates. If code is a lawmaker, then it should embrace the values of a particular kind of lawmaking.

The core of these values is transparency. What a code regulation does should be
at least as apparent as what a legal regulation does. Open code would provide that

2 2 5

transparency—not for everyone (not everyone reads code),and not perfectly (badly
written code hides its functions well), but more completely than closed code would.
Some cl o s ed code would provi de this tra n s p a ren c y. If code were more modular—if a code writer simply pulled parts off the shelf to plug into her system, as if
she were buying spark plugs for a car—then e ven if the code for these components
was closed, the functions and regulation of the end product would be open.4 Componentized architecture could be as transparent as an open code architecture, and
transparency could thus be achieved without opening the code.

The best code (from the pers pective of con s ti tuti onal va lues) is both modu l a r
and open . Modu l a ri ty en su res that bet ter com pon ents could be su b s ti tuted for
worse. And from a competitive perspective, modularity permits greater competition
in the development of improvements in a particular coding project.

It is plausible, however, that particular bits of code could not be produced if it
were produced as open code,that closed code may sometimes be necessary for competitive survival. If so, then the compromise of a component system would permit
s om ething of the best of both worl d s — s ome com peti tive adva n t a ge along wi t h
transparency of function.

I've argued for transparent code because of the constitutional values it embeds. I
have not argued against code as a regulator or against regulation. But I have argued
that we insist on transparency in regulation and that we push code structures to enhance that transparency.

The law presently does not do this. Indeed, as Mark Lemley and David O'Brien
argue, the existing structure of copyright protection for software tends to push the
development of software away from a modular structure.5 The law prefers opaque to
transparent code; it constructs incentives to hide code rather than to make its functionality obvious.

Ma ny have argued that the law 's pre s ent incen tives are inef f i c i ent—that they
tend to reduce competition in the production of software.6 This may well be right.
But the greater perversity is again constitutional.Our law creates an incentive to enclose as much of an intellectual commons as possible. It works against publicity and
transparency, and helps to produce,in effect, a massive secret government.

Here is a place for con c rete legal ch a n ge . Wi t h o ut re s o lving the qu e s ti on of
whether closed or open code is best, we could at least push closed code in a direction
that would fac i l i t a te gre a ter tra n s p a ren c y. Yet the inertia of ex i s ting law — wh i ch
gives sof t w a re manu f actu rers ef fectively unlimited terms of pro tecti on — work s
against change. The politics is just not there.

R E S P O N S E S O F A D E M O C R A C Y

In his rightly famous book Profiles in Courage, then-Senator John F. Kennedy tells
the story of Daniel Webster, who, in the midst of a fight over a pact that he thought
would divi de the nati on , said on the floor of the Sen a te , " M r. Pre s i den t , I wish to

2 2 6

speak today, not as a Massachusetts man, nor as a Northern man, but as an American. . . . "7

When Webster said this—in 1850—the words "not as a Massachusetts man" had
a significance that we are likely to miss today. To us, Webster's statement seems perfectly ordinary. What else would he be but an American? How else would he speak?
But these words came on the cusp of a new time in the United States. They came
just at the moment when the attention of American citizens was shifting from their
citizenship in a state to their citizenship in the nation. Webster spoke just as it was
becoming possible to identify yourself, apart from your state, as a member of a nation.

As I've said,at the founding citizens of the United States (a contested concept itself) were citizens o f particular states first. They were loyal to their own states because their lives were determined by where they lived. Other states were as remote to
them as Tibet is to us—indeed, today it is easier for us to go to Tibet than it was then
for a citizen of South Carolina to visit Maine.

Over time, of course, this changed. In the struggle leading up to the Civil War, in
the battles over Reconstruction, and in the revolution of industry that followed, ind ivi dual citi zen s' s ense of t h em s elves as Am ericans grew. In those nati onal exch a n ges and stru ggl e s , a nati onal iden ti ty was born . O n ly wh en citi zens were
engaged with citizens from other states was a nation created.

It is easy to for get these mom ents of tra n s form a ti on , and even easier to imagi n e
that they have happen ed on ly in the past. Yet no one can deny that the sense of bei n g
"an Am eri c a n" s h i f ted in the nineteenth cen tu ry, just as no one can deny that the sen s e
of being "a Eu rope a n" is shifting in Eu rope tod ay. Na ti ons are built as people ex experience ce them s elves inside a com m on po l i tical cultu re . This ch a n ge con ti nues for us tod ay.
We stand today just a few years before where Webster stood in 1850. We stand on
the brink of being able to say, "I speak as a citizen of the world," without the ordinary person thinking, "What a nut." We stand just on the cusp o f a time when ordinary citizens will begin to feel the effects of the regulations of other governments,
just as the citizens of Massachusetts came to feel the effects of slavery and the citizens of Virginia came to feel the effects of a drive for freedom. As Nicholas Negroponte puts it, "Nations today are the wrong size. They are not small enough to be
local and they are not large enough to be global."8 This misfit will matter.

As we, citizens of the United States, spend more of our time and money in this
space that is not part of any particular jurisdiction but subject to the regulations of
all jurisdic tions, we will increasingly ask questions about our status there. We will
begin to feel the entitlement Webster felt, as an American, to speak about life in another part of the United States. For us, it will be the entitlement to speak about life
in another part of the world, grounded in the feeling that there is a community of
interests that reaches beyond diplomatic ties into the hearts of ordinary citizens.

What will we do then? When we feel we are part of a world, and that the world
regulates us? What will we do when we need to make choices about how that world
regulates us, and how we regulate it?

2 2 7

The we a weariness with govern m ent that I de s c ri bed at the end of the last ch a pter is not
a con d i ti on wi t h o ut cause. But its cause is not the death of a ny ideal of dem oc rac y. We
a re all sti ll dem oc ra t s ; we simply do not like what our dem oc racy has produ ced . An d
we cannot imagine ex tending what we have to new domains like cybers p ace . If t h ere
were just more of the same there — m ore of the excesses and betrayals of govern m en t
as we have come to know it—then bet ter that there should be less.

There are two problems here, though only one that is really tied to the argument
of this boo k , and so on ly one that I wi ll discuss in any dept h . The other is mu ch
deeper—a sense of a basic corruption in any syst em that would allow so much political influence to be peddled by those who hand out money. This is the corruption
of campaign financing, a corruption not of people but of process. Even good souls
in Con gress have no ch oi ce but to spend an ever- i n c increasing amount of t h eir ti m e
raising an ever-increasing amount of money to compete in elections. This is an arms
race,and our Supreme Court has effectively said that the Constitution requires it.9
But there is a second, oddly counterintuitive reason for this increasing failure of
democracy. This is not that government listens too little to the views of the public.
It is that government listens too much. Every fancy of the population gets echoed in
polls,and these polls in turn pulse the democracy. Yet the message the polls transmit
is not the message of democracy; their frequency and influence is not the product of
increased significance. The president makes policy on the basis of overnight polling
only because overnight polling is so easy.

This is partly a technology problem. Polls mark an interaction of technology and
democracy that we are just beginning to understand. As the cost o f monitoring the
current view of the population drops, and as the machines for permanent monitoring of the population are built, we are producing a perpetual stream of data about
what "the people" think about every issue that government might consider.

A certain kind of code perfects the machine of m on i tori n g — code that automates perfect sample selection, that facilitates databases of results, and that simplifies the process of connecting. We rarely ask,however, whether perfect monitoring is
a good.

It has never been our ideal—constitutionally at least—that democracy be a perfect reflection of the present temperature of the people. Our framers were keen to
design structures that would mediate the views of the people. Democracy was to be
more than a string of excited utterances of the people. It was to be deliberative, reflective,and balanced by limitations imposed by a constitution.

But maybe, to be consistent with the arguments from part 3, I should say that at
least there was a latent ambi g u i ty abo ut this qu e s ti on . In a world wh ere el ecti on s
were extremely costly and communication was complicated, democracy had to get
by with infrequent elections. Nevertheless, we cannot really know how the framers
would have reacted to a technology that allows perfect and perpetual polling.

There is an important reason to be skeptical of the flash pulse of the people. The
flash pulse is qu e s ti on a ble not because the people are uneducated c a ted or incapable of
good judgment, and not because democracy needs to fail, but because it is often the

2 2 8

produ ct of i gn ora n ce . People of ten have ill - i n form ed or parti a lly inform ed vi ews
that they simply repeat as judgments when they know that their judgments are not
being particularly noticed or considered.

Technology encourages this sort of judgment. As a consequence of the massive
i n c rease in reporting on news , we are ex po s ed to a gre a ter ra n ge of i n form a ti on
about the world today than ever before. This exposure, in turn, gives us confidence
in our judgment. Never having heard of East Timor, people when asked might well
have said,"I don't know." But having seen ten seconds on TV, or thirty lines on a web
portal news page , gives them a spin they didn't have before . And they repeat this
spin, with very little value added.

The solution to this problem is not less news, or a ban on polling. The solution
is a better kind of polling. The government reacts to bad poll data because that is the
only data we have. But these polls are not the only possible kinds of polls. There are
techniques for polling that compensate for the errors of the flash poll and produce
judgments that are both more considered and more stable.

An example is the "del i bera tive" po ll devi s ed by Profe s s or James Fishkin.1 0
Rather than a pulse, Fishkin's polls seek an equilibrium. They bring a cross-section
of people together for a weekend at a time. These people, who represent all segments
of a society, are given information before the poll that helps ensure that they know
something about the subject matter. After being introduced to the topic of the poll,
they are then divided into small juries and over the course of a couple of days argue
about the topic at issue and exchange views about how best to resolve it. At the end
they are asked about their views,and their responses at this point form the "results"
of the poll.

The great advantage of this system is not only that information is provided but
that the process is deliberative. The results emerge out of the reasoning of citizens
debating with other citizens. People are not encouraged to just cast a ballot. They
give reasons for their ballot, and those reasons will or will not persuade.

We could imagine (we could dream) of this process ex tending gen era lly. We
could imagine it becoming a staple of our political life. And if it did,it might well do
good , as a co u n counterweight ght to the flash pulse and the perpetu a lly intere s ted proce s s
that ordinary g overnment is. It would be a corrective to the process we now have,
and one that might bring hope.

Cyberspace might make this process where reasons count more possible; it certainly makes it e ven more necessary. It is possible to imagine using the architecture
of the space to de s i gn del i bera tive forums m s , wh i ch could be used to implem en t
Fishkin's polling. But my message throughout is that cyberspace makes the need all
the more urgent.11

Th ere is a magic in a process wh ere re a s ons count—not wh ere ex perts rule or
where only smart people have the vote, but where power gets set in the face of reason. The magic is in a process where citizens give reasons, and citizens understand
that power is constrained by these reasons.

2 2 9

This was the magic that Tocqu evi lle wro te of wh en he told the world of t h e
amazing system of juries in the United States. Citizens serving on juries must make
re a s on ed , persu a s ive arguments in coming to dec i s i ons that of ten have ex tra ord inary consequences for social and political life. Writing in 1835, Tocqueville said of
juries:

The jury . . . serves to communicate the spirit of the judges to the minds of all the
citizens; and this spirit, with the habits which attend it, is the soundest preparation for free institutions. It imbues all classes with a respect for the thing judged
and with the noti on of ri gh t . . . . It te aches men to practi ce equ i ty; every man
learns to judge his neighbor as he would himself be judged. . . . The jury teaches
every man not to recoil before the responsibility of his own actions and impresses
him with that manly confidence without which no political virtue can exist. It invests each citi zen with a kind of m a gi s trac y; it makes them all feel the duties e s
which they are bound to discharge towards society and the part which they take
in its government. By obliging men to turn their attention to other affairs than
their own, it rubs off that private selfishness which is the rust of society.12

It wasn't Tocqueville, however, or any other theorist, who sold me on this ideal.
It was a lawyer who first let me see the power of this idea—a lawyer from Madison,
Wisconsin, my uncle, Richard Cates.

We live in a time when the sane vilify lawyers. No doubt lawyers are in part responsible for this. But I can't accept it,and not only because I train lawyers for a living. I can't accept it because etched into my memory is a picture my uncle sketched,
explaining why he was a law yer. In 1974 he had just retu rn ed from Wa s h i n g ton ,
where he worked for the House Committee on Impeachment—of Nixon, not Clinton,though Hillary Rodham was working with him. I pressed him to tell me everything; I wanted to hear about the battles. It was not a topic that we discussed much
at home. My parents were Republicans. My uncle was not.

My uncle's job was to teach the congressmen about the facts in the case—to first
learn everything that was known,and then to teach this to the members of the committee. Although there was much about his story that I will never forget, the most
compelling part was not really related to the impeachment. My uncle was describing
for me the essence of his job—both for the House and for his clients:

It is what a lawyer does, what a good lawyer does,that makes this system work. It
is not the blu f fin g, or the outra ge , or the stra strategies and tacti c s . It is som et h i n g
much simpler than that. What a good lawyer does is tell a story that persuades.
Not by hiding the truth or exc i ting the em o ti on , but using re a s on , t h ro u gh a
story, to persuade.

When it works, it does something to the people who experience this persuasion. Some, for the first time in their lives, see power constrained by reason. Not

2 3 0

by votes, not by wealth, not by who someone knows—but by an argument that
persuades. This is the magic of our system,however rare the miracles may be.

This picture stuck—not in its elitist version, of experts deciding what's best, nor
in its Rikki Lake version, of excited crowds yelling opponents down. But in its simple version that juries know. And it is this simple picture that our current democracy
misses. Where through deliberation, and understanding, and a process of building
community, judgments get made about how to go on.

We could build some o f this back into our democracy. The more we do, the less
significant the flash pulses will be. And the less significant these flash pulses are, the
more we might have faith again in that part of our tradition that made us revolutionaries in 1791—the commitment to a form of government that respects deliberation, and the people,and that stands opposed to corruption dressed in aristocratic
baubles.

S E V E N T E E N

w h a t d e c l a n d o e s n ' t g e t

Decl an McCullagh l agh is a wr it er wh o wor ks f or Wired News. He al so r uns a
"listserve" that feeds to subscribers the bulletins that he has decided to forward and
facilitates a discussion among these members. The list was originally called "Fight
Censorship," and it initially attracted a large number of subscribers who were eager
to organize to resist the government's efforts to "censor" the Net.

But Declan uses the list now for more than a discussion of censorship. He feeds
to the list other news that he imagines his subscribers will enjoy. So in addition to
news about efforts to eliminate porn from the Net, Declan includes reports on FBI
wiretaps, or efforts to protect privacy, or the government's efforts to enforce the nation's antitrust laws. I'm a subscriber; I enjoy the posts.

Declan's politics are clear. He's a smart, if young, libertarian whose first reaction
to any suggestion that involves government is scorn. In one recent message,he cited
a story about a British provider violating fax spam laws; this,he argued,showed that
l aws reg u l a ting e-mail spam are usel e s s . Th ere is one unifying theme to Decl a n's
po s t s : l et the Net alon e . And with a som etimes sel f - ri gh righteous sneer, he ri d i c u l e s
those who question this simple, if powerful, idea.

I've watched Declan's list for some time. For a brief time I watched the discussion part of the list as well. But the most striking feature about this list to me is the
slow emergence of a new topic of concern—one that now gets more posts than "censorship."

This topic is Y2K—the " year 2000 probl em" that thre a tens to disru pt mu ch in
our social and economic life as computers discover that the new millennium does
not compute. As clearly as Declan's libertarianism comes through, so too does his
obsession with Y2K. He is either terrified or perversely amused by what the new millennium will bring to the computer next door.

From the perspective of this book, these twin concerns—with regulation by the
state and regulation by code—are quite consistent. Just as we should worry about
the bad reg u l a ti ons of l aw, so too should we worry abo ut the bad reg u l a ti ons of

2 3 2

code. And from the perspective of this book,Y2K is our first real crisis in code. It is
the first time that the cultu re as a whole wi ll have to con f ront the envi ron m en t a l
damage done by shortsighted coders.Like shortsighted lawmakers,they have created
a crisis whose proportions we cannot yet see.

But from the pers pective of Decl a n's libert a ri a n i s m , these twin con cerns are
harder to reconcile.Y2K is the product of a certain kind of libertarianism. It is the
produ ct of not thinking thro u gh the reg u l a ti on of code , and of l aw not properly
holding coders re s pon s i ble for their code . Thousands of coders went abo ut thei r
work thinking their actions were simply their own. The culture and the legal system
essentially treated those actions as those of individuals acting alone. Now, years after the first bad code was compiled, we are faced with a kind of environmental disa s ter: we are su rro u n ded by code that in cri tical and unpredictable i ct a ble ways wi ll
misfire—at a minimum causing the economy millions of dollars, and under some
doomsday scenarios costing much worse damage.

It is a lack of a certain kind of regulation that produced the Y2K problem, not
too much regulation. An overemphasis on the private got us here,not an overly statist federal govern m en t . Were the tort sys tem bet ter at holding produ cers re s responsible for the harms they create, code w riters and their employers would have b een
more concerned with the harm their code would create.Were contract law not so eager to all ow liabi l i ty in econ omic tra n s acti ons to be waived , the licenses that abs o lved the code wri ters of a ny po ten tial liabi l i ty from bad code would not have
induced an even greater laxity in what these code writers were producing. And were
the intell ectual property sys tem more con cern ed with captu ring and pre s ervi n g
k n owl ed ge than with all owing priva te actors to captu re and pre s erve prof i t , we
might have had a copyright system that required the lodging of source code with the
government before the protection of copyright was granted,thus creating an incentive to preserve source code and hence create a resource that does not now exist but
that we might have turned to in undoing the consequences of this bad code. If in all
these ways government had been diff erent, the problems of Y2K would have b een
different as well.1

Y2K is just one example of a more general point that has been at the core of this
book. We've had technology in our lives forever, and people have written about the
con s equ en ces of tech n o l ogy for soc i ety since there has been tech n o l ogy. But this
continuity should not blind us to an important disconnect we are about to see. Code
may be only a difference in degree, but a difference in degree at some point becomes
a differen ce in kind. The uninten ded con s equ en ce of priva te coding beh avi or is a
time-bomb set to explode over the next year or so. The Y2K problem should awaken
us to other time-bombs in our lives—that is, to the general effect that code will have
on our lives.

For here is a reality that all this "code talk" obscures. By speaking as I have about
the code in cyberspace, by describing how government might regulate that code, by
making it seem as if the worlds I am describing were in some sense elsewhere,I have

w h a t d e c l a n d o e s n ' t g e t

2 3 3

ob s c u red an obvious and cri tical point that the Y2K crisis makes re a l : code is not
elsewhere,and we are not elsewhere when we feel its effects. As Andrew Shapiro puts
i t : "Seeing cybers p ace as el s ewh ere . . . m i s con s true[s] its legal sign i f i c a n ce . It . . .
keep[s] us from seeing the way that regulatory forces like . . . code, which some say
are 'there,' are actually affecting us here."2

We live life in real space, subject to the effects of code. We live ordinary lives, subject to the effects of code. We live social and political lives, subject to the effects of
code. Code regulates all these aspects of our lives, more pervasively over time than
a ny other reg u l a tor in our life . Should we remain passive abo ut this reg u l a tor ?
Should we let it affect us without doing anything in return?

And thus again the odd ju x t a po s i ti on of Decl a n's two ob s e s s i on s . G overn m en t s
should interven e , at a minimu m , wh en priva te acti on has public con s equ en ce s ; wh en
s h ort s i gh ted acti ons thre a ten to cause lon g - term harm ; wh en failu re to intervene undermines sign i ficant con s ti tuti onal va lues and important indivi dual ri gh t s ; and wh en
a form of l i fe em er ges that may thre a ten va lues we bel i eve to be fundamen t a l .

Yet so pervasive is our sense o f the failure of government that a writer as intelligent as Declan cannot see the implications of these two great evils that he does so
much to report. If we believe that government cannot do anything good, then Declan's plea—that it do nothing—makes sense. And if government can do nothing,
then it follows that we should treat these man-ma de disasters as natural. Just as w e
s peak of the disaster of the West Coast sliding into the Pac i f i c , so too should we
speak of a disaster of code sliding us into another dark age. Neither can we do anything about, yet both are great topics for growing audiences.

I 've advoc a ted a different re s pon s e . We need to think co ll ectively and sen s i bly
about how this emerging reality will affect our lives. Do-do-nothingism is not an answer; something can and should be done.

I've argued this, but not with much hope. So central are the Declans in our political culture today that I confess I cannot see a way around them. I have sketched
small steps;they seem very small.I've described a different ideal;it seems quite alien.
I've promised that something different could be done, but not by any institution of
government that I know. I've spoken as if there could be hope. But Hope was just a
television commercial.

The truth, I suspect, is that the Declans will win—at least for now. We will treat
code-based environmental disasters—like Y2K, like the loss of privacy, like the censorship of filters,like the disappearance of an intellectual commons—as if they were
produced by gods, not by Man. We will watch as important aspects of privacy and
free speech are erased by the emerging architecture of the panopticon, and we will
speak, like modern Jeffersons, about nature making it so—forgetting that here, we
a re natu re . We wi ll in many domains of our social life come to see the Net as the
product of something alien—something we cannot direct because we cannot direct
a nyt h i n g. Som ething inste ad that we must simply accept , as it invades and tra n transforms our lives.

2 3 4

Some say this is an exc i ting ti m e . But it is the exc i tem ent of a teen a ger playing n g
chicken,his car barreling down the highway, hands held far from the steering wheel.
There are choices we could make, but we pretend that there is nothing we can do. We
choose to pretend; we shut our eyes. We build this nature, then are constrained by
this nature we have built.

It is the age of the ostrich. We are excited by what we cannot know. We are proud
to leave things to the invi s i ble hand. We make the hand invi s i ble by looking the
other way.

But it is not a great time, culturally, to come across revolutionary technologies.
We are no more ready for this revolution than the Soviets were ready for theirs. We,
like the Soviets, have been caught by a revolution. But we, unlike they, have something to lose.

A P P E N D I X

In chapter 7,I sketched briefly an argument for how the four modalities I described constrain differently. In this appendix, I want to extend that argument. My hope is to prothe market , n orm s , a n d
vi de a ri ch er sense of h ow these mod a l i ti e s — l aw,
architecture—interact as they regulate. Such an understanding is useful, but not necessary, to the argument of this book. I've therefore put it here, for those with an interest,
and too much time. Elsewhere I have called this approach "the New Chicago School."1

Law is a command backed up by the threat of a sanction. It commands you not to
commit murder and threatens a severe penalty if you do so anyway. Or it commands you
not to trade in cocaine and threatens barbaric punishments if you do. In both cases,the
picture of law is fairly simple and straightforward: don't do this, or else.

Obvi o u s ly law is mu ch more than a set of commands and thre a t s .2 L aw not on ly
commands certain behaviors but expresses the values of a community (when, for example, it sets aside a day to celebrate the birth of Martin Luther King, Jr.);3 constitutes or
regulates structures of government (when the Constitution, for example, establishes in
Article I a House of Representatives distinct from a Senate); and establishes rights that
individuals can invoke against their own government (the Bill of Rights). All these are
examples of law; by focusing on just one kind of law, I do not mean to diminish the significance of these other kinds. Still, this particular aspect of law provides a well-defined
constraint on individuals within the jurisdiction of the law giver, or sovereign. That constraint—objectively—is the threat of punishment.

Social n o rms con s train differen t ly. By social norm s , I mean those norm a tive constraints imposed not through the organized or centralized actions of a state, but through
the many slight and sometimes forceful sanctions that members of a community impose
on each other. I am not talking about patterns of behavior: it may be that most people
drive to work between 7:00 and 8:00 A.M., but this is not a norm.A norm governs socially
salient behavior, deviation from which makes you socially abnormal.4

L i fe is fill ed wi t h , con s ti tuted by, and defin ed in rel a ti on to su ch norm s — s ome of
which are valuable, and many of which are not. It is a norm (and a good one) to thank
others for service. Not thanking someone makes you "rude," and being rude opens you
up to a range of social sanctions, from ostracism to criticism. It is a norm to speak cautiously to a seatmate on an airplane, or to stay to the right while driving slowly. Norms
discourage men from wearing dresses to work and encourage all of us to bathe regularly.
Ordinary life is filled with such commands about how we are to behave. For the ordin a ri ly soc i a l i zed pers on , these commands con s ti tute a significant porti on of the constraints on individual behavior.

2 3 6

a p p e n d i x

What makes norms different, then, is the mechanism and source of their sanction:
they are imposed by a community, not a state. They are similar to law in that,at least objectively, their constraint is imposed after a violation has o occurred.

The con s traints of the m a rket a re different aga i n . The market con s trains thro u gh
price. A price signals the point at which a resource can be transferred from one person
to another. If you want a Starbucks coffee, you must give the clerk two dollars. The constraint (the two dollars) is simultaneous with the benefit you want (the coffee). You may,
of co u rs e , b a r gain to pay for the ben efit later ("I'd gl adly pay you Tu e s d ay for a hamburger today"), but the obligation is incurred at the time you receive the benefit. To the
extent that you stay in the market, this simultaneity is preserved. The market constraint,
then,unlike law and norms, does not kick in after you have taken the benefit you seek;it
kicks in at the same time.

This is not to say that market tra n s acti ons cannot be tra n s l a ted into law or norm
transactions. Indeed,market transactions do not exist except within a context of law and
norms. You must pay for your coffee; if you do not,the law of theft applies. Nothing in
the market requires that you tip the waiter, but if you do not, norms kick in to regulate
your stinginess. The constraints of the market exist because of an elaborate background
of law and norms defining what is buyable and sellable,as well as rules of property and
contract for how things may be bought and sold. But g iven these laws and norms, the
market still constrains in a distinct way.

The constraint of our final modality is neither so contingent nor, in its full range, so
dependent. This is the constraint of architecture—the way the world is, or the ways specific aspects of it are. Architects call it the built environment; those who don't give out
names just recognize it as the world around them.

Plainly some of the constraints of architecture are constraints we have made (hence
the sense of "architecture") and some are not.A door closes off a room. When locked,the
door keeps you out. The constraint functions not as law or norms do—you cannot ignore the constraint and suffer the consequence later. Even if the constraint imposed by
the door is one you can overcome—by breaking it down perhaps, or picking the lock—
the door still constrains, just not absolutely.

Some architectural constraints,however, are absolute.Star Trek notwithstanding, we
cannot travel at warp speed. We can no doubt travel fast,and technology has enabled us
to travel faster than we used to. Nonetheless, we have good reason (or at least physicists
do) for believing that there is a limit to the speed at which we can travel. As an old T-shirt put it,"186,282 miles per second. It's not just a good idea. It's the law."

But wh et h er absolute or not, or wh et h er man-made or not, we can con s i der these
constraints as a single class—as the constraints of architecture, or real-space code. What
unites this class is the agency of the constraint: no individual or group imposes the constraint, or at least not directly. Individuals are no doubt ultimately responsible for much
of the constraint, but in its actual execution the constraint takes care of itself.Laws need
police, prosecutors, and courts to have an effect; a lock does not. Norms require that individuals take note of nonconforming behavior and respond accordingly; gravity does
n o t . The con s traints of a rch i tectu re are sel f - exec uting in a way that the con s traints of
law, norms,and the market are not.

This fe a tu re of a rch i tectu re — s el f - exec uti on—is ex trem ely important for understanding its role in regulation. It is particularly important for unseemly or unjust regulation. For example, to the extent that we can bring about effects through the automatic

a p p e n d i x

2 3 7

constraints of real-space code, we need not depend on the continued agency, loyalty, or
reliability of individuals. If we can make the machine do it, we can be that much more
confident that the unseemly will be done.

The launching of nuclear missiles is a nice example. In their original design,missiles
were to be launched by individual crews located within missile launch silos. These men
would have been ordered to launch their missiles, and the ex pect a ti on was that they
would do so. Laws, of course,backed up the order—disobeying the order to launch subjected the crew to court-martial.5

But in testing the system, the army found it increasingly unreliable. Always the decision to launch was che cked by a judgment made by an individual, and always that indivi dual had to dec i de wh et h er the order was to be obeyed . P l a i n ly this sys tem is less
reliable than a system where all the missiles are wired,as it were, to a single button on the
president's desk. But we might believe that there is value in this second check, that the
agency of the action by the soldier ensures some che ck on the decision to launch.6

This is an important consequence of the automatic nature of the constraints of architecture. Law, norms, and the market are constraints checked by judgment. They are
enacted only when some person or group chooses to do so. But once instituted, architectural constraints have their effect until someone stops them.

Agency, then, is one distinction between the four constraints. The temporality of the

constraint—when it is imposed—is a second one.

Here I should distinguish bet ween two different pers pective s : that of s om eone observing when a constraint is imposed (the objective perspective), and that of the person
who experiences the constraint (the subjective perspective). So far my description of the
four constraints in this single model has been from the objective perspective. From that
perspective they are quite different, but from a subjective perspective they need not differ at all.

From the obj ective pers pective the differen ce is bet ween con s traints that dem a n d
payment up front and constraints that let you play and then pay. Architecture and the
market constrain up front; law and norms let you play first. For example, think of the
constraints blocking your access to the air-conditioned home of a neighbor who is gone
for the wee ken d . L aw con s trains yo u — i f you break in, you wi ll be tre s p a s s i n g. Norm s
con s train you as well — i t's unneighborly gh neighborly to break into your nei gh bor 's house. Both of
these con s tra i n t s , h owever, would be impo s ed on you a f ter you bro ke into the house.
They are prices you might ha ve to pay lat er.7 The architectural constraint is the lock on
the door—it blocks you as you are trying to enter the house. The market constrains your
ownership of an air conditioner in the same way—it demands money before it will g ive
you on e . From an obj ective pers pective what distinguishes these two classes of constraints is their temporality—when the sanction is imposed.

From a subjective perspective, however, all these differences may disappear. Subjectively, you may well feel a norm constraint long before you violate it. You may feel the
constraint against breaking into your neighbor's house just at the thought of doing so.
Whatever the temporality of the constraint from an objective perspective, you may experi en ce the con s traint differen t ly. A con s traint may be objectively ctively ex po s t , but ex perienced subjectively ex ante.

The point is not limited to norms. Think about a child and fire. Fire is a bit of realspace code: the consequences are f elt as soon as the constraint it imposes is violated. A
child learns this the first time he puts his hand near a flame. Thereafter, the child inter-

2 3 8

a p p e n d i x

n a l i zes the con s traint of f i re before put ting his hand in a fire . Bu rn ed on ce , the ch i l d
knows not to put his hand so near the flame a second time.8

We can de s c ri be this ch a n ge as the devel opm ent of a su bj ective con s traint on the
child's behavior. We can then see how the idea extends to other constraints. Think about
the stock market. For those who do not shop very much, the constraints of the market
may indeed be only the objective constraint of the price demanded when they make a
purchase. However, for those who experience the market regularly—who have,as it were,
a sense of the market—the con s traints of the market are qu i te differen t . Su ch peop l e
come to know them as second nature, which guides or constrains their actions. Think of
a stockbroker on the floor of an exchange. To be a great broker in that context is to come
to know the market "like the back of your hand," to let it become second nature. In the
terms that we've used,this broker has let the market become subjectively part of who she
is.

Each constraint, then, has a subjective and an objective aspect. Laws are objectively
ex post, but for most of us,the fact that a law directs us in a particular way is usually sufficient to make it a subjective constraint. (It is not the objective threat of jail that constrains me from cheating on my taxes; instead,I have made subjective the constraints of
the law with respect to taxes. Honest,IRS. This is true.) As a subjective constraint,it constrains us before we act.

For those who are fully mature, or fully integrated, all objective constraints are subjectively effective prior to their actions. They feel the constraints of real-space code, of
law, of norms,and of the market, before they act. For the completely immature, or totally
alienated, few objective constraints are subjectively effective. They step in the mud and
only then learn about the constraint of mud; they steal bread and only then learn about
the punishments of the law; they show up at a wedding in cut-offs and only then learn
about the scorn of their friends;they spend all their money on candy and only then learn
of the constraint of market scarcity. These two types mark out the extremes; most of us
are somewhere in between.

The more subjective a constraint,then,the more effective it is in regulating behavior.
It takes work to make a con s traint su bj ective . An indivi dual must ch oose to make it a
part of who he or she is. To the extent that the norm is made subjective, it constrains simultaneously with the behavior it regulates.

This points to one final distinction between law and norms, on the one hand, and
real-space code, on the other. Law and norms are more efficient the more subjective they
a re , but they need some minimal su bj ectivi ty to be ef fective at all . The pers on cons tra i n ed must know of the con s tra i n t . A law that sec ret ly punishes people for of fen s e s
they do not know exist would not be effective in regulating the behavior it punishes.9

But this is not the case with architecture. Architecture can constrain without any subjectivity. A lock constrains the thief whether or not the thief knows that it is a lock blocking the door. The distance between two places constrains the intercourse between those
two places whether or not anyone in those places understands that constraint. This point
is a corollary of the point about agency: just as a constraint need not be imposed by an
agent,neither does the subject need to understand it.

Arch i tectu ral con s tra i n t s , t h en , work wh et h er or not the su bj ect knows they are
working, while law and norms work only if the subject knows something about them. If
the subject has internalized them,they can constrain whether or not the expected cost of
complying exceeds the benefit of deviating. Law and norms can be made more code-like

a p p e n d i x

2 3 9

the more they are internalized. But internalization takes work.

Though I have used language invoking architects, my language is not the language of
a rch i tect s . It is inste ad sto l en , and ben t . I am not a scholar of a rch i tectu re , but I have
taken from architecture its insight about the relationship between the built environment
and the practices that environment creates.10 Neither architects nor I take this relationship to be determ i n a tive . S tru ctu re X does not determine beh avi or Y. In s te ad , t h e s e
forms are alw ays simply influ en ces that can ch a n ge , and wh en they are ch a n ged , t h ey
change the affected behavior.

Like Michael Sorkin, I believe that "meanings inhere in forms, and that the settings
for social life can aid its fulfillment." His book Local Code: The Constitution of a City at
42ºN Latitude suggests each feature of the model I am describing, including the ambiguity between law and architecture (building codes) and the constitution the two enable.
Wh a tever the source of the con tent of these code s , he wri te s , "t h eir con s equ en ces are
built."11 This is the feature to focus on.

My suggestion is that if we relativize regulators—if we understand how the different
m od a l i ties reg u l a te and how they are su bj ect , in an important sen s e , to law — t h en we
will see how liberty is constructed not simply through the limits we place on law. Rather,
liberty is constructed by structures that preserve a space for individual choice,however
that choice may be constrained.

We are entering a time when our power to muck about with the structures that regulate is at an all-time high. It is imperative,then,that we understand just what to do with
this power. And,more important, what not to do.

N O T E S

P R E F A C E

1. See http://mit.edu/cfp6.

C H A P T E R O N E

1. Paulina Borsook,"How Anarchy Works," Wired 110 (October 1995):3.10, available online at http : / / w w w. wi red . com / wi red / a rch ive / 3 . 1 0 / i etf . h tml (vi s i ted May 30, 1 9 9 9 ) , qu o ti n g
Netlander, David Clark.

2. James B oyle, talk at Telecommunications Policy Research Conference (TPRC), Washington, D.C., September 28, 1997. David Shenk discusses the libertarianism that cyberspace
i n s p i res (as well as other, m ore fundamental probl ems with the age) in a bri lliant cultu ra l
h ow - to book that re s pon s i bly covers both the tech n o l ogy and the libert a ri a n i s m ; s ee Da t a
Smog: Surviving the Information Glut (San Francisco, Harper Edge, 1997), esp. 174–77. The
book also de s c ri bes tech n ore a l i s m , a re s pon s ive movem ent that adva n ces a more balanced
picture of the relationship between technology and freedom.

3. See Kevin Kelley, Out of Control: The New Biology o f Machines, Social Systems, and the

Economic World (Reading, Mass.: Addison-Wesley, 1994),119.

4. As Stephen Holmes has put it, "Rights depend upon the competent exercise of . . . legitimate public power. . . . The largest and most reliable human rights organization is the liberal state. . . . Unless society is political ly well organized,there will be no individual liberties
and no civil society"; "What Russia Teaches Us Now: How Weak States Threaten Freedom,"
American Prospect 33 (1997): 30,33.

5. This is a dark picture, I confess,and it contrasts with the picture of control drawn by
Andrew Shapiro in The Control Revolution (New York: Public Affairs,1999). As I discuss later,
however, the difference between Shapiro's view and my o wn turns on the ext ent to which architectures enable top-down regulation. In my view, one highly probable architecture would
enable greater regulation than Shapiro believes is likely.

6 . See "We Kn ow Wh ere You Wi ll Live ," Com p uters , Freedom , and Privacy Con feren ce ,

March 30,1996,audio link available at http://www-swiss.ai.mit.edu/~switz/cfp96/#audio.

7 . See Wi lliam J. Mi tch ell , Ci ty of Bits: Spa ce , Pl a ce , and the In foba h n ( Ca m bri d ge , Ma s s . :
MIT Pre s s , 1 9 9 5 ) , 1 1 1 . In mu ch of this boo k , I work out Mi tch ell 's ide a , t h o u gh I drew the
m et a ph or from others as well . Ethan Katsh discusses this noti on of s of t w a re worlds in "Sof t w a re
Worlds and the First Am en d m en t : Vi rtual Doorkeepers in Cybers p ace ," Un ivers i ty of C h i c a go Le -
gal Fo rum ( 1 9 9 6 ) : 3 3 5 ,3 3 8 . Joel Rei den berg discusses the rel a ted noti on of "l ex inform a ti c a" i n
" Lex In form a ti c a : The Formu l a ti on of In form a ti on Policy Rules Th ro u gh Tech n o l ogy," Texa s
Law Revi ew 76 (1998): 5 5 3 . I have been espec i a lly influ en ced by James Boyl e's work in the are a .

2 4 2

n o t e s

I discuss his book in ch a pter 9, but see also " Foucault in Cybers p ace : Su rvei ll a n ce , Soverei gn ty,
and Ha hardware red Cen s ors ," Un ivers i ty of Ci n ci n n a ti Law Revi ew 66 (1997): 1 7 7 . For a recent and
powerful use of the ide a , s ee Shapiro, The Co n trol Revol u ti o n . Mi tch Ka por is the father of t h e
m eme "a rch i tectu re is po l i ti c s" within cybers p ace talk. I am indebted to him for this.

8 . Ma rk Stefik , " Ep i l og u e : Ch oi ces and Dre a m s ," in In tern et Dreams: Arch archetypes s , Myt h s ,

and Metaphors, edited by Mark Stefik (Cambridge, Mass.:MIT Press,1996),390.

9. Missouri v Holland, 252 US 416,433 (1920).
1 0 . Ri ch a rd Stall m a n , for ex a m p l e , or ga n i zed re s i s t a n ce to the em er gen ce of p a s s words at
M I T. Pa s s words are an arch i tectu re that fac i l i t a tes con trol by excluding users not "of fic i a lly sanctioned on ed ." S teven Lev y, Ha ckers ( G a rden Ci ty, N . Y. : An ch or Pre s s / Do u bl ed ay, 1 9 8 4 ) ,4 1 6 – 1 7 .

C H A P T E R T W O

1. See, for example,Stanley Fish, Doing What Comes Naturally (Durham,N.C.: Duke University Press, 1989), ch.17.

2. It is also hypothetical. I have constructed this story in light of what could be, and in

places is. But I'm a law professor; I make up hypotheticals for a living.

3. One gets a good sense of the possibilities in this space from a how-to manual; one of
my favorites is Bruce Damer's Avatars! (Berkeley, Calif.: Peachpit Press, 1998). The range of
experiences and the possibilities outlined by Damer don't yet match the hypothetical I have
based this section on, but any difference is just a matter of coding.

4. "MUD" has had a number of meanings, originally Multi-User Dungeon, or Multi-User
Domain. A MOO is a "MUD, object-oriented." Sherry Turkle's analysis of life in a MUD or
M OO, Li fe on the Screen en: Id en ti ty in the Age of the In tern et ( New York : Si m on & Schu s ter,
1995), is still a classic. See also Elizabeth Reid,"Hierarchy and Power: Social Control in Cybers p ace ," in Co m mu n i ties in Cy bers pa ce , ed i ted by Ma rc A . Smith and Peter Ko ll ock (New
York : Ro ut l ed ge , 1 9 9 9 ) , 1 0 7 . The father — or god — of a MUD named LamdaMOO is Pavel
Cu rti s . See his account in " Mu d d i n g : Social Phen om ena in Tex t - Ba s ed Vi rtual Re a l i ti e s ," i n
Stefik, Internet Dreams, 265–92. For two magical pages of links about the history of MUDs,
see Lauren P. Burka, "The MUDline," available at http://www.apocalypse.org/pub/u/lpb/muddex/mudline.html (visited May 30, 1999); and Lauren P. Burka, "The MUDdex," available at
http://www.apocalypse.org/pub/u/lpb/muddex/ (visited May 30,1999).

5. A pareto superior move requires that at least one person be made better off and that no
one be made worse of f . See Robert Coo ter and Th omas Ul en , Law and Eco n o m i cs , 2d ed .
(Reading, Mass.: Addison-Wesley, 1997),12,41–42.

6. Jake Baker's given name was Abraham Jacob Alkhabaz, but he changed his name after
his parents' divorce. See Peter H. Lewis, "Writer Arrested After Sending Violent Fiction Over
Internet," New York Times, February 11,1995, 10.

7. The seven are comp, misc,news, rec,sci, soc,and talk. See Henry Edward Hardy, "The
Hi s tory of the Net , v 8 . 5 ," Septem ber 28, 1 9 9 3 , ava i l a ble at http : / / w w w. gri n . n et / ~ ctu rl ey /
gsezine/GS.WorldView/*HISTORY.OF.THE.NET/ (visited May 30,1999).

8. I have drawn from Jonathan Wallace and Mark Mangan's vivid account in Sex, Laws,
and Cyberspace (New York:M&T Books,1996),63,though more interesting variations on this
story circulate on the Net (I'm playing it safe).

9. See United States v Baker, 890 FSupp 1375, 1390 (EDMich 1995); see also Wallace and

Mangan, Sex, Laws, and Cyberspace, 69–77.

10. See Mike Godwin, CyberRights: Defending Free S peech in the Digital Age (New York:

Times Books, 1998),117–32.

11. No doubt the worm would interact with the operation of the machine,as it would interact with, for example,the operating system at least.

2 4 3

12. My example is drawn from Michael Adler, "Cyberspace,General Searches, and Digital
Con tra b a n d : The Fo u rth Am en d m ent and the Net - Wi de Se a rch ," Yale Law Jou rnal 1 0 5
(1996): 1093; cf. Laura B. Riley, "Concealed Weapon Detectors and the Fourth Amendment:
The Con s ti tuti on a l i ty of Rem o te Sense Enhanced Se a rch e s ," U C LA Law Revi ew 45 (1997):
2 8 1 , 3 2 5 – 2 7 . Adl er 's example provi des a nice para ll el to Arnold H. Loew y, "The Fo u rt h
Amendment as a Device for Protecting the Innocent," Michigan Law Review 81 (1983): 1229,
1244—though they reach opposite conclusions.

13. See William J. Stuntz, "The Substantive Origins of Criminal Procedure," Yale Law Jour -

nal 105 (1995): 393,406–7.

14. See, for example, Thomas A. Clancy, "The Role of Individualized Suspicion in Assessing the Re a s on a bl eness of Se a rches and Sei z u re s ," Un ivers i ty of Memphis Law Revi ew 2 5
(1995):483,632."Individualized suspicion . . . has served as a bedrock protection against unjustified and arbitrary police actions."

15. See United States v Place, 462 US 696,707 (1983).
1 6 . James Boyl e , Sh a m a n s , S of twa re , and Spl e ens: Law and the Co n s tru ction of the In fo r -

mation Society (Cambridge, Mass.: Harvard University Press,1996),4.

17. See Susan Freiwald,"Uncertain Privacy: Communication Attributes After the Digital

Telephony Act," Southern California Law Review 69 (1996): 949,951, 954.

18. Cf. John Rogers,"Bombs, Borders,and Boarding: Combatting International Terrorism
at United States Airports and the Fourth Amendment," Suffolk Transnational Law Review 20
(1997):501, n.201.

1 9 . See Mi tch ell Ka por, "The Sof t w a re De s i gn Ma n i fe s to," ava i l a ble at http : / /
w w w. kei . com / h om ep a ge s / m k a por / Sof t w a re _ De s i gn _ Ma n i fe s to. h tml (vi s i ted May 30, 1 9 9 9 ) ;
D avid Fa rber, "A No te on the Po l i tics of Privacy and In f ra s tru ctu re ," Novem ber 20, 1 9 9 3 ,
ava i l a ble at http : / / i c g. pobox . com / c i s 5 9 0 / re ad i n g.045.txt (vi s i ted May 30, 1 9 9 9 ) ; "Q u o t ati on s ," ava i l a ble at http : / / w w w. c s . york u . c a / ~ peter / 4 3 6 1 / qu o te s . h tml (vi s i ted May 30, 1 9 9 9 ) ;
see also Pamela Samuelson et al., "A Manifesto Concerning the Legal Protection of Computer
Programs," Columbia Law Review 94 (1994): 2308. Steven Johnson powerfully makes a similar point: "All works of architecture imply a worldview, which means that all architecture is in
some deeper sense political"; see Interface Culture: How New Technology Transforms the Way
We Create and Communicate (San Francisco: Harper Edge,1997),44. The Electronic Frontier
Foundation, originally cofounded by Mitch Kapor and John Perry Barlow, has updated Kapor's slogan "architecture is politics" to "architecture is policy." I prefer the original.

2 0 . See Steve Si l berm a n , "We're Teen , We're Queer, and We've Got E-Ma i l ," Wi red ( Novem ber 1994): 7 6 , 7 8 , 8 0 , repri n ted in Co m posing Cy bers pa ce: Id en ti ty, Co m mu n i ty, a n d
Knowledge in the Electronic Age, edited by Richard Holeton (Boston: McGraw-Hill,1998),116.

21. Cf. United States v Lamb, 945 FSupp 441 (NDNY 1996).
2 2 . Jed Ru ben feld has devel oped most ex ten s ively an interpretive theory that gro u n d s
meaning in a practice of reading across time, founded on paradigm cases; see "Reading the
Constitution as Spoken," Yale Law Journal 104 (1995): 1119, 1122; and "On Fidelity in Constitutional Law," Fordham Law Review 65 (1997): 1469.

2 3 . See Mi n n e sota v Di ckerso n , 508 US 366, 380 (1993) (Ju s ti ce An tonin Scalia con c u rring:"I frankly doubt . . . whether the fiercely proud men who adopted our Fourth Amendment would have allowed themselves to be subjected, on mere suspicion of being armed and
dangerous, to such indignity. . . . ").

C H A P T E R T H R E E

1 . My use of the term "a rch i tectu re" is som ewhat idiosyncratic ti c , but not com p l etely. I use it
in the sense spo ken of by Ch a rles Morris and Ch a rles Fer g u s on in " How Arch i tectu re Wi n s

2 4 4

Tech n o l ogy Wa rs ," Ha rva rd Business Revi ew ( Ma rch - April 1993): 8 6 . My usage is not qu i te the
u s a ge of com p uter scien ti s t s , except in the sense of a "s tru ctu re of a sys tem" ; s ee the defin i ti on
of a rch i tectu re in Pete Lo s h i n , TCP/IP Clearly Expl a i n ed , 2d ed .( Bo s ton : AP Profe s s i on a l ,1 9 9 7 ) .
2 . J. C . Her z , Su rfing on the In tern et: A Net h e a d 's Adven tu res On - Li n e ( Bo s ton : L i t t l e ,

Brown,1995),2–3.

3. This account of Chicago's network design may well be dated. I can verify its accuracy

only up to 1996.

4. The University of Chicago is a private university, so on its own force, the First Amendment would not constrain it. That distinguishes it from a public university, such as the University of California.

5 . See Hel en Ni s s en b a u m , "Va lues in the De s i gn of Com p uter Sys tem s ," Co m pu ters and

Society (March 1998): 38.

6. For an extremely readable description,see Loshin, TCP/IP Clearly Explained, 15–23;see
also Craig Hunt, TCP/IP Network Administration, 2d ed.(Sebastopol, Calif.: O'Reilly & Associates, 1998),8–22; Trust in Cyberspace, edited by Fred B. Schneider (Washington, D.C.: National Academy Press,1999),29–36.

7. Peter Steiner, cartoon, New Yorker, July 5,1993,61.
8. See Nicholas Negroponte, Being Digital (New York: Alfred A. Knopf,1995),18,179–80.
9 . This was the hope , as Ju s ti ce Sa n d ra Day O' Con n or saw it, of the Com mu n i c a ti ons Decen c y
Act (CDA) of 1 9 9 6 . See Reno v Am erican Civil Li berties Un i o n , 117 SCt 2329, 2351–57 (1997) (Ju sti ce Sa n d ra Day O' Con n or con c u rring in part and dissen ting in part ) . Its obj ective , in her vi ew,
was to requ i re the use of tech n o l ogies that would make it fe a s i ble to zone kids out of p a rts of t h e
Net wh ere porn ogra phy was pre s en t . While O' Con n or thought the CDA uncon s ti tuti on a l , s h e
su gge s ted that another statute , m ore narrowly tailored , would pass con s ti tuti onal revi ew; s ee
L awren ce Le s s i g, " Re ading the Con s ti tuti on in Cybers p ace ," Em o ry Law Jou rn a l 45 (1996): 8 6 9 ,
8 8 3 – 9 5 ;L awren ce Le s s i g, "The Zones of Cybers p ace ," St a n fo rd Law Revi ew 48 (1996): 1 4 0 3 .

10. In some contexts we call a network architecture that solves some o f these "imperfections"—that builds in these elements of control—an intranet. Intranets are the fastest-growing porti on of the In tern et tod ay. Th ey are a stra n ge hybrid of t wo trad i ti ons in net work
computing—the open system of the Internet, based on TCP/IP, and the control-based capability of traditional proprietary networks layered onto the Internet. Intranets mix values from
each to produce a network that is interoperable but gives its controller more control over ac -
cess than anyone would have over the Internet. My argument in this book is that an "internet"
with con trol is what our In tern et is becom i n g. According to the reporter Steve Lo h r
("Netscape Taking on Lotus with New Corporate System," New York Times, October 16,1996,
D2),"Netscape executives pointed to studies projecting that the int intranet market will grow to
$10 billion by 2000." Lohr had also reported ("Internet Future at IBM Looks Oddly Familiar,"
New York Times, September 2,1996,37) that "investment in the United States in intranet software for servers,the powerful computers that store network data, would increase to $6.1 billion by 2000 from $400 million this year. By contrast, Internet server software investment is
projected to rise to $2.2 billion by 2000 from $550 million."

C H A P T E R F O U R

1 . Th o u gh I do think it is nece s s a ri ly the case that how com m erce is arch i tected affects fund a m ental va lu e s . In this, I agree with David Ch a u m , who argued early on that paym ent sys tem s
would be crucial for "ach i eving el ectronic privac y " ;s ee , for ex a m p l e , "Ach i eving Electronic Privac y," S ci en ce ( August 1992): 9 6 , 9 6 – 9 7 , ava i l a ble at http : / / ga n ge s . c s . tcd . i e / m epei rce / Proj ect /
Ch a u m / s c i a m . h tml (vi s i ted May 30, 1 9 9 9 ) . Paym ent sys tems are cru c i a l , and they can be crucially i a lly differen t .

2 4 5

2. As in United States v O'Brien, 391 US 367 (1968), in which the Court upheld a statute
that made burning a draft card a crime. The state interest was in preserving a usable credential.

3. See Ed Krol, The Whole Internet: User's Guided Catalogue (Sebastopol, Calif.: O'Reilly &
As s oc i a te s , 1 9 9 2 ) , 2 3 – 2 5 ; Lo s h i n , TCP/IP Clearly Expl a i n ed , 3 – 8 3 ; Hu n t , TC P / I P, 1 – 2 2 ; s ee
also Ben M. Sega l , "A Short Hi s tory of In tern et Pro tocols at CERN," ava i l a ble at
http://wwwinfo.cern.ch/pdp/ns/ben/TCPHIST.html (visited May 30,1999).

4. See Jerome H. Saltzer et al.,"End-to-End Arguments in System Design," in Integrated
B roa d band Netwo rk s , ed i ted by Amit Bh a r gava (New York : E l s evi er Scien ce Pu blishing Co. ,
1991),30.

5. By "layering" I don't mean that such architectures would change the basic TCP/IP protocol suite. The changes I am describing here are within the application space—not the application layer—of Internet applications.I define "application space" in chapter 8.

6 . Th ere is also the disadva n t a ge of s ec u ring the password , e s pec i a lly if the password is

transmitted as plain text.I am simplifying brutally in my consideration of that issue here.

7 . For a de s c ri pti on of the privacy and sec u ri ty threats po s ed by cookies ("e s s en ti a lly non exi s ten t" ) ,s ee U. S . Dep a rtm ent of E n er gy, "Com p uter In c i dent Advi s ory Ca p a bi l i ty," In fo rm a ti o n
B u ll eti n , I–034: In tern et Cook i e s , ava i l a ble at http : / / w w w. c i ac . or g / c i ac / bu ll eti n s / i – 0 3 4 . s h tm l
( vi s i ted May 30, 1 9 9 9 ) ; s ee also Ca rl W. Ch a m berl i n , "To the Mi ll en n iu m : E m er ging Is sues for
the Year 2000 and Cybers p ace ," Notre Dame Jou rnal of Law, Et h i cs , and Pu blic Pol i c y 1 3 ( 1 9 9 9 ) :
1 3 1 ,1 7 3 ;" Devel opm ents in the Law — The Law of Cybers p ace :I V. In tern et Reg u l a ti on Th ro u gh
Arch i tectu ral Mod i fic a ti on : The Property Rule Stru ctu re of Code So luti on s ," Ha rva rd Law Re -
vi ew 112 (1999): 1 6 3 4 , 1 6 4 4 , n . 5 7 ; Neil Ra n d a ll , " How Cookies Work ," PC Ma Magazine On l i n e ,
ava i l a ble at http : / / w w w. zd n et . com / pc m a g / fe a tu re s / coo k i e / ck s 1 . h tm (vi s i ted May 30, 1 9 9 9 ) .

8 . Any sec u ri ty probl em comes not from the cookies direct ly (since they are simply passive
data) but from app l ets (small er app l i c a ti ons) that might misuse the data co ll ected .D avid Wi ll e ,
in " Pers onal Ju ri s d i cti on and the In tern et : Propo s ed Limits on State Ju ri s d i cti on over Data
Com mu n i c a ti ons in Tort Ca s e s" (Ken tu cky Law Jou rn a l 87 [1999]: 9 5 ,1 9 8 – 9 9 ) , de s c ri bes the sec u ri ty dangers with coo k i e s . For a second de s c ri pti on of the po s s i ble risks from coo k i e s , s ee
Jerry Ka n g, " In form a ti on Privacy in Cybers p ace Tra n s acti on s ," St a n fo rd Law Revi ew 50 (1998):
1 1 9 3 ,1 2 2 7 – 2 9 .

9 . S tew a rt A . Ba ker and Paul R. Hu rs t , The Limits of Trust: Crypto gra p hy, Govern m en t s ,

and Electronic Commerce (Boston: Kluwer Law International,1998),xv.

10. Ibid.
11. See Hal Abelson et al., "The Risks of Key Recovery, Key Escrow, and Trusted Third-
Party Encryption," World Wide Web Journal 2 (1997): 241, 245: "Although cryptography has
traditionally been associated with confidentiality, other cr cryptographic mechanisms, such as
authentication codes and digital signatures,can assure that messages have not been tampered
with or forged."

1 2 . Wh i tf i eld Diffie and Ma Martin E. Hell m a n ," New Di recti ons in Cryptogra phy," I E E E
Tra n s a ctions on In fo rm a tion T h e o ry I T– 2 2 ( Novem ber 1976): 6 4 4 – 5 4 . The idea had app a ren t ly been discovered earl i er by James Ellis at the Bri British Govern m ent Com mu n i c a ti on
He ad qu a quarters , but it was not then publ i s h ed ; s ee Ba ker and Hu rs t , The Limits of Tru s t ,
x vi i .

13. A symmetric key algorithm is an encryption routine that requires the same key to encrypt and decrypt a message. An asymmetric key algorithm is one that uses a diff erent key to
encrypt and decrypt.

14. There are other issues as well;see Bruce Schneier, Applied Cryptography: Protocols, Al -
algorithms,and Source Code in C, 2d ed.(New York: Wiley, 1996),4–5; Conference, "The Development and Practice of Law in the Age of the Internet," American University Law Review 46
(1996): 327.

2 4 6

15. For a comprehensive analysis of the legal issues surrounding PKI,see "Public Key Infrastructure Symposium," Jurimetrics Journal 38 (1998): 241.

1 6 . " Di gital ID Cen ter," ava i l a ble at http : / / w w w. veri s i gn . com / produ ct s / i n d ivi du a l / i index.html (visited May 30,1999).

17. As Baker and Hurst point out, certifications supporting the secure electronic transaction (SET) protocol are not identity certificates; The Limits of Trust, 252–53.

1 8 . See A . Mi ch ael Froom k i n ," F l ood Con trol on the In form a ti on Oce a n : L iving wi t h
Anonymity, Digital Cash,and Distributed Databases," Journal of Law and Communication 15
(1996): 395,505.

19. See Gail L. Grant, Understanding Digital Signatures: Establishing Trust over the Internet

and Other Networks (New York: McGraw-Hill,1998),5.

20. Jane Kaufman Winn, "Open Systems, Free Markets,and Regulation of Internet Commerce," Tulane Law Review 72 (1998): 1177,1238.

2 1 . O n ce aga i n , of co u rs e , even that idea is not new. Tel eph ones have been used to sell
things since the birth of phones; they too are an open and insecure network. The same was
true of telegraphs before them; see Tom Standage, The Victorian Internet (New York: Walker
& Co.,1998).

22. See Mark A. Lemley and David McGowan,"Legal Implications of Network Economic

Effects," California Law Review 86 (1998): 479,484, 552–53.

23. See Richard E. Smith, Internet Cryptography (Reading, Mass.: Addison-Wesley, 1997),

218–28.

2 4 . Winn ("Open Sys tem s ," 1210) reports that the SET "pro tocol devel oped by Visa and Ma ster Ca rd [is] curren t ly being marketed . . . as a sec u re In tern et app l i c a ti on for any type of bank or
c redit card ." See also the introdu cti on to the con cept of "s ec u re el ectronic com m erce" on the Vi s a
web site at http : / / w w w. vi s a . com / c gi - bi n / vee / n t / ecom m / m a i n . h tml (vi s i ted May 30, 1 9 9 9 ) .

25. See Winn, "Open Systems," 1210–11.
26. See C. Bradford Biddle,"Legislating Market Winners: Digital Signature Laws and the

Electronic Commerce Marketplace," San Diego Law Review 34 (1997): 1225,1242,n.37.

27. See Grant, Understanding Digital Signatures, 14;see also Smith, Internet Cryptography,

295–319.

28. See Richard L.Field,"1996: Survey of the Year's Developments in Electronic Cash Law
and the Laws Affecting Electronic Banking in the United States," American University Law Re -
view 46 (1997): 967, 988 (discussing a federal PKI steering committee to "coordinate efforts
by exec utive agencies to use public key digital sign a tu re tech n o l ogy " ) ; s ee also Ba ker and
Hurst, The Limits of Trust, 275–83.

2 9 . See Donna N. L a m pert et al., "Overvi ew of In tern et Legal and Reg u l a tory Is su e s ,"
Pra cti cing Law In s ti tu te / Pa ten t s , Copyri gh t s , Tra d em a rk s , and Li tera ry Property 544 (1998):
179,220; see also Grant, Understanding Digital Signatures, 66–93.

3 0 . In the Un i ted States mandated IDs are ex trem ely ra re . It was not until the late 1950s that
c i ti zens retu rning from abroad were requ i red to carry a passport ;s ee David Bri n , The Tra n s pa r -
ent Soci ety: Wi ll Te ch n ol o gy Fo rce Us to Choo se Betwe en Privacy and Fre ed o m ? ( Ca m bri d ge ,
Ma s s . : Pers eus Boo k s ,1 9 9 8 ) ,6 8 .

31. There are many digital certificate vendors serving as certificate authorities. The more
well - k n own inclu de Veri Si gn (www. veri s i gn . com ) , Th awte (www. t h awte . com ) , G T E's Cyber Trust (www. c cybertrust s t . g te . com ) , E n trust (www. en tru s t . com ) , Fron ti er Tech n o l ogi e s
( w w w. f ron ti frontiertech . com ) , and Xcert (www. xcert . com ) . Some are tailored to a particular industry, such as TradeWave (www.tradewave.com),and some are region-specific, such as Key-
Wi tness (www. key wi tness.ca) in Ca n ada and Bel Si gn In tern a ti onal (www. bel s i gn . be) in
Europe. Network Solutions has teamed up with VeriSign so that anyone who registers his or
her domain name has an option to obtain a digital server certificate from VeriSign; see "Our

2 4 7

Partners," available at http://www.netsol.com/partners/ (visited May 30,1999). For a more exh a u s tive list of certi f i c a te aut h ori ti e s , s ee "The PKI Pa ge ," ava i l a ble at http : / / w w w.
pca.dfn.de/eng/team/ske/pem-dok (visited May 30,1999).

C H A P T E R 5

1. See generally Trust in Cyberspace, edited by Fred B. Schneider (Washington, D.C.: National Academy Press, 1999),27–29.

2. See Katie Hafner and Matthew Lyon, Where Wizards Stay Up Late: The Origins of the In -

ternet (New York: Simon & Schuster, 1996),62–63.

3 . Com mu n i c a ti ons As s i s t a n ce for Law Enforcem ent Act , Pu blic Law 103–414, 108 Stat

4279,47 USC § 1001 et seq., and in scattered sections of 18 USC.

4. See Richard A. Posner, "The Cost of Rights: Implications for Central and Eastern Europe—and for the United States," Tulsa Law Journal 32 (1996): 1, 7–9; cf. William J. Stuntz,
"The Uneasy Relationship Between Criminal Procedure and Criminal Justice," Yale Law Jour -
nal 107 (1997): 1,4.

5 . "Wi t h o ut su ch limits, the govern m en t's natu ral incen tive is to evade or ex p l oit the procedu ral civi l - c riminal line by ch a n ging the su b s t a n tive civi l - c riminal line" ; S tu n t z 's poi n t , m ade
e a rl i er, is abo ut overcriminalization ri m i n a l i z a ti on , not incre a s ed punishmen t s ; s ee Wi lliam J. S tu n t z , "Su bs t a n ce , Proce s s , and the Civi l - Criminal Line," Jou rnal of Co n tem po ra ry Legal Is su e s 7 (1996): 1 .
6 . From an econ omic pers pective , this kind of reg u l a ti on makes sense if it is the ch e a pe s t
means to a social en d . Obvi o u s ly, i f the govern m ent simply mandated this ch a n ge in arch i tectu re , it would be inex pen s ive for the govern m en t . What is intere s ting abo ut the act is its mand a te that the govern m ent pay for the ch a n ge in arch i tectu re . The govern m ent is thu s
i n internalizing the costs of ch a n ge , and we might think abo ut this as a useful tech n i que to en su re
that social va lue is incre a s ed by this type of reg u l a tory tech n i qu e . Put another way: the governm ent is "t a k i n g" the reg u l a tory power of the tel eph one net work's code , and as is gen era lly tru e
with takings , it might make sense to requ i re that this taking be funded by the govern m en t .

7 . As of this wri ti n g, the proposals are sti ll being revi reviewed ; s ee John Ha n ch et te , " ' Bi g
Bro t h er ' G oing Too Fa r ? : Privacy Ri ghts Erod i n g, Cri tics Say," F l o rida Tod ay, Febru a ry 15,
1999,10A, available at 1999 WL 7000142.

8 . See Cen ter for Dem oc racy and Tech n o l ogy, "FBI Seeks to Im pose Su rvei ll a n ce Ma nd a tes on Tel eph one Sys tem ; Ba l a n ced Obj ectives of 1994 Law Fru s tra ted : S t a tus Report ,"
March 4,1999, available at http://www.cdt.org/digi_tele/status.html (visited May 30,1999).

9 . For a good de s c ri pti on of the Audio Home Recording Act of 1 9 9 2 , s ee Ch ri s tine C.
Carlisle,"Recent Development: The Audio Home Recording Act of 1992," Journal of Intellec -
tual Property Law 1 (1994):335,336–38. For an analysis of the act and its effect on copyright,
s ee Joel L. Mc Ku i n , " Home Audio Taping of Copyri gh ted Works and the Audio Hom e
Recording Act of 1992:A Critical Analysis," Hastings Communications and Entertainment Law
Journal 16 (1994):311.

1 0 . See Audio Home Recording Act , 17 USC § 1002 (1994) (requ i ring the serial copy
m a n a gem ent sys tem ) ; s ee also U. S . Dep a rtm ent of Com m erce , In tell e ctual Property and the
Na tional In fo rm a tion In f ra s tru ctu re: Repo rt of the Wo rking Group on In tell e ctual Property
Rights (Washington, D.C.: Information Infrastructure Task Force,1995), 179,189–90.

11. See 47 CFR § 15.120;see also Telecommunications Act of 1996 Pub.L.104–104,§ 551,
110 Stat. 56, 139–42 (1996), 47 USC § 303 (1998) (providing for study and implementation
of video blocking devices and rating systems).

1 2 . For a revi ew of the evi den ce con s i dered , s ee U. S . Sen a te Com m i t tee on Com m erce ,
Subcommittee on Communications, Hearings on Violence on Television, 93d C ong., 2d sess.

2 4 8

(1974); U.S. Senate Committee on Commerce, Subcommittee on Communications, Hearings
in Review of Policy Matters of Federal Communications Commission and Inquiry into Crime and
Vi ol en ce on Tel evision and a Propo sed Stu dy T h ere of by the Su rgeon Gen era l , 91st Con g. , 1 s t
s e s s . , pt . 2 (1969); s ee also Su r geon Gen era l 's Scien ti fic Advi s ory Com m i t tee on Tel evi s i on
and Social Behavior, Television and Growing Up: The Impact of Televised Violence: Report to the
Su rgeon Gen era l (Wa s h i n g ton , D. C . : U. S . G overn m ent Pri n ting Office , 1 9 7 2 ) ; Ma t t h ew L.
S p i t zer, S even Di rty Wo rds and Six Other Sto ri e s ( New Haven , Con n . : Yale Un ivers i ty Pre s s ,
1986), 95–118; Television and Social Behavior: Media Content and Cont rol, edited by George
Comstock and Eli A. Rubinstein (1972); George Comstock, "Television and American Social
Institutions," in Children and Television, 3d ed., edited by John C. Wright and Aletha C. Huston (1983),27;George Comstock, "Violence in Television Content: An Overview," in National
Institute of Mental Health: Television and Behavior: Scientific Progress and Implications for the
Eighties: Technical Reviews 2 (1982),110; Harry T. Edwards and Mitchell N. Berman,"Regulating Violence on Television," Northwestern University Law Review 89 (1995): 1487,1535; E.
Barrett Prettyman Jr. and Lisa A. Hook, "The Control Of Media-Related Imitative Violence,"
Federal Communications Law Journal 38 (1987):317.

13. See Red Lion Broadcasting Company v Federal Communications Commission, 395 US
367 (1969) (ruling that the FCC's orders requiring radio stations to provide time for response
to personal attack do not violate the First Amendment); see also Turner Broadcasting System,
Inc., v Federal Communications Commission, 512 US 622,637–38 (1994). But see Denver Area
Educational Telecommunications Consortium, Inc.v Federal Communications Commission, 518
US 727 (1996) (ruling that provisions permitting cable operator to filter content on leased access channels are consistent with First Amendment, but that similar provisions with regard to
public access channels are not).

14. Increasingly the opinion is that the rationale behind Red Lion (scarcity of spectrum
justifies certain regulation) is no longer valid;see Roxana Wizorek, "Children's Television: The
FCC's Attempt to Educate America's Children May Force the Supreme Court to Reconsider
the Red Lion Rationale," Catholic University Law Review 47 (1997): 153, 182–86; but see Laurence H. Winer, "The Red Lion of Cable, and Beyond?–Turner Broadcasting v FCC," Cardozo
Arts and En tert a i n m ent Law Jou rn a l 15 (1997): 1 , 21–25 (arguing Tu rn er m ay revive ga tekeeper aspect of Red Lion).

1 5 . The con s equ en ce of an ef fic i ent v-chip on most tel evi s i ons would be the rem oval of t h e
s t a n d a rd ju s ti fic a ti on for reg u l a ting con tent on broadc a s ti n g. If u s ers can sel f - fil ter, t h en the
FCC need not do it for them ;s ee Peter Hu ber, Law and Di so rd er in Cy bers pa ce: Ab olish the FCC
and Let Common Law Rule the Tel e co s m ( New York : Ox ford Un ivers i ty Pre s s ,1 9 9 7 ) ,1 7 2 – 7 3 .

1 6 . For a good discussion of the Cl i pper con trovers y, s ee Laura J. Gu ra k , Persuasion and Pri -
vacy in Cy bers pa ce: The Online Protests over Lotus Ma rketpl a ce and the Clipper Chip ( New Haven ,
Con n . : Yale Un ivers i ty Pre s s ,1 9 9 7 ) ,3 2 – 4 3 . For a sample of va rious vi ews ,s ee Ki rs ten Sch eu rer,
"The Cl i pper Ch i p : Cryptogra phy Tech n o l ogy and the Con s ti tuti on ," Ru t gers Co m pu ter and
Te ch n ol o gy Law Jou rn a l 21 (1995): 2 6 3 ;c f . How a rd S. D a kof f , "The Cl i pper Chip Propo s a l : Dec iph ering the Un fo u n ded Fe a rs That Are Wron gf u lly Derailing Its Im p l em en t a ti on ," John Ma rs h a ll
Law Revi ew 29 (1996): 4 7 5 . "Cl i pper was adopted as a federal inform a ti on - processing standard
for voi ce com mu n i c a ti on" in 1994; s ee Gu ra k , Persuasion And Privacy in Cy bers pa ce , 1 2 5 .

1 7 . See Electronic Fron ti er Fo u n d a ti on (EFF), Cra cking DES: Secrets of En cryption Re se a rch ,
Wi retap Pol i ti cs , and Chip De s i gn ( Seb a s topo l , Ca l i f . :E l ectronic Fron ti er Fo u n d a ti on ,1 9 9 8 ) , ch .1 .
18. For a good summary of the Clipper scheme,see Baker and Hurst, The Limits of Trust,
15–18;A. Michael Froomkin, "The Metaphor Is the Key: Cryptography, the Clipper Chip, and
the Constitution," University of Pennsylvania Law Review 143 (1995):709,752–59. For a more
technical discussion , s ee Bru ce Sch n ei er, Appl i ed Crypto gra p hy: Proto col s , Al go ri t h m s , a n d
Source Code in C, 2d ed.(New York: Wiley, 1996): 591–93.

2 4 9

19. See Field,"1996: Survey of the Year's Developments in Electronic Cash Law . . . ," 967,

993,n.192.

2 0 . See A . Mi ch ael Froom k i n , " It Came from Planet Cl i pper: The Battle over Cryptographic Key 'Escrow,'" University of Chicago Legal Forum 1996 (1996): 15,32.

21. This was the purpose of the proposed Oxley-Manton Amendment to the Security and
Freedom Through Encryption (SAFE) Act of 1997,NR 695,105th Cong., 1st sess. Baker and
Hurst (The Limits of Trust, 21–22) note that "1997 saw remarkable change in the nature of the
encryption debate. The beginning of the legislative session saw industry pushing for export
l i bera l i z a ti on and the closing weeks saw indu s try defending against dom e s tic con tro l s ." In
1996 the government implemented a policy to allow firms to export encryption technologies
using the government's DES (digital encryption standard) so long as a key recovery system is
built in; see EFF, Cracking DES, 1–4–1–5. As EFF's "Cracking DES" project makes clear, however, DES is an unreliable encryption standard.There was some hope for the government's enc rypti on policy after the 1996 publ i c a ti on of the Na ti onal Re s e a rch Co u n c i l 's report , t h e
produ ct of a com m i t tee appoi n ted by the NRC to stu dy nati onal cryptogra phy po l i c y. Th e
committee, chaired by Uni versity o f Chicago Law Professor Kenneth Dam, was made up of
m a j or leaders in both the indu s trial and re s e a rch sectors . The report's con clu s i ons were
clear—and damning for the government's anti-encryption policy. The report argued strongly
for liberalization of encryption regulations; see Cryptography's Role in Securing the Informa -
tion Soci ety, ed i ted by Ken n eth W. Dam and Herbert S. Lin (Wa s h i n g ton , D. C . : Na ti on a l
Academy Press,1996). Some believed that the report would have a significant effect, but there
were doubts early on. As Froomkin says ("It Came from Planet Clipper," 69),the battle is far
from over.

22. This is one reading of the decision in Bernstein v U.S. Department of Justice, 176 F3d
1132 (9th Cir 1999). There were dissents from the view of the rights of programmers (Judge
Thomas Nelson:"I am still inevitably led to conclude that encryption source code is more like
conduct than speech"). See also Laura M.Pilkington,"First and Fifth Amendment Challenges
to Export Controls on Encr yption: Bernstein and Karn," Santa Clara Law Review 37 (1996):
159,210; Thinh Nguyen, "Cryptography, Export Controls,and the First Amendment in Bern -
s tein v U. S . Depa rtm ent of Ju s ti ce ," Ha rva rd Jou rnal of Law and Te ch n ol o gy 10 (1997): 6 6 7 ,
6 7 7 – 7 8 ; in "Cryptic Con trovers y: U. S . G overn m ent Re s tri cti ons on Cryptogra phy Ex port s
and the Plight of Philip Zimmermann," Georgia State University Law Review 13 (1997): 581,
603). Ronald J. Stay claims that the right to speak cryptographically is supported as much as
the right to speak Navajo.

23. The idea was suggested in the Clinton administration's 1995 White Paper; see Pamela
Samuelson,"Regulation of Technologies to Protect Copyrighted Works," Communications of
the ACM [Association for Computing Machinery] 39 (1996): 17.

24. Digital Millennium Copyright Act, Public Law 105–304,112 Stat 2860 (1998).
25. Former Attorney General Richard Thornburgh, for example, has called a national ID
card "an infringement on rights of Americans";see Ann Devroy, "Thornburgh Rules Out Two
Gun Control Options; Attorney General Objects to Registration Card f or Gun O wners, Nati onal Iden ti fic a ti on Ca rd ," Wa s h i n g ton Po s t , June 29, 1 9 8 9 , A 4 1 . The Im m i gra ti on Reform
and Control Act of 1986 (Public Law 99–603,100 Stat 3359 [1986],8 USC § 1324a[c] [1988])
eschews it:"Nothing in this section shall be construed to authorize directly or indirectly, the
issuance or use of national identification cards or the establishment of national identification
cards." Given the power of the network to link data,however, this seems to me an empty protection.

26. Notice that this would be an effective end-run around the protections that the Cour t
recogn i zed in Reno v Am erican Civil Li berties Un i o n , 117 SCt 2329 (1997). Th ere are many
"activities" on the Net that Congress could easily regulate (such as gambling). Regulation of

2 5 0

these activities could require IDs before access to these activities would be permitted. To the
extent that such regulation increases the incidence of IDs on the Net,other speech-related access conditions would become easier to justify.

27. Arthur Cordell and T. Ran Ide have proposed the consideration of a bit tax;see Arthur
J. Cordell et al., The New Wealth of Nations: Taxing Cyberspace (Toronto: Between the Lines,
1997). Their arguments are compelling from the perspective of social justice and economics,
but what they do not account for is the architecture that such a taxing system would require.
A Net architected to meter a bit tax could be architected to meter just about anything.

2 8 . Co u n tries with su ch a requ i rem ent inclu de Ar gen ti n a , Au s tra l i a , Bel giu m , Greece ,
Italy, and Switzerland; see Richard L. Hasen,"Law, Economics, and Norms: Voting Without
Law?" University of Pennsylvania Law Review 144 (1996): 2135.
29. See Baker and Hurst, The Limits of Trust, 255–73.
30. See the description in Scott B radner, "The Internet Engineering Task Force," in Open
S ou rces: Vo i ces from the Open Sou rce Revol u ti o n , ed i ted by Ch ris Di Bona et al. ( Seb a s topo l ,
Calif.: O'Reilly & Associates, 1999).

31. Michael Froomkin makes a similar point:"Export control rules have had an effect on
the domestic market for products with cryptographic capabilities such as e-mail, operating
systems, and word processors.Largely because of the ban on export of strong cr yptography,
there is today no strong mass-market standard cryptographic product within the U.S. even
though a considerable mathematical and programming base is fully capable of creating one";
"It Came from Planet Clipper," 19.

3 2 . See " Net work As s oc i a tes and Key Recovery," ava i l a ble at http : / / w w w. n a i . com / products/security/key.asp (visited May 30, 1999).

3 3 . Ci s co has devel oped produ cts that incorpora te the use of n et work - l ayer en c rypti on
through the IP Security (IPSec) protocol. For a b rief discussion of IPSec, see Cisco Systems,
Inc.,"IP Security–IPSec Overview," available at http://www.cisco.com/warp/public/732/Security/ipsec_ov.htm (visited May 30,1999). For a more extensive discussion,see Cisco Systems,
In c . , "Ci s co IOS Sof t w a re Fe a tu re : Net work - L ayer Encrypti on — Wh i te Pa per," ava i l a ble at
h t tp : / / w w w. c i s co. com / w a rp / p u bl i c / cc / c i s co / m k t / s ec u ri ty / en c ryp / tech / en c rp _ wp. h tm (vi si ted May 30, 1 9 9 9 ) ; Ci s co Sys tem s , In c . " I P Sec — Wh i te Pa per," ava i l a ble at http : / / w w w.
c i s co. com / w a rp / p u bl i c / cc / c i s co / m k t / s ec u ri ty / en c ryp / tech / i p s ec _ wp. h tm (vi s i ted May 30,
1999); see also Dawn Bushaus,"Encryption Can Help ISPs Deliver Safe Services," Tele.Com.
March 1, 1997; Beth Davis and Monua Janah, "Cisco Goes End-to-End," Information Week,
February 24,1997,22.

3 4 . See In tern et Arch i tectu ral Boa rd statem ent on "priva te doorbell " en c rypti on , ava i la ble at http : / / w w w. i etf . or g / m a i l - a rch ive / i etf - a n n o u n ce / m sg 0 1 9 3 7 . h tml (vi s i ted May 31,
1 9 9 9 ) .

3 5 . L i t t l e , but not nothing. Th ro u gh con d i ti onal spending gra n t s , the govern m ent was
quite effective initially in increasing Net participation,and it was effective in resisting the development of encryption technologies;see Whitfield Diffie and Susan Eva Landau, Privacy on
the Line: The Pol i ti cs of Wi ret a pping and En crypti o n ( Ca m bri d ge , Ma s s . : MIT Pre s s , 1 9 9 8 ) .
Steven Levy tells of a more direct intervention. When Richard Stallman refused to password protect the MIT AI (artificial intelligence) machine,the Department of Defense threatened to
t a ke the machine of f the Net unless the arch i tectu res were ch a n ged to re s tri ct acce s s . For
Stallman,this was a matter of high principle; for the Department of Defense,it was business
as usual;see Steven Levy, Hackers: Heroes of the Computer Revolution (Garden City, N.Y.: Anchor Press/Doubleday, 1984), 417–18.

3 6 . See Minnesota Statute §§ 609.75, su b d . 2 – 3 , 609.755(1) (1994), making it a misdemeanor to place a bet unless done pursuant to an exempted,state-regulated activity, such as
licensed charitable gambling or the state lottery. Internet gambling organizations are not exempted.

2 5 1

37. See Scott M. Montpas, "Gambling Online: For a Hundred Dollars,I Bet You Government Regulation Will Not Stop the Newest Form of Gambling," University of Dayton Law Re -
view 22 (1996): 163.

3 8 . Or at least it could work like this. Depending on the de s i gn , it could reveal mu ch

more.

3 9 . See 18 USC § 1955 (reg u l a ting bu s i n e s s e s , defining inters t a te " i ll egal ga m bl i n g" a s

gambling that occurs in a state in which it is illegal).

4 0 . See B i o m etri cs: Personal Id en ti f i c a tion in Netwo rked Soci ety, ed i ted by Anil Ja i n ,
Ruud Bo ll e , and Sharath Pa n k a n ti (Bo s ton : Kluwer Ac academic Pu bl i s h ers , 1 9 9 9 ) ; s ee also
Amanda Lang in " Mytec Braced for Lu cen t's Ch a ll en ge ," Fin a n ci a l Post (Toron to ) , May 15,
1 9 9 7 , 6 . At a con feren ce wh ere these tech n o l ogies were de s c ri bed , a participant rec a ll ed a
qu e s ti on he had asked the manu f actu rer of a devi ce that iden ti f i ed people based on thei r
h a n d :" Does it have to be a live hand?" The com p a ny repre s en t a tive tu rn ed wh i te ." No," w a s
the re s pon s e .

41. On virtual private networks, see Smith, Internet Cryptography, chs. 6,7; on biometric
tech n i ques for sec u ri ty, s ee Trust in Cy bers pa ce , ed i ted by Fred B. S ch n ei der (Wa s h i n g ton ,
D.C.: National Academy Press, 1999),123–24,133–34.

42. Roberto Mangabeira Unger, Social Theory: Its Situation and Its Task (New York: Cambridge University Press, 1987).

43. In Bruce Ackerman, Social Justice in the Liberal State (New Haven, Conn.: Yale University Press, 1980), the core analytic device is dialogue: every assertion of power is met with a
demand for justification.

44. Mitchell, City of Bits, 112.
45. Brin, The Transparent Society, 324.

C H A P T E R 6

1. Mike Godwin, CyberRights: Defending Free Speech in the Digital Age (New York: Times
Boo k s , 1 9 9 8 ) , 1 5 . See also Esther Dys on , Rel e a se 2.0: A De s i gn for Living in the Di gital Age
(New York: Broadway Books,1997), who asserts:"Used right, the Internet can be a powerful
enabling technology fostering the development of communities because it supports the very
thing that creates a community—human interaction" (32); see also Stephen Doheny-Farina,
The Wired Neighborhood (New Haven, Conn.: Yale University Press, 1996), 121–37. For a r ecent and important collection examining community in cyberspace, see Marc A. Smith and
Peter Kollock, Communities in Cyberspace (New York: Routledge,1999). The collection ranges
across the social issues of community, including "social order and control," "collective action,"
"community st ructure and dynamics," and "identity." The same relationship between architecture and norms assumed in this chapter guides much of the analysis in Smith and Kollock's
collection.

2 . The newest "com mu n i t a ri a n" on the Net might be bu s i n e s s . A nu m ber of i n flu en ti a l
works have argued that the key to success with online businesses is the development of "virtual com mu n i ti e s" ; s ee , for ex a m p l e , L a rry Downes and Chunka Mu i , Unleashing the Ki ll er
App: Digital Strategies for Market Dominance (Boston: Harvard Business School Press,1998),
101–9; John Hagel and Arthur G. Armstrong, Net Gain: Expanding Markets Through Virtual
Communities (Boston: Harvard Business School Press, 1997).

3. For a detailed study o f Internet demographics, see Matrix Information and Directory
Servi ce s ," In tern et Dem ogra ph i c s : The Th i rd MIDS In tern et Dem ogra phic Su survey " ( M I D S
ids3,October 1995), available at http://www.mids.org/ids3/index.html (visited May 30,1999).
4. For a great sense of how it was, see the articles by Rheingold, Barlow, Bruckman, and
Ramo in part 4 of Richard Holeton, Composing Cyberspace: Identity, Community, and Knowl -

2 5 2

edge in the Electronic Age (Boston: McGraw-Hill, 1998). Howard Rheingold's book (the first
chapter of which is excerpted in Holeton book) is also an early classic; see The Virtual Com -
mu n i ty: Ho m e s homesteading on the Electronic Fro n ti er ( Re ad i n g, Ma s s . : Ad d i s on - We s l ey, 1 9 9 3 ) .
Stacy Horn's book is a brilliant text taken more directly from the interchange (and more) onl i n e ; s ee Cy bervi lle: Click s , Cu l tu re , and the Cre a tion of an Online Town ( New York : Wa rn er
Books,1998).

5. For an excellent description, see Jonathan Zittrain, "The Rise and Fall of Sysopdom,"

Harvard Journal of Law and Technology 10 (1997): 495.

6 . As Steven Jo h n s on puts it: " In theory, these are examples of a rch i tectu re and urb a n
p l a n n i n g, but in practi ce they are bound up in broader issu e s : e ach de s i gn dec i s i on ech oe s
and amplifies a set o f values,an assumption about the larger society that frames it"; Interface
Cu l tu re: How New Te ch n ol o gy Tra n sfo rms the Way We Cre a te and Co m mu n i c a te ( San Fra San Francisco: Harper, 1997),44. See also Nelson Goodman,"How Buildings Mean," in Reconceptions
in Philosophy and Other Arts and Sciences, edited by Nelson Goodman and Catherine Z.Elgin
(London: Routledge,1988),31–48.

7 . C f . G odwi n , Cy ber Ri gh t s : " If yo u're face - to - f ace with som eon e , yo u're ex po s ed to
countless things over which the other person may have had no conscious control—hair color,
say, or facial expressions. But when you're reading someone's posted ASCII message, every -
thing you see is a product of that person's mind" (42,italics in original);see also ibid.,44.

8. See Martha Minow, Making All the Diff erence: Inclusion, Exclusion, and American Law

(Ithaca,N.Y.: Cornell University Press,1990), 74–97.

9. See Laura J. Gurak, Persuasion and Privacy in Cyberspace: The Online Protests over Lotus,
Marketplace,and the Clipper Chip (New Haven, Conn.: Yale University Press,1997),4–15. Gurak notes that "pseudonyms, for example,can be used to mask the name of a speaker, so that
often it is the ethos of the texts, not the character of the speaker, that does or does not convi n ce others ." C f . Lori Ken d a ll , " M U D der? I Ha hardly Kn ow 'Er!: Adven tu res of a Fem i n i s t
MUDder," in Wired Women: Gender and New Realities in Cyberspace, edited by Lynn Cherny
and Elizabeth Reba Weise (Seattle: Seal Press, 1996),207.Godwin describes another possibility, as the ASCII channel on the Net shuts down: "Then, perhaps, the world of ASCII communications will become a preserve for the edgy exchanges of tense text maniacs. Like me";
CyberRights, 45.

1 0 . This is what econ omists would call a "s ep a ra ting equ i l i briu m" : "p l ayers of d i f feren t
types adopt different s tra strategies e s and thereby all ow an uninform ed player to draw inferences ce s
a bo ut an inform ed player 's type from that player 's acti on s" ; Do u glas G. Ba i rd , Robert H. G ertn er, and Randal C. P i cker, Game T h e o ry and the Law ( Ca m bri d ge , Ma s s . : Ha rva rd Un ivers i ty
Pre s s ,1 9 9 4 ) ,3 1 4 . Wi lliam Mi tch ell argues that the adva n ce back to synch ronous com mu n i c ati on is not nece s s a ri ly an adva n t a ge : "As mu ch more ef fic i ent asynch ronous com mu n i c a ti on s
s ys tems have become com m on p l ace , t h o u gh , we have seen that stri ct synch rony is not alw ays
de s i ra bl e ; con tro ll ed asynch rony may have its adva n t a ge s" ; Ci ty of B i t s , 5 – 1 6 .

11. On making the Web accessible,see Judy Brewer and Daniel Dardailler, "Web Accessibility Initiative (WAI)," available at http://www.w3.org/WAI (visited May 30,1999);cf."Note:
Facial Discrimination: Extending Handicap Law to Employment Discrimination on the Basis
of Physical Appearance," Harvard Law Review 100 (1987):2035.

12. See AOL, "About the Company: Profile," available at http://www.aol.com/corp/profile/

(visited May 30,1999).

13. See Kara Swisher, Aol.com: How S teve Case Beat Bill Gates, Nailed the Netheads, and

Made Millions in the War for the Web (New York: Times Business,1998),65.

14. As stated in AOL's Terms of Service (TOS): "As an AOL member you are required to
follow our TOS no matter where you are on the Internet." Some of the other terms of service
include the following rules:"Language: Mild expletives and nonsexual anatomical references
are allowed, but strong vulgar language,crude or explicit sexual references, hate speech, etc.,

2 5 3

are not. If you see it, report it at Keyword: Notify AOL.Nudity: Photos containing revealing
attire or limited nudity in a scientific or artistic context are okay in some places (not all). Partial or full frontal nudity is not okay. If you see it, report it at Keyword: Notify AOL.Sex/Sensu a l i ty: Th ere is a differen ce bet ween affection on and vu l ga ri ty. Th ere is also a differen ce
between a discussion of the health or emotional aspects of sex using appropriate language,
and more crude conversations about sex. The former is acceptable, the latter is not. For example, in a discussion about forms of cancer, the words breast or testicular would be acceptable, but slang versions of those words would not be acceptable anywhere."Violence and Drug
Abuse: Graphic images of humans being killed, such as in ne ws accounts,may be acceptable
in some areas, but blood and gore, gratuitous violence, etc., are not acceptable. Discussions
about coping with drug abuse in health areas are okay, but discussions about or depictions of
illegal drug abuse that imply it is acceptable are not."

15. See Amy Harmon, "Worries About Big Brother at America Online," New York Times,

January 31,1999,1.

16. Swisher, Aol.com, 314–15.
17. Ibid., 96–97.
1 8 . See Robert C. Po s t , Co n s ti tu tional Domains: Dem o cra c y, Co m mu n i ty, Ma n a gem en t

(Cambridge, Mass.: Harvard University Press,1995), 199–267.

19. See Cyber Promotions, Inc. v America Online, Inc., 948 FSupp 436 (EDPa 1996) (holding that a company has no free speech right under the United States, Pennsylvania, or Virginia
Constitutions to send unsolicited e-mail over the Internet to a competitor's customers).

2 0 . See Elizabeth Rei d ," Hi era rchy and Power: Social Con trol in Cybers p ace ," in Co m mu n i -

ties in Cy bers pa ce , ed i ted by Ma rc A . Smith and Peter Ko ll ock (Lon don : Ro ut l ed ge ,1 9 9 9 ) ,1 0 9 .
2 1 . See Josh Quittner er, " Jo h n ny Manhattan Meets the Fu rry Mu ckers ," Wi red ( Ma rch 1994):

9 2 , ava i l a ble at http : / / w w w. wi red . com / wi red / a rch ive / 2 . 0 3 / mu d s . h tml (vi s i ted May 30, 1 9 9 9 ) .

22. See Julian Dib bell, "A Rape in Cyberspace," Village Voice, December 23, 1993, 36, 37,

available at http://www.levity.com/julian/bungle_vv.html (visited May 30,1999).

23. Ibid.
24. In particular, see Dibbell's extraordinary My Tiny Life: Crime and Passion in a Virtual

World (London: Fourth Estate, 1998).

25. Ibid.,13–14.
26. If anything, the sexuality of the space invited adolescent responses by adolescents; see
S cott Bu k a tm a n , Terminal Id en ti ty: The Vi rtual Su bje ct in Po s tm od ern Sci en ce Ficti o n
(Durham,N.C.: Duke University Press, 1993), 326. On MOOs in particular, see Dibbell, My
Tiny Life. The challenge for the community was to construct norms that would avoid these responses without destroying the essential flavor of the space.

27. Dibbell, My Tiny Life, 24–25.
28. See Haakon (Pavel Curtis),"Petition System Implemented and in Force," message 773
on *soc i a l - i s sues (#7233), L a m b d a M OO Bu ll etin Boa rd , May 1, 1 9 9 3 , ava i l a ble at
h t tp : / / ve s t a . phys i c s . u cl a . edu / ~ s m o l i n / l a m b d a / l aws _ a n d _ h i s tory / b a ll o t h i s tory (vi s i ted May
30,1999).

29. See Haakon (Pavel Curtis),"How to Make a Vote Binding on the Wizards" (first draft),
message 511 on *social-issues (#7233), LambdaMOO Bulletin Board, April 8, 1993, available
at http://vesta.physics.ucla.edu/~smolin/lambda/laws_and_history/ballothistory (visited May
30,1999).

30. For a rich account of both the democracy and how it func tions,and the implications
for self-regulation with a MUD, see Jennifer Mnookin, "Virtual(ly) Law: The Emergence of
Law on LambdaMOO," Journal of Computer-Mediated Communication 2 (1996): 1.

31. Hafner and Lyon, Where Wizards Stay Up Late, 216."Flaming" is e-mail or other electronic communication that expresses exaggerated hostility; see Gurak, Persuasion and Privacy
in Cyberspace, 88.

2 5 4

32. Mnookin, "Virtual(ly) Law," 14.
33. One student of mine studied this behavior and concluded that the difference was significant. That study was limited,however, by a relatively small sample.On the question more
gen era lly, Gu rak re aches a different con clu s i on abo ut wh et h er cybers p ace rem remedies gen der
imbalances; Persuasion and Privacy in Cyberspace, 104–13.

3 4 . Mi ke Godwin makes a similar point abo ut the con s tru cti on of a ny vi rtual com munity: "What most of us will want in the future, I think,is a place where we're known and accepted on the basis of what Martin Luther King Jr. called 'the content of our character.' But
without planning, without a deliberate architectural vision about shaping virtual communities—and, most of all, without true freedom of speech—the incoming hordes of cyberspace
inhabitants will continue to be alienated, isolated, without any sense of belonging. Virtually
homeless"; CyberRights, 41.

C H A P T E R S E V E N

1. Or more precisely, against a certain form of government regulation. The more powerful libertarian arguments against regulation in cy berspace are a dvanced, for example, by Peter Huber in Law and Disorder in Cyberspace: Abolish the FCC and Let Common Law Rule the
Telecosm. Huber argues against agency regulation and in favor of regulation by the c ommon
law. See also Thomas Hazlett in "The Rationality of U.S. Regulation of the Broadcast Spectrum," Journal of Law and Economics 33 (1990):133,133–39. For a lawyer, it is hard to understand precisely what is meant by "the common law." The rules of the common law are many,
and the substantive content has changed. There is a c ommon law process, which lawyers like
to mythologize,in which judges make policy decisions in small spaces against the background
of binding precedent. It might be this that Huber has in mind, and if so, there are, of course,
benefits to this system. But as he plainly understands, it is a form of regulation even if it is
constituted differently.

2 . The pri m a ry examples are the convi cti ons under the 1917 Espionage a ge Act ; s ee , for ex a mp l e , S ch en ck v Un i ted St a te s , 249 US 47 (1919) (upholding convi cti on for distri buting a leaflet
a t t attacking World War I con s c ri pti on ) ; Frohwerk v Un i ted St a te s , 249 US 204 (1919) (uph o l d i n g
convi cti on based on news p a per all eged to cause disloya l ty ) ; Debs v Un i ted St a te s , 249 US 211
(1919) (convi cti on uph eld for po l i tical speech said to cause insu bord i n a ti on and disloya l ty ) .

3 . See , for ex a m p l e , the work of John R. Com m on s , Legal Fou n d a tions of C a p i t a l i s m
(1924), 296–98, discussed in Herbert Hovenkamp, Enterprise and American Law, 1836–1937
(Cambridge, Mass.: Harvard University Press,1991),235;see also John R. Commons, Institu -
tional Economics: Its Place in Political Economy (1934).

4. The general idea is that the tiny corrections of space enforce a discipline, and that this
discipline is an important reg u l a ti on . Su ch theorizing is a ti ny part of the work of Mi ch el
Foucault; see Discipline and Punish: The Birth of the Prison (1979),170–77, though his work
generally inspires this p erspective. It is what Oscar Gandy speaks about in The Panoptic Sort:
A Political Economy of Personal Information (Boulder, Colo.: Westview Press,1993),23.David
Brin makes the more general point that I am arguing—that the threat to liberty is broader
than a threat by the state; see The Transparent Society, 110.

5. See, for example, The Built Environment: A Creative Inquiry into Design and Planning,
edited by Tom J. Bartuska and Gerald L. Young (Menlo Park, Calif.: Crisp Publications,1994);
Pre serving the Built Heri t a ge: Tools for Im pl em en t a ti o n , ed i ted by J. Ma rk Schu s ter et al.
(Hanover, N.H.: University Press of New England, 1997). In design theory, the notion I am
describing accords with the tradition of Andres Duany and Elizabeth Plater-Zyberk; see, for
example, William Lennertz, "Town-Making Fundamentals," in Towns and Town-Making Prin -
ciples, edited by Andres Duany and Elizabeth Plater-Zyberk (New York: Rizzoli, 1991): "The

2 5 5

work of . . . Duany and . . . Plater-Zyberk begins with the recognition that design affects behavior. [They] see the structure and function of a community as interdependent. Because of
this,they believe a designer's decisions will permeate the lives of residents not just visually but
in the way re s i dents live . Th ey bel i eve de s i gn stru ctu res functi onal rel a ti on s h i p s , qu a n ti t atively and qualitatively, and that it is a sophisticated tool whose power exceeds its cosmetic attributes" (21).

6 . E l s ewh ere I've call ed this the " New Ch i c a go Sch oo l " ; s ee Lawren ce Le s s i g, "The New
Chicago School," Journal of Legal Studies 27 (1998): 661. It is within the "tools approach" to
govern m ent acti on (see John de Mon chaux and J. Ma rk Schu s ter, " F ive Th i n gs to Do," i n
S chu s ter, Pre serving the Built Heri t a ge , 3 ) , but it de s c ri bes four tools wh ereas Schu s ter describes five.I develop the understanding of the approach in the appendix to this book.

7. See generally Smoking Policy: Law, Politics, and Culture, edited by Robert L. Rabin and
Stephen D. Sugarman (New York: Oxford University Press,1993);Lawrence Lessig, "The Regulation of Social Meaning," University of Chicago Law Review 62 (1995):943,1025–34; Cass R.
Sunstein, "Social Norms and Social Roles," Columbia Law Review 96 (1996): 903.

8. These technologies are themselves affected, no doubt, by the market. Obviously, these
con s traints could not exist indepen den t ly of e ach other but affect each other in sign i fic a n t
ways.

9. The ACLU lists twelve states that passed Internet regulations between 1995 and 1997;

see http://www.aclu.org/issues/cyber/censor/stbills.html#bills (visited May 31,1999).

10. See, for example, the policy of the Minnesota attorney general on the jurisdiction of
Minnesota over people tra n s m i t ting ga m bling inform a ti on into the state ; ava i l a ble at
h t tp : / / w w w. a g. s t a te . m n . u s / h om e / con su m er / con su m ern ews / O n l i n e S c a m s / m em o. h tml (vi sited May 31, 1999).

11. See, for example, Playboy Enterprises v Chuckle berry Publishing, Inc., 939 FSupp 1032
(SDNY 1996); United States v Thomas, 74 F3d 1153 (6th Cir 1996); United States v Miller, 166
F3d 1153 (11th Cir 1999); United States v Lorge, 166 F3d 516 (2d Cir 1999); United States v
W h i ti n g , 165 F3d 631 (8th Cir 1999); Un i ted St a tes v Hi bbl er, 159 F3d 233 (6th Cir 1998);
United States v Fellows, 157 F3d 1197 (9th Cir 1998); United States v Simpson, 152 F3d 1241
(10th Cir 1998); United States v Hall, 142 F3d 988 (7th Cir 1998); United States v Hockings,
129 F3d 1069 (9th Cir 1997); United States v Lacy, 119 F3d 742 (9th Cir 1997); United States v
Smith, 47 MJ 588 (CrimApp 1997); United States v Ownby, 926 FSupp 558 (WDVa 1996).
12. See Julian Dibbell, "A Rape in Cyberspace," Village Voice, December 23,1993,36.
13. See, for example, "AOL Still Suffering but Stock Price Rises," Network Briefing, January
3 1 , 1 9 9 7 ; D avid S. Hi l zen ra t h , " ' Free' E n terpri s e , Online Styl e ; AO L , Com p u Serve , a n d
Prod i gy Settle FTC Com p l a i n t s ," Wa s h i n g ton Po s t , May 2, 1 9 9 7 , G 1 ; "Am erica Online Plans
Bet ter In form a ti on Abo ut Pri ce Ch a n ge s ," Wa ll Stre et Jou rn a l , May 29, 1 9 9 8 , B 2 ; s ee also
Swisher, Aol.com, 206–8.

14. USENET postings can be anonymous; see Henry Spencer and David Lawrence, Man -

aging USENET (Sebastopol, Calif.: O'Reilly & Associates,1998),366–67.

1 5 . Web brows ers make this inform a ti on ava i l a bl e , both in real time and arch ived in a
cookie file; see http://www.cookiecentral.com/faq.htm (visited May 31,1999). They also permit users to turn this tracking feature off.

16. PGP is a program to encrypt messages offered both commercially and free.
1 7 . E n c rypti on , for ex a m p l e , is ill egal in some intern a ti onal con tex t s ; s ee Ba ker and

Hurst, The Limits of Trust, 130–36.
18. Mitchell, City of Bits, 159.
19. See Katsh, "Software Worlds and the First Amendment," 335,340."If a comparison to
the physical world is necessary, one might say that the software designer is the architect, the
builder, and the contractor, as well as the interior decorator."
20. See Rummel v Estelle, 445 US 263,274 n.11 (1980).

2 5 6

2 1 . In tere s ti n gly—and aga i n , a re a s on to see the futu re of reg u l a ti on talk loc a ted el s ewh ere—this is not true of a rch i tect s . An example is the work of John de Mon chaux and J.
Mark Schuster. In their essay "Five Things to Do" and in the collection that essay introduces,
Preserving the Built Heritage, they describe the "five and only five things that governments can
do—five distinct tools that they can use—to implement their" policies (4–5): ownership and
operation (the state may own the resource); regulation (of either individuals or institutions);
incentives; property rights; information. Monchaux and Sc huster's five tools map in a complex way on the st ructure I have described, but significantly, we share a view of regulation as
a constant trade-off between tools.

22. See, for example, James C. Carter, The Provinces of the Written and the Unwritten Law
(New York: Banks & Brothers, 1889), who argues that the common law cannot be changed
(38–41).

23. See, for example, the discussion of wage fund theory in Hovenkamp, Enterprise and

American Law, 193–96.

24. For a fascinating account o f the coming of age of the idea that the natural environment might be tamed to a productive and engineered end,see John M. Barry, Rising Tide: The
Great Mississippi Flood of 1927 and How It Changed America (New York: Simon & Schuster,
1997).

25. As Roberto Unger puts it,"Modern social thought was born proclaiming that society
is made and imagined,that it is a human artifact rather than the expression of an underlying
natural order"; Social Theory, 1.

26. The idea of a free market was the obsession of the realists,especially Robert Hale;see
Barbara Fried, The Progressive Assault on Laissez-Faire: Robert Hale and the First Law and Eco -
n o m i cs Movem en t ( Ca m bri d ge , Ma s s . : Ha rva rd Un ivers i ty Pre s s , 1 9 9 8 ) :" E con omic life , l i ke
Clark's moral market, was constituted by a regime of property and c ontract rights that were
neither spontaneously occurring nor self-defining, but were rather the positive creation of the
s t a te" ( 2 – 3 ) . For a modern retell i n g, s ee Cass R. Su n s tei n , The Pa rtial Co n s ti tu ti o n ( Ca mbridge, Mass.: Harvard University Press,1993),51–53.

27. Americans with Disabilities Act (ADA) of 1990,42 USC §§ 12101 et seq.(1994).
28. See Alain Plessis, The Rise and Fall of the Second Empire,1852–1871, (1979) translated
by Jonathan Mandelbaum (English-language edition, New York: Cambridge University Press,
1985), 121; "Haussmann, Georges-Eugene Baron," in Encyclopedia Britannica, 5th ed., vol. 5
(1992).Steven Johnson criticizes other aspects of the change in Interface Culture, 63–64.

2 9 . See Robert A . Ca ro, The Power Broker: Robert Mo ses and the Fa ll of New Yo rk ( New

York: Alfred A. Knopf, 1974), 318.

30. Brin, The Transparent Society, 293.
3 1 . Con s i der civil ri ghts in the Am erican So ut h . Du ring the legi s l a tive hearings n gs on the
Civil Rights Act o f 1964, supporters of the bill called before the committee white, southern
employers and business owners whose discrimination against blacks was the prime target of
the legislation. Some of these employers and businessmen supported the bill because business
would improve:the labor pool would increase,causing wages to decrease,and the demand for
services would increase—so long, that is,as whites did not shift their custom. This last point
is what set the stage for business support for the Civil Rights Act. What business leaders feared
was the retaliation of whites against their voluntary efforts to integrate. The Civil Rights Act
ch a n ged the con text to make discri m i n a ti on against bl acks ill ega l . The businessman co u l d
t h en — wi t h o ut fear of the ret a l i a ti on of wh i te s — h i re or serve a bl ack because of ei t h er his
concern for the status of blacks or his concern to obey the law. By creating this ambiguity, the
l aw redu ced the sym bolic costs of h i ring bl ack s . This example dem on s tra tes how law can
change norms without government having control over the norms. In this case, the norm of
accom m od a ting bl acks was ch a n ged by giving it a second meaning—the norm of s i m p ly
obeying the law; see Lessig, "The Regulation of Social Meaning," 965–67.

2 5 7

3 2 . Thu r good Ma rs h a ll , E s q . , oral argument on beh a l f of re s pon den t s , Cooper v Aa ro n ,
358 US 1 (1958) (no. 1),in Fifty-four Landmark Briefs and Arguments of the Supreme Court of
the United States: Constitutional Law, edited by Philip B. Kurland and Gerhard Casper (Washington, D.C.: University Publications of America, 1975),533, 713.

3 3 . See , for ex a m p l e , Dys on , Rel e a se 2.0: "G overn m ent can play a divi s ive role vi s - à - vi s
com mu n i ti e s . O f ten , the more govern m ent provi de s , the less com mu n i ty mem bers themselves contribute" (43); in "The Regulation of Groups: The Influence of Legal and Nonlegal
Sa n cti ons on Co ll ective Acti on" (Un ivers i ty of C h i c a go Law Revi ew 63 [1996]: 1 3 3 ) , E ric A .
Posner argues that government help to a community can undermine the community.

3 4 . Cass Su n s tein points to seatbelt law as a hypo t h etical of "govern m ent reg u l a ti on permit[ing] people to ex press preferen ces by using the shield of the law to lessen the risk that priva te actors wi ll interfere with the ex pre s s i on [thro u gh norm a tive cen su re ] " ;" Legal In interference ce
with Priva te Preferen ce s ," Un ivers i ty of C h i c a go Law Revi ew 53 (1986): 1 1 2 9 ,1 1 4 5 . Al tern a tively,
s e a seatbelt laws have been used as the factual basis for cri ti ques of n orm spon s orship as inef fective
and no su b s ti tute for direct reg u l a ti on ; s ee Robert S. Al der and R. D avid Pittle, "Ca j o l ery or
Com m a n d : Are Edu c a ti on Ca m p a i gns an Adequ a te Su b s ti tute for Reg u l a ti on ? " Yale Jou rnal on
Reg u l a ti o n 1 (1984): 1 5 9 ,1 7 1 – 7 8 . However, the ob s erva ti ons may have been prem a tu re . John C.
Wri gh t , com m en ting on tel evi s i on's norm a tive con ten t , claims that " we have won the battle on
s e a tbel t s , just by a bu n ch of people get ting toget h er and sayi n g, ' It is indeed macho to put on a
s e a tbel t . It is macho and it is smart and it is manly and it is also feminine and smart and sav v y
and ch a rming to put on a seatbel t' " ; Ch a rles W. Gu s ewelle et al., " Round Ta ble Di s c u s s i on : Vi ol en ce in the Med i a ," Kansas Jou rnal of Law and Pu blic Pol i c y 4 (1995): 3 9 ,4 7 .

35. The analysis here was in part suggested by Minow, Making All the Difference: Inclusion,

Exclusion and American Law (1990).

3 6 . See Tracey L. Me a re s , "Social Orga n i z a ti on and Drug Law Enforcem en t ," Am eri c a n

Criminal Law Review 35 (1998):191.

3 7 . E ric Po s n er ("The Reg u l a ti on of Gro u p s") points to con texts within wh i ch government action may have had this effect.

38. See Tracey L. Meares, "Charting Race and Class Differences in Attitudes Toward Drug
Legalization and Law Enforcement: Lessons for Federal Criminal Law," Buffalo Criminal Law
Review 1 (1997): 137.

3 9 . In the mid-1970s the U. S . govern m ent spon s ored a campaign to spray para quat (a
herbicide that causes lung damage to humans) on the Mexican marijuana crop. This sparked
a public outcry that resulted in congressional suspension of funding in 1978. However, foll owing a con gre s s i onal amen d m ent in 1981, p a ra quat spraying was used on the dom e s ti c
marijuana crop during the 1980s. The publicity surrounding the use of paraquat in Mexico is
generally believed to have created a boom in the domestic marijuana industry and also an inc rease in the pop u l a ri ty of cocaine du ring the 1980s. See gen era lly Mi ch ael Is i kof f , " D E A
Finds Herbicides in Marijuana Samples," Washington Post, July 26, 1989,17. In "Drug Diplomacy and the Supply-Side Strategy: A Survey of United States Practice" (Vanderbilt Law Re -
vi ew 43 [1990]: 1 2 5 9 , 1275 n.99), Sandi R. Mu rphy gives a full history of the laws passed
relevant to paraquat; see also "A Cure Worse Than the Disease?," Time, August 29,1983,20.

40. Roe v Wade, 410 US 113 (1973).
41. Rust v Sullivan, 500 US 173 (1991).
42. Maher v Roe, 432 US 464 (1977).
43. Hodgson v Minnesota, 497 US 417 (1990).
44. This distinction between "direct" and "indirect" regulation, of course,has a long and
troubled history in philosophy as well as in law. Judith J. Thomson describes this difference in
her distinction between the trolley driver who must run over one person to save five and the
surgeon who may not harvest the organs from one healthy person to save five dying people;
see "The Trolley Problem," Yale Law Journal 94 (1985): 1395,1395–96. This difference is also

2 5 8

known as the "double effect doctrine," discussed in Philippa Foot, "The Problem of Abortion
and the Doctrine of the Double Effect," in Virtues and Vices and Other Essays in Moral Philos -
op hy ( Berkel ey: Un ivers i ty of Ca l i fornia Pre s s , 1 9 7 8 ) , 1 9 . See also Th omas J. Bole III, "Th e
Doctrine of Do u ble Effect : Its Philosophical Vi a bi l i ty," S ou t hwest Ph i l o sophical Revi ew 7
( 1 9 9 1 ) : 9 1 ; Fra n ces M. Ka m m , "The Doctrine of Do u ble Effect : Reflecti ons on Th eoreti c a l
and Practical Issues," Journal of Medicine and Philosophy 16 (1991): 571; Warren Quinn, "Actions, Intentions, and Consequences: The Doctrine of Double Effect," Philosophy and Public
Affairs 18 (1989): 334. The trouble in these cases comes when a line between them must be
drawn;here I do not need to draw any such line.

4 5 . Ri ch a rd Cra s well su ggests other examples making the same poi n t : the govern m en t
could (a) regulate product quality or safety directly or (b) disclose information about different products' quality or safety ratings,in the hope that manufacturers would then have an incentive to compete to improve those ratings; the government could (a) allow an industry to
remain monopolized and attempt directly to regulate the price the monopolist charged or (b)
break up the monopolist into several competing firms, in the hope that competition would
then force each to a more competitive price; the government could (a) pass regulations directly requiring corporations to do various things that would benefit the public interest or (b)
pass regulations requiring that corporate boards of directors include a certain number of "independent" representatives, in the hope that the boards would then d ecide for themselves to
act more consistently with the public interest.

46. See New York v United States, 505 US 144 (1992).
4 7 . Aida Torre s , "The Effects of Federal Funding Cuts on Fa m i ly Planning Servi ce s ,

1980–1983," Family Planning Perspectives 16 (1984): 134,135,136.

48. Rust v Sullivan, USNY (1990) WL 505726, reply brief,*7: "The doctor cannot explain
the medical safety of the procedure,its legal availability, or its pressing importance to the patient's health."

49. See Madsen v Women's Health Center, Inc., 512 US 753, 785 (1994) (Justice Antonin
Scalia concurring in the judgment in part and dissenting in part: "Today's decision . . . makes
it painfully clear that no legal rule or d octrine is safe fr om ad hoc nullification by this Court
when an occasion for its application arises in a case involving state regulation of abortion"
[quoting Thornburgh v American College of Obstetricians and Gynecologists, 476 US 747, 814
(1986) (Justice Sandra Day O'Connor dissenting)]).

50. Shelley v Kraemer, 334 US 1 (1948).
51. See Herman H. Long and Charles S. Johnson, People Versus Property: Race-Restrictive
Covenants in Housing (Nashville, Fisk University Press, 1947),32–33. Douglas S. Massey and
Nancy A. Denton point out that the National Association of Real Estate Brokers adopted an
article in its 1924 code of ethics stating that "a Realtor should never be instrumental in introducing into a neighborhood . . . members of any race or nationality . . . whose presence will
clearly be detrimental to property values in that neighborhood" (citing Rose Helper, Racial
Policies and Practices of Real Estate Brokers [1969],201); they also note that the Fair Housing
Authority advocated the use of race-restrictive covenants until 1950 (citing Kenneth T. Jacks on , Cra b grass Fro n ti er: the Su bu rba n i z a tion of the Un i ted St a te s [ 1 9 8 5 ] , 2 0 8 ) ; Am eri c a n
Apartheid: Se gregation and the Making of the Under Class (Cambridge, Mass.: Harvard University Press,1993),37,54.

52. See Massey and Denton, American Apartheid.
53. Michael Froomkin points to the Clipper chip regulations as another example. By using the standards-setting process for government purchases,the federal government could try
to achieve a standard for encryption without adhering to the Administrative Procedure Act.
"A stroke of bureaucratic genius lay at the heart of the Clipper strategy. Congress had not,and
to this date has not, given the executive branch the power to control the private use of encryption. Congress has not even given the executive the power to set up an escrow system for

2 5 9

keys. In the absence of any formal authority to prevent the adoption of unescrowed cryptogra phy, Cl i pper 's propon ents hit upon the idea of using the govern m en t's power as a major
consumer of cryptographic products to rig the market. If the government could not prevent
the public from using non con forming produ ct s , perhaps it could set the standard by purchasing and deploying large numbers of escrowed products";"It Came from Planet Clipper,"
15,24,1–33.

54. See http://thestandard.com/articles/display/0,1449,4165,00.html.
55. See "Legal Eagle" (letter to the editor), The Industry Standard, April 26,1999 (emphasis ad ded ) , ava i l a ble at http : / / w w w. t h e s t a n d a rd . com / a rti cl e s / a rti cl e _ pri n t / 0 , 1 4 5 4 , 4 3 0 6 , 0 0 .
html (visited May 30, 1999).

C H A P T E R E I G H T

1. I want to sidestep the raging debate about whether to call this mo vement the free software movement,the open source software movement, or something altogether different. The
reality is mo re important than the label. Activists will work out how best to claim the tradition. My aim is simply to understand the consequences of the struggle.

2. By "closed code" I don't mean anything conspiratorial. I mean simply code that does
not reveal its source.A code writer might have many reasons for hiding the source—including economic survival, security, or embarrassment. The crux of my argument is that, regardless of the reason, closed code is not as easily modified as open code.

3. Hunt, TCP/IP: Network Administration, 1–22, 6, 8; Loshin, TCP/IP: Clearly Explained,

13–17.

4. There is no standard reference model for the TCP/IP layers. Hunt refers to the four layers as the "n et work acce s s ," " i n tern et ," "h o s t - to-host tra n s port ," and "a pp l i c a ti on" l ayers ;
TCP/IP: Network Administration, 9. Loshin uses the terminology I follow in the text; TCP/IP:
Clearly Explained, 13–17. Despite the diff erent moniker, the functions performed in each of
these layers are consistent. As with any protocol stack model, data are "passed down the stack
when it is being sent to the network,and up the stack when it is being received from the network." Each layer "has its own independent data structures," with one layer "unaware of the
data structures used by"other layers; Hunt, TCP/IP: Network Administration, 9.

5. Loshin, TCP/IP: Clearly Explained, 18.
6. As Hafner and Lyon explain: "The general view was that any protocol was a potential
building bl ock , and so the best approach was to define simple pro toco l s , e ach limited in
scope, with the expectation that any of them might someday be joined or modified in various
unanticipated ways. The protocol design philosophy adopted by the NWG [network working
group] broke ground for what came to be widely accepted as the 'layered approach to protocols"; Where Wizards Stay Up Late, 147.

7. The fights over encryption at the link level, for example,are fights over the TCP/IP protocols. Some within the network industry have proposed that encryption be done at the gateways ays , with a met h od for dumping plain text at the ga tew ays if t h ere were proper lega l
authority—a kind of "private doorbell" for resolving the encryption controversy; see Elizabeth Kaufman and Roszel Thomsen II, "The Export of Certain Networking Encryption Produ cts Un der ELAs ," ava i l a ble at http : / / w w w. c i s co. com / w a rp / p u bl i c / 7 7 9 / gov t a f f / po l i c y / p a per /
paper_index.html (visited May 30,1999). This has been opposed by the Internet Architectural
Board (IAB) as inconsistent with the "end-to-end"architecture of the Internet; see IAB statement on "private doorbell" encryption, available at http://www.ietf.org/mail-archive/ietf-announce/msg01937.html (visited May 30,1999).

8 . See John C. Morl ey and Stan S. G el ber, The Em erging Di gital Fu tu re: An Overvi ew of
Broadband and Multimedia Networks (Danvers, Mass.: Boyd & F Fraiser Publishing C o., 1996);

2 6 0

Jerome H. Saltzer et al.,"End-to-End Arguments in System Design," in Integrated Broadband
Networks, edited by Amit Bhargava (New York:Elsevier Science Publishing Co.,1991),30.

9. See Timothy Wu, "Internet v Application: An Introduction to Application-Centered Internet Analysis," Virginia Law Review 86 (1999).

10. See Hafner and Lyon, Where Wizards Stay up Late, 174.
11. A 1994 HTML manual lists twenty-nine different browsers;see Larry Aronson, HTML

Manual of Style (Emeryville, Calif.: Ziff-Davis Press,1994), 124–26.

12. See Ibid., 4.
1 3 . O f co u rs e , not alw ays . Wh en com m ercial produ cti on of com p uters bega n , s of t w a re
was often a free addition to the computer. Its commercial development as proprietary came
on ly later; s ee Ira V. Hef f a n , "Copyleft ef t : L i censing Co ll a bora tive Works in the Di gital Age ,"
Stanford Law Review 49 (1997): 1487,1492–93.

14. Netscape's Communicator is an exception. As I explained,in 1998, the company gave
the source code for the product (minus some encr yption modules) to Mozilla, which would
continue the development of Mozilla as part of the open source movement;see "Mozilla Public Licen s e ," ava i l a ble at http : / / w w w. m oz i ll a . or g / N P L / N P L – 1 _ 1 F i n a l . h tml (vi s i ted May 31,
1 9 9 9 ) . See the discussion in Robert W. G omu l k i ewi c z , "The License Is the Produ ct : Comments on the Promise of Article 2B f or Software and Information Licensing," Berkeley Tech -
nology Law Journal 13 (1998): 891,924.

15. See Amy Harmon, "The Rebel Code," New York Times Magazine, February 21, 1999,

34.

16. At the time Linux was developed, the dominant thinking among computer scientists
was against a monolithic operating system operating out o f a single kernel and in favor of a
"m i c ro kern el " - b a s ed sys tem . M I N I X , a micro kern el sys tem , was the pri m a ry com peti tor at
the time. Torvalds consciously rejected this "modern" thinking and adopted the "traditional"
m odel for Linu x ; s ee "The Ta n en b a u m - Torvalds Deb a te ," in Open Sou rces: Vo i ces from the
Open Source Revolution, edited by Chris DiBona et al.(Sebastopol, Calif.: O'Reilly & Associates, 1999),221–52.

17. Technically, it does not sit in the public domain. Code from these open source projects
is licensed.GNU/Linux is licensed under the GNU GPL, which limits the possible use you can
make of Linux; essentially, you cannot take the public part and close it,and you cannot integrate the open part with the closed; see Bruce Perens, "The Open Source Definition," in Di-
Bona et al., Open Sources, 181–82. But for purposes of future open source development, the
code sits in the commons.On the idea and values of the commons,see, for example, Michael
A. Heller, "The Tragedy of the Anticommons: Property in the Transition from Marx to Markets," Harvard Law Review 111 (1998): 621; Stephen M. McJohn,"Fair Use and Privatization
in Copyright," San Diego Law Review 35 (1998): 61; Mark A. Lemley, "The Economics of Improvement in Intellectual Property Law," Texas Law Review 75 (1997): 989; Mark A. Lemley,
"Romantic Authorship and the Rhetoric of Property," Texas Law Review 75 (1997): 873; Jessica Litman, "The Public Domain," Emory Law Journal 39 (1990): 965; Carol M. Rose, "The
Several Futures of Property: Of Cyberspace and Folk Tales,Emission Trades and Ecosystems,"
Minnesota Law Review 83 (1998): 129.

18. See, for example, Stephen Shankland, "Big Blue Gives Green Light to Linux," CNET
News . co m , Febru a ry 16, 1 9 9 9 , ava i l a ble at http : / / w w w. n ews . com / News / Item / 0 , 4 , 3 2 4 7 6 , 0 0 .
h tml (vi s i ted May 30, 1 9 9 9 ) ; S Stephen en Shankland, " Big Blue Latches on to Linu x ," C N E T
News . co m , Febru a ry 18, 1 9 9 9 , ava i l a ble at http : / / w w w. n ews . com / News / Item / 0 , 4 , 3 2 5 6 3 , 0 0 .
html (visited May 30, 1999).

1 9 . Peter Ha rter, "The Legal and Policy Fra m ework for Global Electronic Com m erce ,"

comments at the Berkeley Center for Law and Technology Conference, March 5–6,1999.

2 0 . As I explain in more detail in ch a pter 16, tra n s p a rent modular code would do the

same thing as open code. Thus,the code could be closed yet achieve these same objectives.

2 6 1

C H A P T E R N I N E

1 . Ju s ti ce Holmes himsel f c a ll ed the wi ret a pping a "d i rty bu s i n e s s" ; O l m s tead v Un i ted

States, 277 US 438,470 (1928) (Justice Oliver Wendell Holmes Jr. dissenting).

2. Ibid.,457 (Chief Justice William H. Taft:the obtaining of evidence by wiretaps inserted
along telephone wires was done without trespass and thus did not violate the Fourth Amendment).

3. Ibid.,471 (Justice Louis D. Brandeis dissenting; Justices Holmes,Stone,and Butler also

filed dissents).

4. There is an extensive debate about the original meaning of the Fourth Amendment and
how it should be applied today. For the two camps, see Akhil Reed Amar, "Fourth Amendment First Principles," Harvard Law Review 107 (1994):757; Tracey Maclin, "The Complexity
of the Fourth Amendment:A Historical Review," Boston University Law Review 77 (1997):925
(critiquing Amar's argument).

5. See California v Acevedo, 500 US 565, 582 (1991) (Justice Antonin Scalia concurring:

describing warrant requirement as "riddled with exceptions").

6. See Bradford P. Wilson, "The Fourth Amendment as More Than a Form of Words: The
View from the Founding," in The Bill of Rights: Original Meaning and Current Understanding,
ed i ted by Eu gene W. Hi Hickok Jr. ( Ch a rl o t te s vi ll e : Un ivers i ty Press of Vi r gi n i a , 1 9 9 1 ) , 1 5 1 ,
156–57. As many have pointed out,there were not really any "police" at that time in the sense
that we understand the term today. The modern police f force is a creation of the nineteenth
century; see Carol S.Steiker, "Second Thoughts About First Principles," Harvard Law Review
107 (1994): 820,830–34;Stuntz, "The Substantive Origins of Criminal Procedure."

7. See Amar, "Fourth Amendment First Principles," 767;Stuntz, "The Substantive Origins

of Criminal Procedure," 400.

8. Indeed,as Professor William Stuntz argues quite effectively, one danger with warrants
in general is that judges become lax and yet the product of their work (the war rant) receives
great deferen ce in su b s equ ent proceed i n gs ; "Wa rrants and Fo u rth Am en d m ent Rem ed i e s ,"
Virginia Law Review 77 (1991): 881,893.

9. See Stuntz, "The Substantive Origins of Criminal Procedure," 396–406.
10. See United States v Virginia, 518 US 515, 566–67 (1996) (Justice Antonin Scalia dissenting: "Closed-minded they were—as every age is . . . with regard to matters it cannot guess,
because it simply does not consider them debatable").

1 1 . See Lawren ce Le s s i g, " F i del i ty in Tra n s l a ti on ," Texas Law Revi ew 71 (1993): 1 1 6 5 ,

1230.

12. Olmstead v United States, 277 US 438,470 (1928),464–65.
13. Ibid., brief for the Pacific Telephone & Telegraph Company (nos.493, 532,533).
14. Ibid., 473 (Justice Louis Brandeis dissenting).
15. "Translation" is not Brandeis's term,though it is a term of the courts. The idea is best
captured by Justice Robert H. Jackson in West Virginia State Board of Education v Barnette,
319 US 624,639–40 (1943): Nor does our duty to apply the Bill of Rights to assertions of official authority depend upon our possession of marked competence in the field where the inva s i on of ri ghts occ u rs . Tru e , the task of tra n s l a ting the majestic gen era l i ties of the Bi ll of
Rights, conceived as part of the pattern of liberal government in the eighteenth century, into
concrete restraints on officials dealing with the problems of the twentieth century, is one to
disturb self-confidence. These principles grew in soil which also produced a philosophy that
the individual was the center of society, that his liberty was attainable through mere absence
of governmental restraints, and that government should be entrusted with few controls and
only the mildest supervision over men's affairs. We must transplant these rights to a soil in
which the laissez-faire concept or principle of non-interference has withered at least as to economic affairs, and social advancements are increasingly sought through closer integration of

2 6 2

society and through expanded and strengthened governmental controls. These changed conditions often deprive precedents of reliability and cast us more than we would choose upon
our own judgment. But we act in these matters not by authority o f our competence but by
force of our commissions. We cannot, because of modest estimates of our competence in such
specialties as public education, withhold the judgment that history authenticates as the function of this Court when liberty is infringed."

16. See Robert Post, Constitutional Domains: Democracy, Community, Management (Cambridge, Mass.: Harvard University Press,1995),60–64.

17. See Lessig, "Fidelity in Translation," 1214–68; Lawrence Lessig, "Translating Federalism: United States v Lopez," Supreme Court Review 1995 (1995): 125,146. For a more sophisti c a ted analysis of h ow ch a n ging tech n o l ogies in the con text of tel ecom mu n i c a ti ons is
affecting le gislation and judicial doctrine, see Monroe E. Price and John F. Duffy, "Technological Change and Doctrinal Persistence: Telecommunications Reform in Congress and the
Court," Columbia Law Review 97 (1997): 976.

18. So, for example, the translations to support federalism are translations on the right,

while the translations to support criminal rights are t translations on the left.

19. Katz v United States, 389 US 347, 353 (1967).
2 0 . L a u ren ce H. Tri be , "The Con s ti tuti on in Cybers p ace : L aw and Liberty Beyond the
E l ectronic Fron ti er," ad d ress at the First Con feren ce on Com p uters , Freedom , and Privac y,
March 26,1991, reprinted in The Humanist (September-October 1991): 15,20–21.

21. Katz v United States, 389 US 347,351 (1967).
22. As the history of the Fourth Amendment's protection of privacy since Katz will attest,
the technique used by Stewart was in the end quite ineffectual. When tied to property notions,
no doubt the reach of the Fourth Amendment was narrow. But at least its reach went as far as
the reach of property. Because "property"is a body of law independent of privacy questions,
it was resilient to the pressures that privacy placed on it. But once the Court adopted the "reasonable expectation of privacy" test, the Court could lat er restrict these "reasonable expectations" in the Fourth Amendment context, with little consequence outside that context. The
result has been an ever-decreasing scope for privacy's protection.

23. See Lessig, "Translating Federalism," 206–11.
24. Tribe, "The Constitution in Cyberspace," 15.
25. See Lawrence Lessig, "Reading the Constitution in Cyberspace," Emory Law Journal 45

(1996): 869,872.

26. This example is drawn from Maryland v Craig, 497 US 836 (1990).
27. See Tribe, "The Constitution in Cyberspace," 15.
28. "A latent ambiguity arises from extraneous or collateral facts which make the meaning of a written instrument uncertain although the language the thereof be clear and unambiguous. The usual instance of a latent ambiguity is one in which a writing refers to a particular
person or thing and is thus apparently clear on its face, but upon application to external objects is found to fit two or more of them equally"; Williston on Contracts, 3d ed., edited by
Walter H. E. Jaeger (Mount Kisco, N.Y.: Baker, Voorhis,1957),§ 627,898.

29. See United States v Virginia, 518 US 515, 566–67 (1996) (Justice Antonin Scalia dissenting).

3 0 . See Bern a rd Wi ll i a m s , "The Rel a ti ons of P h i l o s ophy to the Profe s s i ons and Pu bl i c

Life," unpublished manuscript.

C H A P T E R T E N

1. Harold Smith Reeves,"Property in Cyberspace," University of Chicago Law Review 63

(1996): 761.

2 6 3

2 . This in the end was not his con clu s i on . He con clu ded inste ad , not that bo u n d a ri e s
should not be protected in cyberspace, but rather that the unconventional nature of cyberspace requires that boundaries be set along nontraditional context-specific lines. This conclusion, Reeves asserts, requires the law to understand both the environment of cyberspace and
the interests of those who transact in that space;see ibid.,799.

3. Cf. Yochai Benkler, "Free as the Air to Common Use: First Amendment Constraints on

Enclosure of the Public Domain," New York University Law Review 74 (1999):354.

4. Maureen O'Rourke has extended the idea of the technological fences that cyberspace
m i ght provi de , de s c ri bing tech n i ques that web site s , for ex a m p l e , m i ght use to con tro l , or
block, links from one site to anothe r; see "Fencing Cyberspace: Drawing Borders in a Virtual
World," Minnesota Law Review 82 (1998):610, 645–47.

5. See, for example, Stephen Breyer, "The Uneasy Case for Copyright: A Study of Copyright in Books,Photocopies,and Computer Programs," Harvard Law Review 84 (1970):281.
6. Copyright gives other rights as well—such as the right to reclaim an assigned copyright
or the right of first sale. For a lucid introduction,see William F. Patry, Latman's The Copyright
Law, 6th ed. (Washington, D.C.: Bureau of National Affairs,1986). For something more than
lucid,see James Boyle,"Intellectual Property Policy Online: A Young Person's Guide," Harvard
Journal of Law and Technology 10 (1996): 47.

7. See Richard A. Posner, Law and Literature, 2d ed.(Cambridge, Mass.: Harvard University Press, 1998),389–92 (discussing incentives to write even without copyright).

8. For the real constraint on publication initially was paper, not presses. Before the invention of wood-based paper, paper was produced from cloth. Cloth,however, was extremely expen s ive . While a pers i s tent myth is that one source for this cloth was Egyptian mu m m i e s
(Scott D. N. Cook, "Technological Revolutions and the Gutenberg Myth," in Internet Dreams:
Archetypes, Myths, and Metaphors, edited by Mark Stefik [1996],75), there is no support for
this claim. See Joseph A.Dane, "The Curse of the Mummy Paper," Printing History 17 (1996):
18. Nonetheless,the shortage of paper is well established (ibid.,18–19).I am grateful to Consuelo Dutschke for help with this history.

9. For a complete and readable account of the transformation in technology, and law's response, see Paul Goldstein, Copyright's Highway: The Law and Lore of Copyright from Guten -
berg to the Celestial Jukebox (New York: Hill and Wang, 1994).

10. See Sony Corporation of America v Universal City Studios, Inc., 464 US 417,421 (1984),
which,in defining "time-shifting" as using a VTR principally to record a program one cannot
view as it is being televised and then to watch it once at a later time, classifies this practice as
a fair use of a copyrighted work that does not entitle the copyright holder to any remedy.

1 1 . See Jonathan Evan Goldber g, " Now That the Futu re Has Arrived , Maybe the Law
Should Take a Look: Multimedia Technology and Its Interaction with the Fair Use Doctrine,"
Am erican Un ivers i ty Law Revi ew 44 (1995): 9 1 9 ; Ma ry L. Mi ll s ," New Tech n o l ogy and the
Limitations of Copyright Law: An Argument for Finding Alternatives to Copyright L egislati on in an Era of Rapid Tech n o l ogical Ch a n ge ," C h i c a go - Kent Law Revi ew 65 (1989): 3 0 7 ;
Kenneth P. Weinberg, "Cryptography: 'Key Recovery' Shaping Cyberspace (Pragmatism and
Theory)," Journal of Intellectual Property Law 5 (1998): 667.

1 2 . Ju d ge Po s n er usef u lly distinguishes bet ween ch a n ges that might help an indivi du a l
author and changes that help authors as a class. Some decreased copyright protection for authors as a whole would benefit authors as a whole,since copyright imposes costs on authors
(the wri ting of o t h ers is an input to their own futu re wri ti n g ) ; s ee Law and Li tera tu re ,
389–405.

13. See Michelle Skatoff-Gee, "Changing Technologies and the Exp ectation of Privacy: A
Modern Dilemma," Loyola University of Chicago Law Journal 28 (1996):189, 201–4, who discusses Congress's enactment of the Electronic Communications Privacy Act of 1986 in an effort to update ex i s ting law and keep pace with ch a n ging tech n o l ogy. But see Sa n d ra Byrd

2 6 4

Petersen, "Your Life as an Open Book: Has Technology Rendered Personal Privacy Virtually
Obsolete?," Federal Communications Law Journal 48 (1995):163, who argues that privacy laws
in the United States have not kept pace with technological developments.

14. See Esther Dyson,"Int ellectual Value," Wired (July 1995):137, who discusses the effect
of the new econ omic envi ron m ent of the Net on intell ectual property. John Perry Ba rl ow
("The Economy of Ideas," Wired [March 1994]:85) asserts that "copyright and patent law was
developed to convey forms and methods of expression entirely different from the vaporous
cargo it is now being asked to carry."

15. As Nicholas Negroponte puts it,"Most people worry about copyright in terms of the
ease of making copies. In the digital world,not only the ease is at issue, but also the fact that
the digital copy is as perfect as the original and, with some fancy computing, even better. In
the same way that bit strings can be error-corrected,a copy can be cleaned up, enhanced,and
have noise removed. The copy is perfect"; Being Digital (1995),58.

16. U.S. Department of Commerce, Task Force—Working Group on Intellectual Property
Rights,"Intellectual Property and the National Information Infrastructure: The Report of the
Working Group on In tell ectual Property Ri gh t s ," ava i l a ble at http : / / w w w. u s pto. gov / web / offices/com/doc/ipnii/ (visited May 30, 1999, and hereinafter referred to as the White Paper).
See also Boyle,"Intellectual Property Policy Online," 66.

17. George Smirnoff III ("Copyright on the Internet:A Critique of the White Paper's Recommendation for Updating the Copyright Act and How the Courts Are Already Filling in Its
Most Important Shortcoming, Online Service Provider Liability," Cleveland State Law Review
44 [1996]:197) criticizes the White Paper's lack of completeness, inconsistencies,and apparent lack of adequate consideration;see also Pamela Samuelson, "The Copyright Grab," Wired
(January 1996):134,136. By contrast,Gary W. Glisson ("A Practitioner's Defense of the White
Paper," Oregon Law Review 75 [1996]: 277) argues that the White Paper is neither a misleading summary of the state of intellectual property law nor a proposal for dramatic changes. For
an extensive analysis of the copyright issues raised by cyberspace,see Trotter Hardy, "Project
Looking Forward: Sketching the Future of Copyright in a Networked World," U.S. Copyright
Office final report (1998), available at http://lcweb.loc.gov/copyright/reports (visited May 30,
1999).

18. For a summary of the changes called for by the White Paper, see Bruce Lehman, address before the Inaugural Engelberg Conference on Culture and Economics of Participation
in an International Intellectual Property Regime, reprinted in New York University Journal of
International Law and Politics 29 (1996–97): 211,213–15; White Paper, 17.

1 9 . The latest su ch threat is the anti c i rc u mven ti on provi s i on of the Di gital Mi ll en n iu m
Copyright Act, which makes it a crime (subject to complex exceptions) to manufacture code
to circumvent a copyright protection mechanism, even if the use of the underlying material
itself would be a fair use; see Pub.L.105–304,112 Stat 2877 (1998) (prohibiting the manufacture,importation, or distribution of "devices, products, components" that "defeat technological methods of preventing unauthorized use").

2 0 . See Ba rl ow, "The Econ omy of Ide a s ," 1 2 9 ; s ee also John Perry Ba rl ow, " Pa pers and
Comments of a Symposium on Fundamental Rights on the Information Superhighway," An -
nual Survey of American Law 1994 (1994): 355, 358. Barlow argues that "it is not so easy to
own that which has never had any physical dimension whatso ever," unlike traditional forms
of property. "We have tended to think," he adds, "that copyright worked well because it was
physically difficult to transport intellectual properties without first manifesting them in some
physical form. And it is no longer necessary to do that."

2 1 . See Ma rk Stef i k , "S h i f ting the Po s s i bl e : How Tru s ted Sys tems and Di gital Property
Ri ghts Ch a ll en ge Us to Rethink Di gital Pu bl i s h i n g," Berkel ey Te ch n ol o gy Law Jou rnal 1 2
(1997): 137; Mark Stefik, "Trusted Systems," Scientific American (March 1997): 78; Mark Sten o t e s

2 6 5

fik,"Letting Loose the Light: Igniting Commerce in Electronic Publication," in Stefik, Internet
Dreams, 220–22, 226–28.

22. See Joel R. Reidenberg, "Governing Networks and Rule-Making in Cyberspace," Emory

Law Journal 45 (1996): 911.

23. In Shifting the Possible (142–44), Stefik discusses how trusted printers combine four
elements—print rights, encrypted online distribution,automatic billing for copies,and digital watermarks—in order to monitor and control the copies they make.

24. Ibid.
25. David Hackett Fischer, Albion's Seed: Four British Folkways in America (New York: Oxford University Press,1989),765.

26. See American Legal Realism, edited by William W. Fisher III et al.(New York: Oxford
University Press, 1993), 98–129; John Henry Schlegel, American Legal Realism and Empirical
Social Science (Chapel Hill: University of North Carolina Press,1995). For a nice modern example of the same analys i s , s ee Keith Ao k i , " ( In tell ectual) Property and Soverei gn ty: No te s
Toward a Cultural Geography of Authorship," Stanford Law Review 48 (1996): 1293.

2 7 . See Fri ed , The Pro gre s s ive Assault on La i s se z - Fa i re , 1 – 2 8 ; s ee also Joel P. Trach tm a n
("The International Economic Law Revolution," University of Pennsylvania Journal of Inter -
national Economic Law 17 [1996]: 33,34), who notes that many realists and critical le gal theorists have asserted that "private law"is an oxymoron.

28. Judges have also made this argument; see Lochner v New York, 198 US 45, 74 (1905)

(Justice Oliver Wendell Holmes Jr. dissenting).

29. This is the epistemological limitation discussed in much of Friedrich A. von Hayek's
work; see, for example, Law, Legislation, and Liberty, vol. 2 (Chicago: University of Chicago
Press, 1978).

30. Boyle, Shamans,Software, and Spleens, 174.
31. I am hiding a great deal of philosophy in this simplified utilitarian account, but for a
powerful economic grounding of the point,see Harold Demsetz, "Toward a Theory of Property Rights," American Economics Review 57 (1967): 347.

32. For a wonderfully clear introduction to this point,as well as a complete analysis of the
law, see Robert P. Merges et al., Intellectual Property in the New Technological Age (New York:
Aspen Law and Business,1997), ch.1.

33. Thomas Jefferson,letter to Isaac Mcpherson, August 13,1813, reprinted in Writings of
Thomas Jef ferso n , 1 7 9 0 – 1 8 2 6 , vo l . 6 , ed i ted by H. A . Wa s h i n g ton (1854), 1 8 0 – 8 1 , qu o ted in
Graham v John Deere Company, 383 US 1,8–9 n.2 (1966).

34. For the classic discussion,see Kenneth J. Arrow, "Economic Welfare and the Allocation
of Resources for Invention," in The Rate and Direction of Inventive Activity: Economic and So -
cial Factors (Princeton,N.J.: Princeton University Press,1962),609,616–17.

3 5 . For a powerf u lly com pelling probl em a ti z a ti on of the econ omic pers pective in this
context, see Boyle,"Intellectual Property Policy Online," 35–46. Boyle's work evinces the indeterminacy that e conomics ought to profess about whether increasing property rights o ver
information will also increase the production of information.

3 6 . Some wi ll insist on calling this "property " ; s ee Frank H. E a s terbroo k ," In tell ectu a l

Property Is Still Property," Harvard Journal of Law and Public Policy 13 (1990):108.

37. This is the message of Justice Stephen Breyer's work on copyright, for example, "The

Uneasy Case for Copyright."

38. For an extensive and balanced analysis,see William M.Landes and Richard A. Posner,
"An Econ omic An a lysis of Copyri ght Law," Jou rnal of Legal Stu d i e s 18 (1989): 3 2 5 , 3 2 5 – 2 7 ,
344–46. These authors note that because ideas are a public good—that is,an infinite number
of people can use an idea without using it up—ideas are readily appropriated from the creator by other people. Hence, copyright protection attempts to balance efficiently the benefits

2 6 6

of c re a ting new works with the losses from limiting access and the costs of ad m i n i s teri n g
copyright protection; copyright protection seeks to promote the public benefit of advancing
knowledge and learning by means of an incentive system. The economic rewards of the marketplace are offered to authors in order to stimulate them to produce and disseminate new
works (326). See also Posner, Law and Literature, 389–405.

39. These limits come from both the limits in the copyright clause, which sets its purposes
out quite clearly, and the First Amendment; see, for example, Feist Publications, Inc. v Rural
Telephone Service Co., 499 US 340,346 (1991).

40. The "first sale" doctrine was developed under § 27 of the former Copyright Act (17
USC [1970]) and has since been adopted under § 109(a) of the pre s ent Copyri ght Act ; s ee
United States v Goss, 803 F2d 638 (11th Cir 1989) (discussing both versions of the Copyright
Act).

41. Europeans like to say that "moral rights" have been part of their system since the b eginning of time, but as Professor Jane C.Ginsburg has shown with respect to France,they are
actu a lly a nineteen t h - cen tu ry cre a ti on ; s ee "A Tale of Two Copyri gh t s : L i tera ry Property in
Revolutionary France and America," Tulane Law Review 64 (1990): 991.
42.Or so it is argued in Eldred v Reno (DDC filed January 4,1999).
43. It is useful to compare the p rotection that copyright gives to the protection of trade
secret law. All of the protection of trade secret law comes, in a sense, from the architectural
constraints I have described. One is always permitted, that is, to reverse-engineer to discover
a trade sec ret ; s ee Kewanee Oil Co m pa ny v Bicron Co rpo ra ti o n , 416 US 470, 476 (1974): "A
trade secret law . . . does not offer protection against discovery by fair and honest means, such
as by independent invention, accidental disclosure, or . . . reverse engineering."

4 4 . 86 F3d 1447 (7th Cir 1996); s ee also Easterbroo k ," In tell ectual Property Is Sti ll Property,"
1 1 3 – 1 4 . For an excell ent account of the deb a te ,s ee Ch a rles R. Mc Ma n i s , "The Priva ti z a ti on (or
'S h ri n k - Wra pp i n g') of Am erican Copyri ght Law," C a l i fo rnia Law Revi ew 87 (1999): 1 7 3 ,1 8 3 .

4 5 . This is a referen ce to the recent battle to draft what was ori gi n a lly call ed the Un i form
Com m ercial Code 2B, and more recen t ly the Un i form Com p uter In form a ti on Tra n s acti on s
Act (UCITA ) . By essen ti a lly ra ti f ying the cl i ck - wrap agreem en t , this code would fac i l i t a te
online mass con su m er con tracts governing the sale of "online inform a ti on ." This move has
been wi dely cri ti c i zed ; s ee "Sym po s iu m : In tell ectual Property and Con tract Law for the Inform a ti on Age : The Im p act of Arti cle 2B of the Un i form Com m ercial Code on the Futu re of
In form a ti on and Com m erce ," C a l i fo rnia Law Revi ew 87 (1999): 1 ; L awren ce Le s s i g, " Pain in
the OS," The In du s try St a n d a rd , Febru a ry 5, 1 9 9 9 , ava i l a ble at http : / / w w w. t h e s t a n d a rd .
com / a rti cl e s / d i s p l ay / 0 , 1 4 4 9 , 3 4 2 3 , 0 0 . h tml (vi s i ted May 30, 1 9 9 9 ) . My cri ticism is that wh i l e
the rh etoric of this move is gro u n ded in the "f reedom of con tract ," the code actu a lly doe s
nothing to en su re that the con tracting process produ ces understanding of the terms of t h e
con tract by both parties to the con tract . The incen tives cre a ted by provi s i ons like the " Res t a tem ent (Second) of Con tract s" (§ 211) are not pre s ent in the UCITA .U C I TA pre su ppo s e s
that if the con su m er had a ch a n ce to unders t a n d , he unders t a n d s . But from an ef f i c i en c y
pers pective , l et alone a ju s ti ce pers pective , the con su m er is not the ch e a pest unders t a n d i n g
produ cer. The code simply ra ti fies the con tract that the sell er propo s e s . This is not "f reedom
of con tract ," but con tract according to wh a tever the sell er says . For a useful analys i s ,s ee Wa lter A .E f f ro s s , "The Legal Arch i tectu re of Vi rtual Store s : World Wi de Web Si tes and the Un iform Com m ercial Code ," San Di ego Law Revi ew 34 (1997): 1 2 6 3 , 1 3 2 8 – 5 9 .

4 6 . See Wi lliam W. F i s h er III, "Com p u l s ory Terms in In tern et - Rel a ted Con tract s ,"
Chicago-Kent Law Review 73 (1998). Fisher catalogs public policy restrictions on freedom of
contract, which he characterizes as "ubiquitous."

47. An argument is raging about whether, even through law, this modification of the default copyright law should be permitted. Mark A. Lemley has catalogued the provisions of the
Copyright Act that are arguably put at risk by contracting behavior; see "Beyond Preemption:

2 6 7

The Law and Policy of Intellectual Property Licensing," California Law Review 87 (1999):111;
see also A. Michael Froomkin, "Article 2B as Legal Software for Electronic Contracting—Operating System or Trojan Horse?," Berkeley Technology Law Journal 13 (1998):1023; Michael J.
Madison,"Legal-War: Contract and Copyright in the Digital Age," Fordham Law Review 67
(1998): 1025; David Nimmer et al., "The Metamorphosis of Contract into Expand," Califor -
nia Law Review 87 (1999):17; Pamela Samuelson,"Intellectual Property and Contract Law for
the Information Age: Foreword," California Law Review 87 (1999): 1. The questions Lemley
raises,however, cannot be easily raised when it is the code that protects the intellectual property interest; Maureen A. O'Rourke, "Copyright Preemption After the ProCD Case:A Market-
Based Approach," Berkeley Technology Law Journal 12 (1997): 53.

4 8 . See Tom W. Bell ," Fair Use vs . Fa red Us e : The Im p act of Autom a ted Ri ghts Ma n a gem en t
on Copyri gh t's Fair Use Doctri n e ," No rth Carolina Law Revi ew 76 (1998): 5 5 7 ,5 8 1 – 8 4 . Bell argues that tech n o l ogy wi ll prove more ef fective than fair use in curing the market failu re that results wh en tra n s acti on costs disco u ra ge otherwise va lue-maximizing uses of copyri gh ted work ;
s ee also the Wh i te Pa per ob s erva ti on that "it may be that tech n o l ogical means of tracking tra n sacti ons and licensing wi ll lead to redu ced app l i c a ti on and scope of the fair use doctri n e" ( 7 4 ) .

4 9 . See Bell , " Fair Use vs . Fa red Us e ," 5 8 2 – 8 4 ; U. S . Dep a rtm ent of Com m erce , Ta s k
Force — Working Group on In tell ectual Property Ri gh t s , " In tell ectual Property and the National Information Infrastructure," 66 n.228,notes the difficulty of defining the bounds of the
fair use doctrine.

50. For a foundational modern work on the nature of fair use,see Wendy J. Gordon,"Fair
Use as Market Failure:A Structural and Economic Analysis of the Betamax Case and Its Precedents s s ors ," Col u m bia Law Revi ew 82 (1982): 1 6 0 0 . A more recent work by Wi lliam Fisher
( " Recon s tru cting the Fair Use Doctri n e ," Ha rva rd Law Revi ew 101 [1988]: 1 6 5 9 , 1 6 6 1 – 9 5 )
considers both the efficiency and utopian goals of copyright law.

51. See Gibbons v Ogden, 22 US 1 (1824) (striking down New York's grant of a monopoly
of steamboat navigation on the Hudson River as inconsistent with the federal Coasting Act of
1793); McCulloch v Maryland, 17 US 316 (1819) (pronouncing that C ongress has the power
to do what is "necessary and proper" to achieve a legitimate end, like the regulation of interstate commerce).

52. See Bernard C.Gavit, The Commerce Clause of the United States Constitution (Bloomington, Ind.: Principia Press,1932),84.

5 3 . See Pen s a cola Tel egraph Co m pa ny v We s tern Union Tel egraph Co m pa ny, 96 US 1, 9

(1877).

5 4 . As one com m en t a tor put it near the tu rn of the cen tu ry: " If the power of Con gre s s
has a wi der inciden ce in 1918 than it could have had in 1789, this is merely because produ cti on is more depen dent now than then on ex tra - s t a te market s . No state liveth to itsel f
a l one to any su ch ex tent as was true a cen tu ry ago. What is ch a n ging is not our sys tem of
govern m en t , but our econ omic or ga n i z a ti on" ; Th omas Reed Powell , "The Child Labor Law,
the Tenth Am en d m en t , and the Com m erce Cl a u s e ," S ou t h ern Law Quarterly 3 (1918): 1 7 5 ,
2 0 0 – 2 0 1 .

5 5 . See Al exis de Tocqu evi ll e , Dem o cracy in Am eri c a , vo l . 1 (New York : Vi n t a ge , 1 9 9 0 ) ,
158–70, on the idea that the frame rs' design pushed states to le gislate in a broad domain and
keep the local government active.

56. See Maryland v Wirtz, 392 US 183,201 (1968) (Justice William O. Douglas dissenting:
the majority's bringing of employees of state-owned enterprises within the reach of the commerce clause was "such a serious invasion of state sovereignty protected by the Tenth Amendm ent that it . . . [was] not con s i s tent with our con s ti tuti onal federa l i s m" ) ; St a te Boa rd of
Insurance v Todd Shipyards Corporation, 370 US 451, 456 (1962) (holding that "the power of
Congress to grant protection to interstate commerce against state regulation or taxation or to
withhold it is so complete that its ideas of policy should prevail") (citations omitted).

2 6 8

5 7 . See Mi ch ael G. Frey, " Un f a i rly App lying the Fair Use Doctri n e : Pri n ceton Un ivers i ty
Press v Michigan Document Services, 99 F3d 1381 (6th Cir 1996)," University of Cincinnati Law
Review 66 (1998): 959, 1001; Frey asserts that "copyright p rotection exists primarily for the
benefit of the public,not the benefit of individual authors. Copyright law does give authors a
con s i dera ble ben efit in terms of the mon opo l i s tic ri ght to con trol their cre a ti on s , but that
right exists only to ensure the creation of new works. The fair use doctrine is an important
safety valve that ensures that the benefit to individual authors does not outweigh the benefit
to the public"; Marlin H. Smith ("The Limits of Copyright: Property, Parody, and the Public
Domain," Duke Law Journal 42 [1993]: 1233, 1272) asserts that "copyright law is better un -
derstood as that of a gatekeeper, controlling access to copyrighted works but guaranteeing, via
fair use,some measure of availability to the public."

58. See Mark Gimbel ("Some Thoughts on the Implications of Trusted Systems for Intellectual Property Law," Stanford Law Review 50 [1998]: 1671, 1686), who notes that fair use
can be "explained as a method of curing the market failure that results when high transaction
costs discourage otherwise economically efficient uses of copyrighted material," and that "because technologies like trusted systems promise to reduce the costs of licensing copyrighted
works—thereby curing this market failure—some argue that the doctrine of fair use will for
the most part be rendered unnecessary, obviating the need to regulate technologies that un -
undermine it"; Lydia Pallas L oren ("Redefining the Market Failure Approach to Fair Use in an
Era of Copyright Permission Systems," Journal of Intellectual Property Law 5 [1997]:1, 7) asserts that under a "narrowed market failure view of fair use, if a copyright owner can estab -
lish an efficient 'permission system' to collect fees for a certain kind of use,then the copyright
owner will be able to defeat a claim of fair use."
59. Stefik,"Letting Loose the Light," 244.
60. Efficient here both in the sense of cheap to track and in the sense of cheap to then discriminate in pricing; William W. Fisher III,"P roperty and Contract on the Internet," Chicago-
Kent Law Review 74 (1998).

61. Julie E. Cohen, "A Right to Read Anonymously: A Closer Look at 'Copyright Management' in Cyberspace," Connecticut L aw Review 28 (1996): Reading anonymously is "so intimately connected with speech and freedom of thought that the First Amendment should be
understood to guarantee such a right" (981,982).

62. "The freedom to read anonymously is just as much a part of our tradition, and the
choice of reading materials just as expressive of identity, as the decision to use or withhold
one's name" (ibid.,1012).

63. See Lessig, "Translating Federalism," 125.
64. See Olmstead v United States 277 US 438, 474 (1928) ( Justice Louis Brandeis dissenting: "Can it be that the Constitution affords no protection against such invasions of individual security?").

6 5 . Peter Hu ber relies ex p l i c i t ly on the high costs of con trol in his rebuttal to Orwell 's
1984; see Orwell's Revenge: The 1984 Palimpsest (New York: Maxwell Macmillan International,
1994). But this is a weak basis on which to build liberty, especially as the cost of networked
control drops. Frances Cairncross ( The Death of Distance: How the Communications Revolu -
tion Wi ll Change Our Live s [ Bo s ton : Ha rva rd Business Sch ool Pre s s , 1 9 9 7 ] , 194–95) ef fectively challenges the idea as well.

66. Washington, Writings of Thomas Jefferson, 6:180–81.
6 7 . A founding work is David Lange , " Recognizing the Pu blic Dom a i n ," Law and Co n -
temporary Problems 44 (1981): 147. There are many imp ortant foundations, however, to this
argument. See, for example, Benjamin Kaplan, An Unhurried View of Copyright (New York:
Co lu m bia Un ivers i ty Pre s s , 1 9 6 7 ) . G ordon ("Fair Use as Ma rket Fa i lu re") argues that the
courts should employ fair use to permit uncompensated transfers that the market is incapable
of ef effectuating a ti n g ; s ee also Wen dy J. G ordon , "On Owning In form a ti on : In tell ectual Property
and Restitutionary Impulse," Virginia Law Review 78 (1992):149. In "Reality as Artifact: From

2 6 9

Feist to Fair Use" (Law and Contemporary Problems 55 5PG [1992]:93,96), Gordon observes
t h a t , while imagi n a tive works are cre a tive , t h ey may also com prise fact s , wh i ch need to be
widely available for public dissemination.Gordon's "Toward a Jurisprudence of Benefits: The
Norms of Copyright and the Problem of Private Censorship" (University of Chicago Law Re -
view 57 [1990]:1009) is a discussion of the ability of copyright holders to deny access to critics and others ; s ee also Wen dy Gordon , "An In qu i ry into the Merits of Copyri gh t : Th e
Ch a ll en ges of Con s i s ten c y, Con s en t , and Enco u ra gem ent Th eory," St a n fo rd Law Revi ew 4 1
(1989): 1343.

6 8 . In ad d i ti on to Boyl e , I have learn ed most from Keith Ao k i , Yochai Ben k l er, Julie Coh en , Niva Elkin-Koren , Peter Ja s z i , Ma rk Lem l ey, Jessica Litm a n , Neil Net a n el , Ma r ga ret
Rad i n , and Pam Sa mu el s on , but no do u bt I have not re ad wi dely en o u gh . See , for ex a m p l e ,
Keith Ao k i ," Foreword to In n ova ti on and the In form a ti on Envi ron m en t : In interrogating ting the
E n entrepreneur eu r," O regon Law Revi ew 75 (1996): 1 ; in " ( In tell ectual) Property and Soverei gn ty,"
Aoki discusses the ch a ll en ges to the trad i ti onal con cept of property that arise from the
growth of d i gital inform a ti on tech n o l ogy; in "Aut h ors , Inven tors , and Tradem a rk Own ers :
Priva te In tell ectual Property and the Pu blic Dom a i n" (Col u m bi a - V LA Jou rnal of Law and the
Art s 18 [1993]: 1 ) , he ob s erves the shifting bo u n d a ries in intell ectual property law bet ween
"p u bl i c" and "priva te" realms of i n form a ti on and argues that trends to increase the nu m ber
of exclu s ive ri ghts for aut h ors are converting the public domain into priva te intell ectu a l
property and con s training other types of s oc i a lly va lu a ble uses of ex pre s s ive works that do
not fit the "a ut h ors h i p" m odel underlying Am erican copyri ght trad i ti on s ; he also argues that
recent ex p a n s i on of tradem a rk law has all owed tradem a rk own ers to obtain property ri gh t s
in their tradem a rks that do not furt h er the Lanham Act's goal of preven ting con su m er conf u s i on . Ben k l er, " Free as Air to Com m on Us e" ; Yochai Ben k l er, "Overcoming Agora ph obi a :
Building the Com m ons of the Di gi t a lly Net worked Envi ron m en t ," Ha rva rd Jou rnal of Law
and Te ch n ol o gy 11 (1998): 2 8 7 ; Julie E. Co h en , "Copyri ght and the Ju ri s pru den ce of Sel f -
Hel p," Berkel ey Te ch n ol o gy Law Jou rn a l 13 (1998): 1 0 8 9 ; Julie E. Co h en ," Loch n er in Cybers p ace : The New Econ omic Ort h orthodoxy of ' Ri ghts Ma n a gem en t ,' " Mi ch i gan Law Revi ew 9 7
( 1 9 9 8 ) :4 6 2 ; Julie E. Co h en , "Some Reflecti ons on Copyri ght Ma n a gem ent Sys tems and Laws
De s i gn ed to Pro tect Th em ," Berkel ey Te ch n ol o gy Law Jou rn a l 12 (1997): 1 6 1 ,1 8 1 – 8 2 ; Julie E.
Co h en , " Revers e - E n gi n eering and the Rise of E l ectronic Vi gi l a n ti s m : In tell ectual Property
Im p l i c a ti ons of ' Lock - O ut' Progra m s ," S ou t h ern Califo rnia Law Revi ew 68 (1995): 1 0 9 1 . Niva
E l k i n - Koren , "Con tracts in Cybers p ace : Ri ghts Wi t h o ut Laws ," C h i c a go - Kent Law Revi ew 7 3
( 1 9 9 8 ) ; Niva Elkin-Koren , "Copyri ght Policy and the Limits of Freedom of Con tract ," Berke -
l ey Te ch n ol o gy Law Jou rn a l 12 (1997): 9 3 , 107–10 (cri ticizing the ProCD dec i s i on ) ; Niva
E l k i n - Koren , "Cyberl aw and Social Ch a n ge : A Dem oc ra tic Approach to Copyri ght Law in
Cybers p ace ," C a rd ozo Arts and En tert a i n m ent Law Jou rn a l 14 (1996): 2 1 5 ; in "Copyri ght Law
and Social Di a l dialogue on the In form a ti on Su superhighway i ghw ay: The Case Against Copyri ght Liabi li ty of Bu ll etin Boa rd Opera tors" (C a rd ozo Arts and En tert a i n m ent Law Jou rn a l 13 [1995]:
3 4 5 ,3 9 0 – 9 9 ) ,E l k i n - Koren analy zes the probl ems cre a ted by app lying copyri ght law in a digi ti zed envi ron m en t . In "G ood bye to All That–A Relu reluctant (and Perhaps Prem a tu re) Ad i eu to
a Con s ti tuti on a lly Gro u n ded Di s co u rse of Pu blic In terest in Copyri ght Law " (Va n d Vanderbilt l t
Jou rnal of Tra n s n a tional Law 29 [1996]: 5 9 5 ) , Peter A . Jaszi advoc a tes the devel opm ent of
n ew, po l i c y - gro u n ded arguments and con s ti tuti on a lly based re a s oning to battle ex p a n s i expansionist legi s l a tive and judicial ten dencies in copyri ght to diminish public access to the " i n tell ectual com m on s" ;s ee also Peter A . Ja s z i , "On the Aut h or Effect : Con tem pora ry Copyri ght and
Co ll ective Cre a creativity ty," C a rd ozo Arts and En tert a i n m ent Law Jou rn a l 10 (1992): 2 9 3 , 3 1 9 – 2 0 ;
Peter A . Ja s z i , "Tow a rd a Th eory of Copyri gh t : The Met a m metamorphoses of 'Aut h ors h i p,' " Du ke
Law Jou rnal 1991 (1991): 4 5 5 . On the misuse of copyri gh t , s ee Lem l ey, " Beyond Preem pti on" ; Ma rk A . Lem l ey, "The Econ omics of Im improvement ent in In tell ectual Property Law," Texa s
Law Revi ew 75 (1997): 9 8 9 , 1 0 4 8 – 6 8 ; in " In tell ectual Property and Shri n k - wrap Licen s e s"
(S ou t h ern Califo rnia Law Revi ew 68 [1995]: 1 2 3 9 , 1 2 3 9 ) , Lem l ey notes that "s of t w a re ven-

2 7 0

dors are attem pting en masse to 'opt out' of i n tell ectual property law by dra f ting license provi s i ons that com pel their custom ers to ad h ere to more re s tri ctive provi s i ons than copyri gh t
. . . l aw would requ i re ." Jessica Litman ("The Tales That Arti cle 2B Tell s ," Berkel ey Te ch n ol o gy
Law Jou rn a l 13 [1998]: 9 3 1 , 938) ch a racteri zes as "du bi o u s" the noti on that current law ena bles publ i s h ers to make a tra n s acti on into a license by so de s i gn a ting it. In her vi ew, a rti cl e
2B is "confusing and con f u s ed "a bo ut copyri ght and its rel a ti onship with that law, and wo u l d
m a ke new law. She bel i eves that " wh a tever the outcom e" of the deb a te over wh et h er copyri ght makes sense in the digital envi ron m ent (see " Reforming In form a ti on Law in Copyri gh t's Im a ge ," Dayton Law Revi ew 22 [1997]: 5 8 7 ,5 9 0 ) , "copyri ght doctrine is ill - ad a pted to
accom m od a te many of the important interests that inform our inform a ti on po l i c y. F i rs t
Am en d m en t , privac y, and distri buti onal issues that copyri ght has tre a ted on ly gl a n c i n gly are
cen tral to any inform a ti on po l i c y." See also Jessica Litm a n ," Revising Copyri ght Law for the
In form a ti on Age ," O regon Law Revi ew 75 (1996): 1 9 ; and "The Exclu s ive Ri ght to Re ad "
(C a rd ozo Arts and En tert a i n m ent Law Jou rnal 13 [1994]: 2 9 ,4 8 ) , in wh i ch Litman states that
"mu ch of the activi ty on the net takes place on the mistaken assu m pti on that any materi a l
on the In tern et is free from copyri ght unless ex pre s s ly decl a red to be otherwi s e ." In "Copyri ght as Myt h" (Un ivers i ty of Pi t t s bu rgh Law Revi ew 53 [1991]: 2 3 5 , 2 3 5 – 3 7 ) , L i Litman provi des a gen eral overvi ew of the issues of a ut h orship and infringement n gem ent in copyri ght law,
i n d i c a ting that deb a te con ti nues rega rding the defin i ti on of "a ut h ors h i p" (she defines "a ut h or " "in the copyri ght sense of a nyone who cre a tes copyri gh t a ble work s , wh et h er they be
boo k s ,s on gs , s c u l ptu re s , bu i l d i n gs , com p uter progra m s , p a i n ti n gs or fil m s" [ 2 3 6 ,n . 5 ] ) ; s h e
also discusses why copyri ght law is co u n teri n tu i tive to the aut h orship proce s s . See also "Th e
Pu blic Dom a i n" (Em o ry Law Jou rn a l 39 [1990]: 9 6 5 , 9 6 9 ) , in wh i ch Litman recom m ends a
broad defin i ti on of the public domain ("ori gi n a l i ty is a keys tone of copyri ght law " [ 9 7 4 ] ) .
Neil Wei n s Weinstock Net a n el, "As s asserting Copyri gh t's Dem oc ra tic Principles in the Global Aren a ,"
Va n d erbilt Law Revi ew 51 (1998): 2 1 7 , 232 n.48, 299 n.322; Neil Net a n el , "Al i en a bi l i ty Res tri cti ons and the Enhancement ent of Aut h or Auton omy in Un i ted States and Con ti n en t a l
Copyri ght Law," C a rd ozo Arts and En tert a i n m ent Law Jou rnal 12 (1994): 1 , 4 2 – 4 3 ; i n
" [ C ] Copyright ght and a Dem oc ra tic Civil Soc i ety " (Yale Law Jou rn a l 106 [1996]: 2 8 3 , 2 8 8 ,
3 2 4 – 3 6 ) , Net a n el analy zes copyri ght law and policy in terms of its dem oc rac y - en h a n c i n g
f u n cti on : "Copyri ght is in essen ce a state measu re that uses market insti tuti ons to en h a n ce
the dem oc ra tic ch a racter of s oc i ety." Ma r ga ret Jane Radin and Polk Wa gn er, "The Myth of
Priva te Ordering n g : Red i s covering Legal Realism in Cybers p ace ," C h i c a go - Kent Law Revi ew 7 3
( 1 9 9 8 ) ; Ma r ga ret Jane Rad i n , Rei n terpreting Property ( Ch i c a go : Un ivers i ty of Ch i c a go Pre s s ,
1 9 9 3 ) ,5 6 – 6 3 . Pam Sa mu el s on ," E n coding the Law into Di gital Libra ri e s ," Co m mu n i c a tions of
the AC M 41 (1999): 1 3 , 1 3 – 1 4 ; Pa m ela Sa mu el s on, foreword to "Sym po s iu m : In tell ectu a l
Property and Con tract Law for the In form a ti on Age ," C a l i fo rnia Law Revi ew 87 (1998): 1 ;
Pa m ela Sa mu el s on ob s erves in " E m bedding Technical Sel f - Help in Licen s ed Sof t w a re"
(Co m mu n i c a tions of the AC M 40 [1997]: 1 3 , 16) that "l i cen s ors of s of t w a re or other inform a ti on . . . wi ll gen era lly invo ke sel f - h el p" ; s ee also the cri ticism of the Eu ropean database
d i rective in J. H . Rei Reichman and Pa m ela Sa mu el s on ," In tell ectual Property Ri ghts in Data?,"
Va n d erbilt Law Revi ew 50 (1997): 5 1 ,8 4 – 9 5 ; Sa mu el s on , "The Copyri ght Gra b," 1 3 4 ; Pa m el a
Sa mu el s on ," Fair Use for Com p uter Programs and Ot h er Copyri gh t a ble Works in Di gi t a l
Form : The Im p l i c a ti ons of Sony, G a l oob and Sega ," Jou rnal of In tell e ctual Property Law 1
( 1 9 9 3 ) : 4 9 .

69. For a recent and compelling account of the general movement to propertize informati on , s ee Debora J. Ha l bert , In tell e ctual Property in the In fo rm a tion Age: The Pol i ti cs of Ex -
Expanding Own ership Ri gh t s (We s Westport , Con n . : Q u oru m , 1 9 9 9 ) . Seth Shu l m a n's Owning the
Future (Boston: Houghton Mifflin,1999) gives the story its appropriate drama.

70. "We favor a move away from the author vision in two directions; first towards recogn i ti on of a limited nu m ber of n ew pro tecti ons for cultu ral heri t a ge , fo l k l oric produ cti on s ,
and bi o l ogical 'k n ow - h ow.' Secon d , and in gen era l , we favor an incre a s ed recogn i ti on and

2 7 1

protection of the public domain by means of expansive 'fair use protections,' compulsory licensing, and narrower initial coverage of property rights in the first place"; Boyle, Shamans,
Software,and Spleens, 169.

7 1 . James Boyl e , "A Po l i tics of In tell ectual Property: E nvi ron m entalism for the Net ? ,"

Duke Law Journal 47 (1997): 87.

C H A P T E R E L E V E N

1. For a comprehensive account of the American protections for privacy, as well as a comparison with European protections,see Peter P. Swire and Robert E.Litan, None of Your Busi -
ness: Wo rld Data Flows , E l e ctronic Co m m erce , and the Eu ropean Privacy Di re ctive
(Washington, D.C.: Brookings Institution Press, 1998).I have drawn from Phil Agre historical framing of the question in "Beyond the Mirror World: Privacy and the Representational
Practices of Computing" (in Technology and P rivacy: The New Landscape, edited by Philip E.
Agre and Marc Rotenberg [Cambridge, Mass.:MIT Press,1997],29) in building the argument
of this chapter.

2. MIT Professor Hal Abelson,interview with the author, Newton, Mass., May 29,1999.
3. Swisher cites an estimate that AOL earned $7 million per month in the spring of 1996

from sex chat; Aol.com, 226.

4. See M. Ethan Katsh, Law in a Digital World (New York: Oxford University Press,1995),

228.

5 . Obvi o u s ly, this con cern is not new. Alan We s ti n's work in the early 1970s was fo u n d ati onal in raising aw a Awareness abo ut the rel a ti onship bet ween com p uters and privac y; s ee Alan F.
We s tin and Mi ch ael A . Ba ker, Da t a banks in a Free Soci ety ( New York :Q u ad ra n gle Boo k s ,1 9 7 2 ) .

6. See Olmstead v United States, 277 US 438 (1928).
7 . For a com preh en s ive tre a tm ent of the legal issues ra i s ed by cases of su rvei ll a n ce , s ee
Christopher Slobogin, "Technologically Assisted Physical Surveillance: The American Bar Association's Tentative Draft Standards," Harvard Journal of Law and Technology 10 (1997): 383.
8. Communication attributes can be defined as "encompass[ing] all of the other informati on that can be learn ed abo ut a com mu n i c a ti on , su ch as wh en and wh ere it occ u rred , to
whom and fr om whom it was sent and how long it lasted"; Susan Freiwald,"Uncertain Privac y: Com mu n i c a ti on At tri butes Af ter the Di gital Tel eph ony Act ," S ou t h ern Califo rnia Law
Review 69 (1996):949,951. Freiwald argues that new technology has increased the amount of
communication attributes that can be stored and retrieved,thus rendering this data highly informative and extremely intrusive (951–52).

9. For instance, USA Today reported in "The Hunt for bin Laden" (August 21, 1998,A1)
that "the supersecret National Agency in Fort Meade, Md.,uses computers to scan tapped intern a ti onal ph one call s" ; s ee also "Ca s h - a n d - Ca rry Di p l om ac y " (Ti m e , Febru a ry 24, 1 9 9 7 ,
22ff.), which mentions that the National Security Agency monitors communications like international phone calls and electronic messages.

1 0 . Lew Platt, key n o te ad d ress at S pring In tern et World '98, Ma rch 11, 1 9 9 8 , ava i l a ble at
h t tp : / / w w w. h p. com / fin a n c i a l s / tex ton ly / pers on n el / ceo / key n o te 9 8 . h tml (vi s i ted May 30, 1 9 9 9 ) .
D avid Brin reports that Kodak can do the same in fif ty byte s ; The Tra n s pa rent Soci ety, 2 4 1 .

11. Michael Kemp, "Centurion to Fight Crooks; 'Thinking' Spy Camera Could Put an End
to Car Crimes," Daily Mail (London), May 20,1995, 49; "Centurion" is a "real-time recogniti on and iden ti f i c a ti on of nu m ber plates sys tem" that "a ll ows com p a ri s on of l i License plate s
with user databases."

12. See, for example,the reports in George Cole, "Smart Building Looks Sharp" (Financial
Times [London], November 2, 1995,14), on a Japanese company that uses a video camera license plate scanner to control access to a garage and image-processing technology in the staff
cafeteria in conjunction with an automatic till operator; in Bill Dawson,"Polluters Beware:

2 7 2

Laser to Pick Out Foulest Tailpipes; Thousands of Commuters' Cars Will Be Checked As They
Pass By" (Houston Chronicle, October 6,1998,A1), on a new Houston program to catch "gross
po Polluters" using a com bi n a ti on of l a s er tech n o l ogy and vi deo camera s ; in Tom God f rey,
"Canada Customs to Border on Hi-Tech" (Toronto Sun, July 20,1997, 16), on an experimental sys tem being te s ted by Ca n Canadian customs to autom a te border cro s s i n gs by using voi ce
recognition, fingerprint and eye scanners,and real-time video cameras and license plate readers; and in Alex Salkever, "Too Many Unse en Cameras?" (Christian Science Monitor, June 5,
1998, 1), on Honolulu's installation of "video cameras at key points along a main thoroughfare to help catch petty thieves and prevent prostitution."

13. See Center for Democracy and Technology, "Filing Before the FCC in the Matter of
the Communications Assistance for Law Enforcement Act,CC docket no. 97–213," December
14,1998,http://www.cdt.org//digi_tele/filing121498.html.

1 4 . See Mi n n e sota v Di ckerso n , 508 US 366, 381 (1993) (Ju s ti ce An tonin Scalia con c u rring).

15. See, for example, William J. Stuntz,"Privacy's Problem and the Law of Criminal Procedure," Michigan Law Review 93 (1995):1016,1026;in "The Substantive Origins of Criminal
Procedure," Stuntz discusses the origins of the Fourth Amendment.

16.Stuntz,"Privacy's Problem and the Law of Criminal Procedure," 1026.
1 7 . Al i en and Sed i ti on Acts of 1 7 9 8 , Act of June 18, 1 7 9 8 , ch .5 9 , 1 Stat. 566 (repe a l ed 1802),
Act of June 25, 1 7 9 8 , ch .6 3 , 1 Stat. 570 (ex p i red ) ; Act of Ju ly 6, 1 7 9 8 , ch .7 0 , 1 Stat. 577 (ex p i red ) ,
Act of Ju ly 14, 1 7 9 8 , ch .7 7 , 1 Stat. 596 (em powering the pre s i dent to deport anyone he deem s
d a n gerous to the co u n try 's pe ace and safety) (ex p i red ) . The Al i en and Sed i ti on Acts were decl a red uncon s ti tuti onal in New Yo rk Times Co. v Su ll iva n , 376 US 254, 276 (1964), t h o u gh , of
co u rs e , by then their terms they had ex p i red . See Neal Devi n s , Co n s ti tu tional Va l u e s ( Ba l ti m ore :
Johns Hopkins Un ivers i ty Pre s s ,1 9 9 6 ) , on overruling (13); and James Morton Sm i t h , Fre ed o m's
Fet ters: The Al i en and Sed i tion Laws and Am erican Civil Li berti e s ( It h ac a ,N . Y. : Corn ell Un ivers i ty Pre s s ,1 9 5 6 ) , on the history, en forcem en t , and impact of the Al i en and Sed i ti on Act s .

18. Stuntz, "Substantive Origins,"395.
19. See Cass R. Sunstein,"Incompletely Theorized Agreements," Harvard Law Review 108
(1995): 1733, 1735–36."Participants in legal controversies," Sunstein observes, ". . . need not
a gree on fundamental pri n c i p l e . . . . Wh en they disagree on an Abstraction on , t h ey move to a
l Level of gre a ter parti c u l a ri ty. The disti n ctive fe a tu re of this account is that it em ph a s i ze s
agreement on (relative) particulars rather than on (relative) abstractions."

20. There is a growing literature that is rethinking the implications of that choice.David
Brin The Transparent Society is among the most arresting; he argues for a fundamental shift
in our conception of privacy (see my discussion of Brin in chapter 10). Amitai Etzioni's The
Limits of Privacy (New York: Basic Books,1999) is closer to the ground, working through the
balance that privacy choices demand. Although I have problems with some of the specifics in
Etzioni's account, his method is right, and some of his conclusions (in particular about the
use of data by commercial entities) are extremely strong. The great strength of the book,however, is that it en ga ges these qu e s ti ons of va lue from a con tem pora ry pers pective . I do not
have much of a taste for the communitarianism in his account, but the value in such a work
is its power to generate argument.

2 1 . The law thinks abo ut it as a qu e s ti on of " i n form a ti on privac y." The Con s ti tuti on has
very little time for the ide a ; s ee Al bert W. Al s chu l er, " In Interpersonal onal Privacy and the Fo u rt h
Am en d m en t ," No rt h ern Illinois Un ivers i ty Law Revi ew 4 (1983): 1 ; s ee also Pri s c i lla M. Rega n ,
Legi s l a ting Priva c y: Te ch n ol o gy, S o cial Va l u e s , and Pu blic Pol i c y ( Ch a pel Hi ll : Un ivers i ty of Nort h
Ca Carolina Pre s s ,1 9 9 5 ) :6 9 – 1 0 8 ; Paul M. S chw a rt z ," Privacy and Pa rti c i p a ti on : Pers onal In form ati on and Pu blic Sector Reg u l a ti on in the Un i ted State s ," Iowa Law Revi ew 80 (1995): 5 5 3 .

22. And they do not come from Janna Malamud Smith's "fallacy of perspective," discussed
by David Brin (The Transparent Society, 68–70). My argument is not that privacy thrived in
the past; it is that privacy was different in the past, and that the construction of searchable

2 7 3

databases constitutes a different sort of threat. We might approach the community of the past
if we adopted a policy of forgetfulness,as Brin explores (247–48). Purging records might well
be a key to a certain kind of liberation.

2 3 . See Gandy, The Pa n optic Sort , 6 6 – 6 8 . In su pport of the theory that co ll Collectors of vo lu nt a ri ly given data can do wh a tever they like with that data, s ome have argued that the pri m a ry
con s ti tuti onal issue is free speech ra t h er than privac y; on ce inform a ti on is freely rel e a s ed , a ny
re s tri cti ons on corpora te speech , su ch as custom er lists, should be disfavored (107).

24. Ibid.,87–90. For example,a targeting system that classified neighborhoods according
to thirty - four different de s c ri Descriptors that acco u n ted for 87 percent of the va ri a n ce in soc i Socioeconomic omic levels ac ross nei gh borh oods was hu Hugely su ccessful with cl i ents su ch as News we e k
and Colgate-Palmolive (88).

25. Peter H. Lewis,"Forget Big Brother," New York Times, March 19,1998,G1.
26. Brin, The Transparent Society, 8–15.
27. For a good story that effectively summarizes the state of Web advertising, and for a
discussion of how DoubleClick operates and the case study of 3M's sale of projectors through
the advertising placem ent com p a ny, s ee Zina Mo u k h ei ber, "Do u bl e Cl i ck Is Wa watching Yo u ,"
Forbes (November 4, 1996): 342; see also http://www.alexa.c om (visit ed May 30, 1999); and
http://www.spinner.com (visited May 30,1999). Spinner asks you to rate music as you listen
to it (à la Firefly),and Alexa is like DoubleClick but has not caused any of the similar uproar
over privacy. When a user downloads Alexa,it monitors every site (not just ones that display
a certain type of ad) that the user visits.

2 8 . See Federal Trade Com m i s s i on , " Privacy Online: A Report to Con gre s s ," June 1998,

n.107, available at http://www.ftc.gov/reports/privacy3/toc.htm (visited May 30,1999).

29. See Gandy, The Panoptic Sort, 1–3.
3 0 . Jo h n s on , In terf a ce Cu l tu re , 1 9 2 – 2 0 5 . An d rew Shapiro calls this the "feed b ack ef fect"

but argues that it nar rows the range of choices; see The Control Revolution, 113.

31. See, for example, McIntyre v Ohio Elections Commission, 514 US 334,341–43 (1995).
3 2 . See Janai S. Nel s on , " Re s i den tial Zoning Reg u l a ti ons and the Perpetu a ti on of

Apartheid," UCLA Law Review 43 (1996): 1689,1693–1704.

33. Examples of laws that aim at segregation based on social or economic criteria include:
regulations requiring a minimum lot size for housing; single-family ordinances prohibiting
"nontraditional" families from living in certain areas; and residential classifications that exclude apar tment housing . All such rest restrictions significantly increase the cost of housing for
lower-income individuals;see ibid.,1699–1700.

34. In 1926 the Supreme Court held zoning to be a valid exercise of local governmental
power. See Village of Euclid v Ambler Realty Company, 272 US 365 (1926) (holding that a state
has the right to separate incompatible uses). Not until the twentieth century were municipalities given much power to regulate areas of law such as zoning decisions;see Richard Briffault,
"Our Localism: Part I—The Structure of Local Government Law," Columbia Law Review 90
(1990):1,8–11, 19.

35. In 1917 the Supreme Court outlawed racial zoning as a violation of the Fourteenth
Amendment; see Buchanan v Warley, 245 US 60 (1917). However, "non exclusionary" zoning
reg u l a ti on was used to pre s erve re s i den tial segrega ti on ; even though fac i a lly neutral and
based on economic factors (ostensibly to prevent property devaluation), various laws and regulations have resulted in de facto segregation; see Briffault, "Our Localism," 103–4; Meredith
Lee Bryant, "Combating School Resegregation Through Housing: A Need for a R reconceptualization of American Democracy and the Rights It Protects," Harvard BlackLetter Journal 13
(1997): 127, 131–32.

3 6 . See Joel Ko s m a n , "Tow a rd an In clu s i on a ry Ju ri s pru den ce : A Recon ceptu a l i z a ti on of

Zoning," Catholic University Law Review 43 (1993): 59,77–86, 101–3.

37. See Gordon S. Wood, The Radicalism of the American Revolution (New York: Alfred A.

Knopf,1992),5–8, 271–86.

2 7 4

38. See Lynne G. Zucker, "Production of Trust: Institutional Sources of Economic Structure,1840–1920," Research in Organizational Behavior 8 (1986): 53.

3 9 . Pri ce discri m i n a ti on is the abi l i ty to ch a r ge different pri ces for the same good . Ai Airplane ti tickets are the best example—the same seat can cost hu n d reds of do ll a rs more for a
traveler who cannot stay over Saturday night. See, for example, Joseph Gregory Sidak,"Debunking Pred a tory In n ova ti on ," Col u m bia Law Revi ew 83 (1983): 1 1 2 1 , 1 1 3 2 – 3 5 ; s ee also
E a s terbroo k ," In tell ectual Property Is Sti ll Property " ; F i s h er, " Recon s tru cting the Fair Us e
Doctrine," 1659; but see Janusz A. Ordover et al.,"Predatory Systems Rivalry: A Reply," Co -
Columbia Law Review 83 (1983):1150,1158–64.

4 0 . Viviana A . Zel i zer, The Social Meaning of Mo n ey, 2d ed . ( Pri n ceton , N . J. : Pri n ceton

University Press,1994), 94–95 (footnote omitted).

41. It is quite clear that the government's data encryption standard (DES) is unreliable.
The Electronic Frontier Foundation (EFF), to its great credit,has made it that way. In Crack -
ing DES: Secrets of Encryption Research, Wiretap Politics, and Chip Design, EFF provides the
code and plans to build a machine that can crack a DES key. As Whitfield Diffie, one of the inventors of public key encryption, writes, "With the appearance of this book and the machine
it represents, the game changes forever. It is not a question of whether DES keys can be extracted by ex h a u s tive search ; it is a qu e s ti on of h ow ch e a p ly they can be ex tracted and for
what purposes" (xi). Other standards are increasingly available,and if the move to lib liberalize
the reg u l a ti on of en c rypti on su cceed s , powerful en c rypti on tech n o l ogies wi ll be gen era lly
available (both in the United States and abroad) soon; see Cryptography's Role in Securing the
Information Society, edited by Kenneth W. Dam and Herbert S. Lin (Washington, D.C.: Nati onal Ac Academy Pre s s , 1 9 9 6 ) . For a discussion of com p uting tech n o l ogies that might well
make these "safer" key systems unsafe (including DNA and quantum computing), see B rin,
The Transparent Society, 280–82.

42. For a discussion o f the law governing compelled disclosure of keys and plaintext, see
Phillip R. Reitinger, "Compelled Production of Plaintext and Keys," University of Chicago Le -
gal Forum 1996 (1996): 171.

4 3 . See Mi ch ael Adl er, "Cybers p ace , G en eral Se a rch e s , and Di gital Con tra b a n d : Th e
Fourth Amendment and the Net-Wide Search," Yale Law Journal 105 (1996): 1093, 1109–10,
1113.

44. Cf.ibid.,1100;see also Brin, The Transparent Society, 158–61 (discussing mutual monitoring).

45. Cf. Froomkin, "The Metaphor Is the Key."
46. See Joel R. Reidenberg, "Privacy in the Information Economy: A Fortress or Frontier
for In d ivi dual Ri gh t s ? ," Fed eral Co m mu n i c a tions Law Jou rn a l 44 (1992): 1 9 5 , 2 3 7 – 3 8 . Th e
principles account for concern that "the privacy concerns of data collection (including notice,
consent, necessity, and accuracy),uses (including associated uses), and the duration of storage require careful consideration" (238, footnotes omitted).

47. For example,the Video Privacy Protection Act (18 USC, § 2701 [1988]) was adopted
in response to outrage over the media's acquisition of a list of films rented by Judge Robert
Bork at the time of his ill-fated nomination to the Supreme Court.

4 8 . One high ly to uted sys tem has been TRU S Te . Wh en a web site becomes licen s ed by
T RU S Te , it has agreed to disclose its inform a ti on - ga t h ering and dissemination i n a ti on practi ce s
(which can be brought up by clicking on the "trustmark") and pledged that the disclosure is
backed by third-party assurance; see TRUSTe,"Building a Site You Can Believe In," available
at http://www.etrust.org (visited May 30,1999).

49. See Joseph M. Reagle and Lorrie Faith Cranor, "The Platform for Privacy Preferences,"

Communications of the ACM (February 1999): 48.

50. See ibid.
5 1 . Jo s eph M. Re a gle Jr. , "P3P and Privacy on the Web FAQ , Vers i on 2.0.1," ava i l a ble at

http://www.w3.org/P3P/P3FAQ.html (visited May 30, 1999).

2 7 5

52. In its current design, the protocol is fairly unwieldy. It also lacks encryption, leaving
u s er data open to interception on ; s ee Ken n eth Lee and Gabriel el Speyer, " P l a tform for Privac y
Preferen ces Proj ect and Ci ti b a n k" ( 1 9 9 8 ) , ava i l a ble at Ci tibank Adva n ced Devel opm en t
Group, "White Paper: Platform for Privacy Preferences Project (P3P) and Citibank" (October
22, 1998), http://www13.w3.org/P3P/Lee_Speyer.html (visited May 30, 1999). The most significant challenge,however, will simply be in implementation. If applications implement P3P
in a way that facilitates simple user control,it could be successful. For a balanced and powerful account of the value of standardized data models,see Agre and Rotenberg, Technology and
Privacy.

5 3 . See Gu i do Ca l a calabresi and A . Do u glas Mel a m ed ," Property Ru l e s ,L i a bi l i ty Ru l e s , a n d
In a l i en a bi l i ty: One Vi ew of the Ca t h ed ra l ," Ha rva rd Law Revi ew 85 (1972): 1 0 8 9 , 1 1 0 5 – 6 .
" Property rules invo lve a co ll ective dec i s i on as to who is to be given an initial en ti t l em en t
but not as to the va lue of the en ti t l em en t . . . . L i a bi l i ty rules invo lve an ad d i ti onal stage of
s t a te interven ti on : not on ly are en ti t l em ents pro tected , but their tra n s fer or de s tru cti on is
a ll owed on the basis of a va lue determ i n ed by some or gan of the state ra t h er than by the
p a rties them s elve s" ( 1 0 9 2 ) . An d rew Shapiro discusses a similar idea in The Co n trol Revol u -
ti o n , 1 5 8 – 6 5 .

54. Cf. Margaret Jane Radin, Contested Commodities (Cambridge, Mass.: Harvard Univers i ty Pre s s , 1 9 9 6 ) ; Ma rtha Nu s s b a u m , "Ari s to Aristotelian Social Dem oc rac y," in Li liberalism and the
Good, edited by R. Bruce Douglass et al.(New York: Routledge,1990),232.

55.Cf. Margaret Jane Radin,"Property Evolving in Cyberspace," Journal of Law and Com -

munications 15 (1996): 509,524–26.

5 6 . See " Privacy Now Ca m p a i gn ," ava i l a ble at http : / / w w w. ef f . or g / go l d key. h tml (vi s i ted

May 30,1999).

5 7 . See Ma rc Ro ten ber g, "Data Pro tecti on in the Un i ted State s : A Rising Ti de ? ," s peech
given at the Nineteenth International Conference of Privacy Data Protection Commissioners,
Bru s s el s , Septem ber 17–19, 1 9 9 7 , ava i l a ble at http : / / w w w. privac y. fgov. be / con feren ce /
pt1_3.html (visited May 30,1999).

58. Cf. Breyer, "The Uneasy Case for Copyright."
59. John Perry Barlow, "The Economy of Ideas," Wired (March 1994), available online at

http://www.wired.com/wired/archive/2.03/economy.ideas.html.

C H A P T E R T W E L V E

1 . Two excell ent examples inclu de Owen M. F i s s , The Iro ny of Free Spe e ch ( Ca m bri d ge ,
Mass.: Harvard University Press, 1996); and Cass R. Sunstein, Democracy and the Problem of
Free Speech (New York: Free Press,1993).

2 . See 47 CFR § 73.658(e) (1998); s ee also Herbert J. Ro Rothfeld et al., "Tel evi s i on Stati on

Standards for Acceptable Advertising," Journal of Consumer Affairs 24 (1990): 392.

3 . See Stra fge s et z bu ch (penal code) (StGB) §§ 130–31, repri n ted in German Cri m i n a l
Law, vol.1, edited by Gerold Harfst, translated by Otto A.Schmidt (Würzburg: Harfst Verlag,
1989),75–76.

4. Built by industry but also especially by Cypherpunks—coders dedicated to building the
tools f or privacy f or the Internet. As Eric Hughes writes in "A Cypherpunk's Manifesto" (in
Appl i ed Crypto gra p hy, 2d ed . , by Bru ce Sch n ei er [New York : Wi l ey, 1 9 9 6 ] , 6 0 9 ) : We the
Cyph erpunks are ded i c a ted to building anonymous sys tem s . We are defending our privac y
with cryptogra phy, with anonymous mail forw a rding sys tem s , with digital sign a tu re s , a n d
with electronic money. Cypherpunks write code. We know that someone has to write software
to defend privacy, and since we can't get privacy unless we all do, we're going to write it. We
publish our code so that our fellow Cypherpunks may practice and play with it. Our code is
free for all to use, worldwide.

2 7 6

5 . John Perry Ba rl ow has put into circ u l a ti on the meme that, "in cybers p ace , the Firs t
Am en d m ent
local ord i n a n ce" ; " Le aving the Physical Worl d ," ava i l a ble at
h t tp : / / w w w. ef f . or g / p u b / Pu bl i c a ti on s / Jo h n _ Perry _ Ba rl ow / l e avi n g _ t h e _ phys i c a l _ worl d . a rti cl e
(visited May 30,1999).

is a

6 . See David Ru den s ti n e , The Day the Pre s ses Stopped: A Hi s to ry of the Pen t a gon Pa pers

Case (Berkeley: University of California Press,1996),101, 139.

7. Ibid.,100.
8. See ibid.,2.
9. See ibid.,2,42.
10. Ibid.,47–63.
11. Sanford J. Ungar, The Papers and the Papers: An Account of the Legal and Political Bat -
tle over the Pen t a gon Pa pers ( New York : Co lu m bia Un ivers i ty Pre s s , 1 9 8 9 ) , 1 2 0 ; c i ted in
Rudenstine, The Day the Presses Stopped, 92.

12. See ibid., 105.
13. Near v Minnesota ota, 283 US 697, 716 (1931); cf. United States v Noriega, 917 F2d 1543
(11th Cir 1990) (affirming the prior restraint of audiotapes of the defendant's conversations
with his attorney on the grounds that they might impede his right to a fair trial), cert. denied,
498 US 976 (1990) ( Justice Thurgood Marshall dissenting).

14. See, for example, Organization for a B etter Austin v Keefe, 402 US 415,418–19 (1971);
Bantam Books, Inc.,v Sullivan, 372 US 58,70 (1963); Near v Minnesota, 283 US 697, 713–14.
1 5 . The standard arguments are su m m a ri zed well by Ka t h l een M. Su ll ivan and Gerald l d
Gu n t h er: "(1) It is easier for an official to re s tri ct speech 'by a simple stro ke of the pen' t h a n
by the more cumbers ome app a ra tus of su b s equ ent punishmen t . . . . (2) Cen s ors wi ll have
a profe s s i onal bias in favor of cen s ors h i p, and thus wi ll sys tem a ti c a lly overvalue lue governm ent interests and undervalue lue speech . (3) Cen s ors opera te more inform a lly than ju d ge s
and so afford less procedu ral safeguards u a rds to spe a kers . (4) Speech su ppre s s ed in adva n ce
n ever re aches the marketplace l ace of i deas at all . (5) Wh en speech is su ppre s s ed in adva n ce ,
t h ere is no em p i rical evi den ce from wh i ch to measu re its all eged likely harm s" ; Firs t
Am en d m ent Law ( New York : Fo u n d a ti on Pre s s , 1 9 9 9 ) , 3 3 9 – 4 0 , c i ting Th omas Emerson on ,
"The Doctrine of Pri or Re s tra i n t ," Law and Co n tem po ra ry Probl em s 20 (1955): 6 4 8 . Frederick ck Sch a u er of fers a nice balance to this com m on p l ace theory; s ee " Fe a r, Ri s k , and the Firs t
Am en d m en t : Un raveling the 'Ch i lling Effect ,' " Bo s ton Un ivers i ty Law Revi ew 5 8 ( 1 9 7 8 ) :
6 8 5 , 7 2 5 – 3 0 .

16. In a particularly telling exchange, Justice Stewart asked Professor Bickel about a case
in which disclosure "would result in the sentencing to death of a hundred young men whose
on ly of fense had been that they were nineteen ye a rs old and had low draft nu m bers . Wh a t
should we do ? " Bi ckel rep l i ed that his " i n cl i n a ti ons of hu m a n i ty overcome the som ewh a t
m ore abstract devo ti on to the First Am en d m ent in a case of that sort" ; May It Pl e a se the
Court: The Most Significant Oral Arguments Made Before the Supreme Court Since 1955, edited
by Peter Irons and Stephanie Guitton (New York: Free Press,1993),173.

17. In a c concurring opinion, Justice Potter Stewart wrote that the prior restraint at issue
was invalid since he could not "say that disclosure of [the Pentagon Papers] will surely result
in direct, immediate, and ir reparable damage to our Nation or its people"; New York Times
Company v United States, 403 US 713,730 (1971) (per curiam). This standard has frequently
been thought to r reflect the position of the Court; see Laurence H. Tribe, American Constitu -
tional Law (Meneola,N.Y.: Foundation Press,1978), 731; Morton H. Halperin and Daniel N.
Hof f m a n , Top Secret: Na tional Security ty and the Ri ght to Kn ow (Wa s h i n g ton , D. C . : New Republic Books, 1977),147 n.22; see also Alderman v Philadelphia Housing Authority, 496 F2d
164,170 (3d Cir 1974), cert. denied,419 US 844 (1974) (prior restraint must be supported by
"compelling proof " that it is "essential to a vital government interest").

2 7 7

18. See United States v Progressive, Inc., 467 FSupp 990 (WDWis 1979);see also L.A. Powe

Jr.,"The H-Bomb Injunction," University of Colorado Law Review 61 (1990): 55,56.

19. The Milwaukee Sentinel and Fusion magazine had published articles dealing with similar concepts; see A. DeVolpi et al., Born Sec ret: The H-Bomb, The P rogressive Case, and Na -
tional Security y (New York: Pergamon Press, 1981), 102, 106; see also Howard Morland, The
Secret That Exploded (New York: Random House, 1981),223,225–26.

2 0 . See Floyd Abra m s , "F i rst Am en d m ent Po s tc a rds from the Edge of Cybers p ace ," St .

John's Journal of Legal Commentary 11 (1996): 693,699.

21. NTSB Chairman Jim Hall announced later that investigations confirmed that a fuel
tank explosion caused the crash; see "Statement of Jim Hall, Chairman, National Transportation Safety Board," July 16, 1998, available at http://www.ntsb.gov/pressrel/980716.htm (visited May 30, 1999).

22. See Robert E. Kessler, "TWA Probe: Submarines off Long Island/Sources: But No Link

to Crash of Jetliner," Newsday, March 22,1997,A8.

2 3 . See , for ex a m p l e , James Sa n ders , The Downing of TWA Flight 800 ( New York : Ken si n g ton Pu bl i s h i n g, 1 9 9 7 ) , 1 3 1 – 3 7 ; Acc u racy in Media et al., "TWA 800—Missile Web s i te
Road m a p," ava i l a ble at http : / / w w w. a n gel f i re . com / h i / TWA800/ (vi s i ted May 30, 1 9 9 9 ) ;
Ma rk K. An ders on , " Fri en dly Ire ," ava i l a ble at http : / / w w w. va ll eyadvoc a te . com / a rti cl e s
/ t w a 3 . h tml (vi s i ted May 30, 1 9 9 9 ) ; Ian W. G od d a rd , "TWA Flight 800 and Facts Pert a i n i n g
to U. S . Navy Cu l p a bi l i ty," ava i l a ble at http : / / w w w. ero l s . com / i god d a rd / t w a - f act . h tm (vi s i ted
May 30, 1 9 9 9 ) .

2 4 . See Sa n ders , The Downing of TWA Flight 800, 2 9 – 3 0 , 7 5 ,7 0 – 7 9 , 1 7 1 – 7 3 .
25. We can tell that it is false, of course, as in, "The cat was alive and not alive."
26. Andrew Shapiro has a powerful analysis of a particularly smart loon; see The Control

Revolution, 133–41.

27. As Shapiro puts it, "What we need are trusted intermediaries: people to whom we entrust certain tasks because we recognize the value of their p erspective, their expertise, their
time,and their independence"; ibid.,188.

28. See Zucker, "Production of Trust," 63–65.
2 9 . Ob s cen i ty is not con s ti tuti on a lly pro tected speech , and federal laws pro h i bit the
tra n s port a ti on of ob s cene materi a l s ; s ee 18 USCA § 1462 (1984), a m en ded by 18 USCA
§1462 (Su pp 1999). In Mi ll er v Califo rn i a , the Su preme Co u rt de s c ri bed the test for obs cen i ty as: "(a) wh et h er 'the average ge pers on ,a pp lying con tem pora ry com mu n i ty standard s'
would find that the work ,t a ken as a wh o l e ,a ppeals to the pru ri ent intere s t ; (b) wh et h er the
work dep i cts or de s c ri be s , in a patently t ly of fen s ive way, s exual con du ct spec i f i c a lly def i n ed by
the app l i c a ble state law; and (c) wh et h er the work , t a ken as a wh o l e , l acks serious litera ry,
a rti s ti c , po l i ti c a l , or scien tific va lu e ; " Mi ll er v Califo rn i a , 413 US 15, 24 (1973) (5–4 dec is i on ) , reh e a ring den i ed , 414 US 881 (1973). Porn , on the other hand, is pro tected by the
F i rst Am en d m ent but may be reg u l a ted to prom o te the state's interest in pro tecting ch i ld ren from harmful materials so long as the reg u l a ti on is the least re s tri ctive means to furt h er the arti c u l a ted intere s t ; s ee G i n s berg v New Yo rk , 390 US 629, 637–40 (1968). Ch i l d
porn may be pro h i bi ted as ob s cene material even if it is not ob s cene under the Mi ll er te s t ,
owing to the strong state interest in preven ting the sexual ex p l oi t a ti on of ch i l d ren ;s ee New
Yo rk v Ferber, 458 US 747, 764 (1982). Child porn is not con s ti tuti on a lly pro tected , and federal law pro h i bits the tra n s port a ti on of child porn ; s ee 18 USCA § 2252 (1984), a m en ded
by 18 USCA §2252 (Su pp 1999).

30. Justice Sandra Day O'Connor listed more than forty states with such law in her concurrence in Reno v ACLU, 521 US 844,887 n.2.
31. Ginsberg v New York, 390 US 629 (1968).
32. See Godwin, CyberRights, 206–59.

2 7 8

33. See Blake T. Bilstad, "Obscenity and Indecency in a Digital Age: The Legal and Political Implications of Cybersmut, Virtual Pornography, and the Communications Decency Act
of 1996," Santa Clara Computer and High Technology Law Journal 13 (1997): 321,336–37.

34. Marty Rimm,"Marketing Pornography on the Information Superhighway: A Survey
of 917,410 Im a ge s , De s c ri pti on s , S h ort Stori e s , and An i m a ti ons Down l oaded 8.5 Mi ll i on
Times by Con su m ers in over 2,000 Ci ties in Forty Co u n tri e s , Provi n ce s , and Terri tori e s ,"
Georgetown University Law Journal 83 (1995):1849.Godwin provides the whole history of the
Rimm article, describing the most significant problems and consequences of the "misleading"
and "false" statements, and its eventual demise; CyberRights, 206–59; see also Jonathan Wallace and Mark Mangan, Sex, Laws, and Cyberspace (New York: M&T Books,1996), ch.6.

35. See Philip Elmer-DeWitt, "On a Screen Near You: Cyberporn—It's Popular, Pervasive,
and Surprisingly Perverse, According to the First Survey of Online Erotica—And There's No
Easy Way to Stamp It Out," Time, July 3,1995.
36. 47 USCA § 223(e)(5)(A) (Supp 1999).
37. The law was extinguished (at least in part) at 521 US 844 (1997); see Eugene Volokh,
" Freedom of S peech , S h i elding Ch i l d ren , and Tra n s cending Ba l a n c i n g," Su preme Cou rt Re -
view 1997 (1997):141.

38. See Federal Communications Commission v Pacifica Foundation, 438 US 726, 748–50
(1978) (plu ra l i ty ) . Th o u gh Pa ci fica has been cri ti c i zed stron gly, s ee Steven H. S h i f f ri n , T h e
First Am en d m en t , Dem o cra c y, and Ro m a n ce ( Ca m bri d ge , Ma s s . : Ha rva rd Un ivers i ty Pre s s ,
1990), 80, as Jonathan Weinberg convincingly argues, Pacifica continues to have influence in
the broadc a s ting con tex t ; "Ca ble TV, In decen c y, and the Co u rt ," Col u m bi a - V LA Jou rnal of
Law and the Arts 21 (1997): 95.

39. See Gentile v State Bar of Nevada, 501 US 1030,1048–51 (1991) (vague regulations of
speech are void owing to the impermissible risk of chilling speech); Dombrowski v Pfister, 380
US 479,494 (1965) (chilling speech).

40. For a more extensive discussion of this system, see Lawrence Lessig and Paul Resnick,
"The Architectures of Mandated Access Controls," Michigan Law Review (forthcoming, 1999).
41. 47 USC § 230 (Supp 1999). Charles Nesson and David Marglin suggest that the constitutionality of the CDA—and by extension of COPA—will change over time: even if it was
not con s ti tuti onal initi a lly, tech n o l ogical ch a n ge may ren der it con s ti tuti onal later; s ee
Charles Nesson and David Marglin, "The Day the Internet Met the First Amendment: Time
and the Com mu n i c a ti ons Decency Act ," Ha rva rd Jou rnal of Law and Te ch n ol o gy 10 (1996):
113.

42. See World Wide Web Consortium, "Platform for Internet Content Selection (PICS),"

available at http://www.w3.org/PICS/ (visited October 25,1998).

43. See Diane Roberts, "On the Plurality of Ratings," Cardozo Arts and Entertainment Law

Journal 15 (1997): 105,113–15.

4 4 . Paul Re s n i ck , " PI C S - In tere s t @ w 3 . or g, Moving On," Ja nu a ry 20 1999, ava i l a ble at
h t tp : / / l i s t s . w 3 . or g / Arch ive s / Pu bl i c / p i c s - i n tere s t / 1 9 9 9 Ja n / 0 0 0 0 . h tml (vi s i ted May 30, 1 9 9 9 ) ;
Paul Re s n i ck , " F i l tering In form a ti on on the In tern et ," S ci en tific Am eri c a n 106 (Ma rch
1 9 9 7 ) , also ava i l a ble at http : / / w w w. s c i a m . com / 0 3 9 7 i s su e / 0 3 9 7 re s n i ck . h tml (vi s i ted May 30,
1 9 9 9 ) ; Paul Re s n i ck ," PICS and In tell ectual Freedom FAQ ," ava i l a ble at http : / / w w w. w 3 . or g
/ PI C S / PI C S - FAQ – 9 8 0 1 2 6 . h tml (vi s i ted May 30, 1 9 9 9 ) ; Paul Re s n i ck and Jim Mi ll er, " PI C S :
In tern et Access Con trols Wi t h o ut Cen s ors h i p," Co m mu n i c a tions of the AC M 39 (1996): 8 7 ,
also ava i l a ble at http : / / w w w. w 3 . or g / PI C S / i ac wc v 2 . h tm (vi s i ted May 30, 1 9 9 9 ) ; Jim Mi ll er,
Paul Re s n i ck , et al., " PICS 1.1 Ra ting Servi ces and Ra ting Sys tems—and Th eir Mach i n e -
Re ad a ble De s c ri pti on s ," O ctober 31, 1 9 9 6 , ava i l a ble at http : / / w w w. w 3 . or g / T R / R E C - PI C S -
s ervi ces) (vi s i ted May 30, 1 9 9 9 ) ; Tim Kra u s Krauskopf , Paul Re s n i ck , et al., " PICS 1.1 Label
Di s tri buti on — L a bel Syntax and Com mu n i c a ti on Pro toco l s ," O ctober 31, 1 9 9 6 , ava i l a ble at
h t tp : / / w w w. w 3 . or g / T R / R E C - PI C S - l a bels (vi s i ted May 30, 1 9 9 9 ) ; Ch ri s toph er Eva n s , Pa u l

2 7 9

Re s n i ck , et al., "W3C Recom m en d a ti on : PICS Rules 1.1, R E C - PI C S , Ru l e s – 9 7 1 2 2 9 ," Decem ber 29, 1 9 9 7 , ava i l a ble at http : / / w w w. w 3 . or g / T R / R E C - PI C S Rules (vi s i ted May 30,
1 9 9 9 ) .

4 5 . See Jonathan Wei n ber g, " Ra ting the Net ," Ha s ti n gs Co m mu n i c a tions and En tert a i n -

ment Law Journal 19 (1997):453, 478 n.108.

4 6 . See , for ex a m p l e , the Cen ter for Dem oc racy and Tech n o l ogy 's en dors em ent of
p a rental em empowerment ent thro u gh ra ting sys tems and bl ocking sof t w a re ra t h er than government regulation in "Internet Family Empowerment White Paper," July 16, 1997, available at
h t tp : / / w w w. cd t . or g / s peech / em power. h tml (vi s i ted May 30, 1 9 9 9 ) ; a similar point of vi ew is
found in Esther Dys on ," Release 1.0: L a bels and Di s cl o su re ," Decem ber 1996, ava i l a ble at
http://www.edventure.com/release1/1296body.html (visited May 30,1999).

47. This claim, of course,is too strong. The site could block deceptively, making it seem as
if the user were gaining access but actually not giving her access to what she believes she is
gaining access to.

48. See Richard Thompson Ford ("The Boundaries of Race: Political Geography in Legal
An a lys i s ," Ha rva rd Law Revi ew 107 [1994]: 1 8 4 1 , 1 8 4 4 ) , who asserts that ju ri s d i cti on a l
bo u n d a ries perpetu a te racial segrega ti on and inequality a l i ty; G erald E. Frug ("Un ivers i ties and
Cities," Connecticut Law Review 30 [1998]: 1199, 1200), explains how universities erect borders to divorce themselves from surrounding poverty and argues that universities should critique these borders;Lani Guinier ("More Democracy," University of Chicago Legal Forum 1995
[ 1 9 9 5 ] : 1 , 3) advoc a tes a cro s s - racial parti c i p a tory dem oc racy that demands a con cern for,
and a familiarity with, the views of others.

4 9 . See Regents of the Un ivers i ty of C a l i fo rnia v Ba k ke , 438 US 265, 312 (1978) (Ju s ti ce
Lewis F. Powell, quoting Keyishian v Board of Regents, 385 US 589,603 [1967]: "The Nation's
future depends upon leaders trained through wide exposure to that robust exchange of ideas
which discovers truth 'out of a multitude of tongues, [rather] than through any kind of authoritative selection'").

50. See Fiss, The Irony of Free Speech, 3, 37–38; Sunstein, Democracy and the Problem of
Free Speech, xvi–xx. Andrew Shapiro's powerful analysis of Sunstein's point is better tuned to
the realities of the Net; see The Control Revolution, 107–12.

5 1 . It h i el de Sola Poo l , Te ch n ol o gies Wi t h out Bou n d a ries: On Tel e co m mu n i c a tions in a

Global Age, edited by Eli M. Noam (Cambridge, Mass.: Harvard University Press,1990),15.

52. See Geoffrey R.Stone,"Imagining a F ree Press," Michigan Law Review 90 (1992):1246,

1264.

53. But see Thomas G. Krattenmaker and L.A. Powe Jr. ("Converging First Amendment
Principles for Conver ging Com mu n i c a ti ons Med i a ," Yale Law Jou rn a l 104 [1995]: 1 7 1 9 ,
1735), who argue that First Amendment principles urge that consumers,not the government,
control the content they consume in the area of emerging media technologies; Sunstein ("The
F i rst Am en d m ent in Cybers p ace ," Yale Law Jou rnal 104 [1995]: 1 7 5 7 , 1765) con tends that
emerging media t echnologies produce new areas for applying old M Madisonian First Amendment principles.

54. For an early and ext extraordinary work that struggles with the complexity of the question about which information you should be able to own, see Anne Wells Branscomb, Who
Owns Information?: From Privacy to Public Access (New York: Basic Books, 1994). My conclusions are different from hers, but I agree with her insight that "ownership" cuts across different kinds of information in different ways. James Boyle advances a similar theme in Shamans,
Software, and Spleens.

55. See 47 CFR § 73.277 (1998).
56.47 USCA §§ 81–119 (1927) (repealed by the Communications Act of 1934).
57. See Red Lion Broadcasting Company v Federal Communications Commission, 395 US
3 6 7 , 375–77 (1969); Na tional Broadcasting d c a s ting Co m pa ny v Un i ted St a te s , 319 US 190, 2 1 2 – 1 3

2 8 0

(1943). Thomas Hazlett makes a powerful critique of Frankfurter's history of the emergence
of any necessity for FCC regulation; see Physical Scarcity.

58. See Turner Broadcasting System, Inc. v Federal Communications Commission, 512 US

622,637–38 (1997);see also Huber, Law and Disorder in Cyberspace.

59. See National Broadcasting Company, Inc. v Columbia Broadcasting System, 213.
60. See Huber, Law and Disorder in Cyberspace, 28–34. The dominant voice in this debate
is Thomas W. Hazlett, who has argued strongly against the licensing regime for spectrum and
in favor of a property auction. His work on the history of the Radio Act is particularly good;
see, for example, "Assigning Property Rights to Radio Spectrum Users: Why Did FCC License
Auctions Take Sixty-seven Years?," Journal of Law and Economics 41 (1998): 529; "Oak Leaves
and the Ori gins of the 1927 Radio Act : Com m en t ," Pu blic Choice 95 (1998): 2 7 7 ; " P hys i c a l
Scarcity, Rent Seeking, and the First Amendment," Columbia Law Review 97 (1997):905; "The
Rationality of U.S. Regulation of the Broadcast Spectrum," Journal of Law and Economics 33
(1990): 133; Thomas W. Hazlett and David Sosa, "Was the Fairness Doctrine a 'Chilling Effect'?: Evidence from the Post deregulation Radio Market," Journal of Legal Studies 26 (1997):
2 7 9 . For another historical acco u n t , s ee Morton I. Ha m burg and Stu a rt N. Bro tm a n , Co m -
mu n i c a tions Law and Pra cti ce , vo l . 1 (New York : L aw Jo u rnal Sem i n a rs – Pre s s , 1 9 9 5 ) , 5 – 8 .
Ithiel de Sola Pool was an early advocate of a position close to Hazlett's;see Technologies With -
out Boundaries, 108–88.

6 1 . See Ronald H. Coa s e , "The Federal Com mu n i c a ti ons Com m i s s i on ," Jou rnal of Law

and Economics 2 (1959): 1.

62. See Patrick M. Garry, Scrambling for Protection: The New Media and the First Amend -

ment (Pittsburgh: University of Pittsburgh, 1994),97–106.

63. There is an important argument supporting a different treatment for the "press" under the First Amendment, though the Supreme Court has not yet developed this distinctive
ju ri s pru den ce . Ju s ti ce Po t ter Stew a rt sketch ed some of the po ten tial in "Or of the Pre s s"
(Hastings Law Journal 26 [1975]: 631), and his argument takes on a new significance in the
context of the Internet. For a persuasive account,see Garry, Scrambling for Protection, 107–21.
64. See Hazlett, Physical Scarcity, 911–12; Anna Couey, "The Birth of Spread Spectrum,"
ava i l a ble at http : / / w w w. s i riu s . be / l a m a rr. h tm (vi s i ted May 30, 1 9 9 9 ) ; Jack Glas, "The Pri principles of S pre ad Spectrum Com mu n i c a ti on ," ava i l a ble at http : / / c a s . et . tu del f t . n l / ~ gl a s
/ssc/techn/techniques.html (visited May 30, 1999).One important reason for the shortage of
spectrum is its inefficient use;see de Sola Pool, "Technologies Without Boundaries," 42–45.

6 5 . Yochai Ben k l er 's arti cle provi des (for law yers) the most ex ten s ive discussion of t h e
tech n o l ogy; s ee "Overcoming Agora ph obi a ," 2 8 7 . He de s c ri bes the ch a n ge in tech n o l ogy:
"The technological shift derives from various techniques—such as spread spectrum and code
division multiple access, time division multiple access,frequency hopping, and packet switching—for allowing multiple users to communicate at the same time using the same frequency
ra n ge . Some of these tech n o l ogies com p l em ent each other; s ome con f l i ct with each other.
What is crucial to understand about these t echnologies is that they challenge the underlying
assumption of both licensing and privatization:that the only way to assure high quality wireless com mu n i c a ti ons is to assign one pers on the ri ght to transmit in a given frequ en c y
b a n d " ( 3 2 4 , foo tn o te om i t ted ) . The appendix to his arti cle then de s c ri bes the rel a ted technologies,including spread spectrum (395), time division multiple access (TDMA) (397),and
frequency hopping (399). For a discussion of code division multiple access and frequency division multiple access,see Ted Stevens,"Regulation and Licensing of Low-Earth-Orbit Satellites," Santa Clara Computer and High Technology Law Journal 10 (1994): 401.

66. Ethernet literally functions like this. Data on an Ethernet network are st reamed into
each machine on that network. Each machine sniffs the data and then pays attention to the
data inten ded for it. This process cre a tes an obvious sec u ri ty hole: "s n i f fers" can be put on

2 8 1

"promiscuous mode" and re ad packets inten ded for other mach i n e s ; s ee Lo s h i n , TC P / I P
Clearly Explained, 44–46.

6 7 . See Yochai Ben k l er and Lawren ce Le s s i g, " Net Gains," New Repu bl i c , Decem ber 14,

1998.

68. The founder of this argument must be Eli Noam;see "Spectrum Auctions: Yesterday's
Heresy, Today's Orthodoxy, Tomorrow's Anachronism—Taking the Next Step to Open Spectrum Access," Journal of Law and Economics 41 (1998): 765. Benkler has spiced it up a bit (in
my vie w, in critical ways) by adding to it the value of the commons. For an extraordinarily
powerful push to a similar political (if not technological) end,see Eben Moglen, "The Invisible Barbecue," Columbia Law Review 97 (1997): 945. Moglen notes the lack of debate regarding the soc i opo l i tical con s equ en ces of c a rving up tel ecom mu n i c a ti on ri ghts at the "Gre a t
Barbecue" and draws a parallel with the Gilded Age's allocation of benefits and privileges associated with the railroad industry.

C H A P T E R F O U R T E E N

1. See Stephen Holmes, "What Russia Teaches Us Now; How Weak States Threaten Freedom," American Prospect (July-August 1997): 30.

2. See Restatement (Third) Of Foreign Relations Law (1986),§ 402(2) and comment (e).
3. Child Sexual Abuse Prevention Act, 18 USC § 2423(b) (1994). See Margaret A. Healy,
" Pro s ec uting Child Sex To u rists at Hom e : Do Laws in Sweden , Au s tra l i a , and the Un i ted
States Safeguard the Rights of Children as Mandated by International Law?," Fordham Inter -
national Law Journal 18 (1995):1852,1902–12.

4. See Bill Grantham, "America the Menace: France's Feud With Hollywood," World Policy
Journal 15,no. 2 (Summer 1998): 58; Chip Walker, "Can TV Save the Planet?," American De -
mographics (May 1996): 42.

5. These are among the most watched television shows in the world;see Henry Goldblatt,

"The Universal Appeal of Schlock," Fortune, May 12,1997,32.

6. Akhil Reed Amar, "Of Sovereignty and Federalism," Yale Law Journal 96 (1987): 1425,

1430–31.

7. U.S. Constitution,art.VI, cl.2.
8. See, for example,David R. Johnson and David Post,"Law and Borders: The Rise of Law

in Cyberspace," Stanford Law Review 48 (1996): 1367,1369–76.

9. Ibid.,1379–80.
1 0 . See Jack L. G o l d s m i t h , "Against Cyberanarchy n a rchy," Un ivers i ty of C h i c a go Law Revi ew 6 5
( 1 9 9 8 ) : 1 1 9 9 ; Jack L. G o l d s m i t h , "The In tern et and the Abiding Si gn i f i c a n ce of Terri tori a l
Soverei gn ty," Indiana Jou rnal of Gl obal Legal Stu d i e s 5 (1998): 4 7 5 ; s ee also David Jo h ns ton , Su n ny Ha n d a , and Ch a rles Mor ga n , Cy berl aw: What You Ne ed to Kn ow Ab out Do i n g
Business On l i n e (Toron to : S tod d a rt , 1 9 9 7 ) , ch . 1 0 . Allan R. S tein ("The Un excepti on a l
Probl em of Ju ri s d i cti on in Cybers p ace ," The In tern a tional Law yer 32 [1998]: 1167) argues
that the ju ri s d i cti onal probl ems in cybers p ace are like those found in re a l - s p ace intern ati onal law.

11. See Litman,"Revising Copyright Law for the Information Age," 38–39.
12. Ibid.
1 3 . As Ka tie Ha f n er and Ma t t h ew Lyon put it: "The best hackers were profe s s i on a l s .
Med dl e s ome and malicious net work users , of wh i ch there were vi rtu a lly none at the out s et ,
were first referred to as 'n et work ra n dom s' or 'n et ra n dom s' or just plain 'ra n dom s .' It
would be another dec ade before hacking was given a bad name" ; W h ere Wi z a rds St ay Up
La te, 1 9 0 .

2 8 2

14. Cf. Bruce Sterling, The Hacker Crackdown: Law and Disorder on the Electronic Frontier

(New York: Bantam Books,1992),55–57.

1 5 . See Ka a re Ch ri s tian and Susan Ri ch ter, The UNIX Opera ting Sys tem , 3d ed . ( New

York: Wiley, 1994),5–8.

1 6 . See , for ex a m p l e , All en H. Lippis et al., E l e ctronic Ba n k i n g ( New York : Wi l ey,

1985),159–87.

17. Examples include the hacking of the Defense Department computers by the German
Peter Ca rl , and then an aut h ori zed break-in to dem on s tra te the vu l n era bi l i ty; s ee Ka ti e
Hafner and John Markoff, Cyberpunk: Outlaws and Hackers on the Computer Frontier (New
York: Simon & Schuster 1991),173–79,266.

18. Morris's father, Robert Morris Sr., was the NSA's expert on data security at the time;

see ibid.,253–341.

19.A commercial version of the software is not free,and of course,that version includes

updates to correct for "bugs."

20. See Computer Fraud and Abuse Act,18 USC § 1030(a)(5)(A) (1988) (current version

at 18 USC § 1030[a][5][A] [1994],amended by 18 USC 1030[a][5][A] [Supp II 1996]).

21. United States v Morris, 928 F2d 504, 506 (2d Cir 1991).
22. Julian Dibbell, "The Prisoner: Phiber Optik Goes Directly to Jail," Village Voice, January 12,1994, available at http://www.levity.com/julian/phiber.html (visited May 30,1999).

23. See United States v LaMaccia, 871 FSupp 535 (DMass 1994);see also Mitchell Zuckoff,
"Sof t w a re Piracy Ch a r ges Di s m i s s ed Against Stu den t ," Bo s ton Gl obe , Decem ber 30, 1 9 9 4 , 1 ;
United States v LaMaccia, memorandum of decision and order on defendant's motion to dismiss, December 28,1994,http://photo.net/dldf/dismiss-order.html (visited May 30,1999).

24. See Steve Jackson Games, Inc. v U.S. Secret Service, 36 F3d 457 (5th Cir 1994); see also
Joe Abernathy, "Trial Set This Week in Computer Case; Publisher Sues Secret Service," Hous -
ton Chronicle (January 18,1993),13; Steve Jackson Games v U.S.Secret Service, complaint, May
1, 1991, available at http://www.eff.org/pub/Legal/Cases/Inc./SJG/complaint.sjg (visited May
30,1999).

2 5 . Nevert h el e s s ,t h ere is arguably som ething of a revival among hackers—as disti n ct from
"c crackers"—at least among new hackers who em ph a s i ze po l i tical or social en d s ; s ee , for ex a mp l e , Jim Kers tet ter, "A Repri eve for ' Ethical Hack i n g,' " PC Week On l i n e , Ju ly 20, 1 9 9 8 , ava i l a ble at
h t tp : / / w w w. zd n et . com / zd n n / s tori e s / zd n n _ d i s p l ay / 0 , 3 4 4 0 , 3 3 7 6 4 4 , 0 0 . h tml (vi s i ted May 30,
1 9 9 9 ) ; Al ex Well en ," 'Cracker ' Term Gains Accept a n ce by Med i a ," Z D TV, May 19, 1 9 9 8 , ava i l a bl e
at http : / / w w w. zd n et . com / zd n n / con ten t / zd t v / 0 5 1 9 / 3 1 7 3 0 7 . h tml (vi s i ted May 30, 1 9 9 9 ) .

2 6 . See Alan Schw a rt z , "The Default Rule Pa rad i gm and the Limits of Con tract Law,"

Southern California Interdisciplinary Law Journal 3 (1993):389.
27. See Goldsmith, "Against Cyberanarchy," 1205–12.
28. ProCD, Inc. v Zeidenberg, 86 F3d 1447,1453–55 (7th Cir 1996).
29. "The teleprompter right to exclude [is] 'one of the most essential sticks in the bundle
of ri ghts that are com m on ly ch a racteri zed as property ' " ; Lo ret to v Tel epro m pter Ma n h a t t a n
CATV Corporation, 458 US 419,433 (1982) (quoting Kaiser Aetna v United States, 444 US 164,
176 [1979]); see also Cape Cod Nursing Home Council v Rambling Rose Rest Home, 667 F2d
238 (1st Cir 1981) (organizations seeking access to rest home to inform residents of services
t h ey provi ded could be exclu ded ) ; Aso ci a cion Tra ba ja d o res Agri colas de Pu Puerto Ri co v Gre en
Giant Co m pa ny, 518 F2d 130 (3d Cir 1975), ( com p a ny - own ed camp for migrant workers
could exclude union officials); cf. Kaiser Aetna v United States, 444 US 164 (1979) (requiring
public access to a private marina was a taking).

3 0 . See , for ex a m p l e , Laguna Pu blishing Co m pa ny v Gol d en Rain Fou n d a ti o n , 131 CAL
App3d 816, 8 4 5 , 182 Ca l i f R ptr 813 839 (1982) (noting that the on ly means for com peti tors
of a com mu n i ty news p a per to distri bute samples was thro u gh the mail); Gu t ten berg Ta x -
payers and Ren rentpayers As so ci a tion v Galaxy Towers Condominium As so ci a ti o n , 297 NJSu per
4 0 4 , 4 1 0 – 1 1 , 688 A2d 156, 159 (NJSu p C t Ch Div) aff 'd 297 NJSu per 309, 688 A2d 108 (NJn o t e s

2 8 3

Su p C t App Div 1996) (noting that the plaintiffs f fs , who were seeking to distri bute po l i tical materials to con dom i n ium re s i den t s , h ad on ly the inadequate a te altern a tive of d i s tri buting thei r
m a materials thro u gh the mail).

3 1 . The re ader may won der wh et h er this kind of c ybers p ace rel a ti onship is more than
"phone sex." Yes. The intensity of this form of exchange is wildly beyond the panting of a telephone lover; see Julian Dib bell,"Keys to the Kingdom: Cryptography, the Black Art of Spies
and Diplomats, Moves Center Stage on the Net," Time, November 11,1996,TD38ff."But it is
also incon controvertible ble proof that some kinds of a ri t h m etic can re ach meaningfully u lly into our
lives at every point on the spectrum of human experience—in our political contests, in our
economic dealings and,as anyone who has used the office computer to E-mail a lover can attest,in the most intimate recesses of our emotional affairs."

32. Timothy S. Wu has a more careful and balanced picture of the conditions under which
sovereignty might exist; see "Cyberspace Sovereignty?: The Internet," Harvard Journal of Law
and Technology 10 (1997):647.

3 3 . D avid R. Jo h n s on and David G. Post both favor, not no govern m en t , but decen tra li zed em er gent norms that resist top - down con tro l ; s ee , for ex a m p l e , "And How Shall the Net
Be Govern ed ? : A Med i t a ti on on the Rel a tive Vi rtues of Decen tra l i zed ,E m er gent Law," in Co -
o rd i n a ting the In tern et , ed i ted by Brian Kahin and James H. Kell er (Ca m bri d ge , Ma s s . : M I T
Pre s s , 1 9 9 7 ) , 6 2 . I have not ad d re s s ed the means for governing in cybers p ace , except to the
ex tent that the means are implied by an arch i tectu re of open code . My pri m a ry focus is on
the set of va lu e s .

34. See Judith N.Shklar, American Citizenship: The Quest for Inclusion (Cambridge, Mass.:
Ha rva rd Un ivers i ty Pre s s , 1 9 9 1 ) , 2 5 – 6 2 ; James A . G a rd n er, " L i berty, Com mu n i ty, and the
Constitutional Structure of Political Influence: A Reconsideration of the Right to Vote," Uni -
versity of Pennsylvania Law Review 145 (1997): 893; Quiet Revolution in the South, edited by
Chandler Davidson and Bernard Grofman (Princeton,N.J.: Princeton University Press,1994):
21–36.

35. See Lani Guinier, The Tyranny of the Majority: Fundamental Fairness in Representative
Democracy (New York: Free Press, 1994); Richard Thompson Ford,"Beyond Borders: A Partial Response to Richard Briffault," Stanford Law Review 48 (1996):1173; Richard Thompson
Ford , "G Geography phy and Soverei gn ty: Ju ri s d i cti onal Form a ti on and Racial Segrega ti on ," St a n -
fo rd Law Revi ew 49 (1997): 1 3 6 5 ; Jerry Fru g, " Decen tering Decen tra l i z a ti on ," Un ivers i ty of
C h i c a go Law Revi ew 60 (1993): 2 5 3 ; Jerry Fru g, "The Geogra phy of Com mu n i ty," St a n fo rd
Law Review 48 (1996): 1047.

36. See Michael Walzer, Spheres of Justice: A Defense of Pluralism and Equality (New York:

Basic Books,1983).

3 7 . See Ch a rles M. Ti ebo ut , "A Pu re Th eory of Local Ex pen d i tu re s ," Jou rnal of Pol i ti c a l
Economy 64 (1956):416; see also Clayton P. Gillette, Local Government Law: Cases and Mate -
rials (Boston: Little, Brown,1994),382; Vicki Been,"'Exit' as a Constraint on Land Use Exactions on s : Rethinking the Un con s ti tuti onal Con d i ti ons Doctri n e ," Col u m bia Law Revi ew 9 1
(1991): 473, 514–28.

38. See David G. Post, "Governing Cyberspace," Wayne Law Review 43 (1996):155; David
Post, "The New Electronic Federalism," American Lawyer (October 1996): 93; David G. Post,
"The 'Unsettled Paradox': The Internet,the State,and the Consent of the Governed," Indiana
Jou rnal of Gl obal Legal Stu d i e s 5 (1998): 5 2 1 , 5 3 9 ; D avid R. Jo h n s on and Kevin A . Ma rk s ,
"Mapping Electronic Data Communications onto Existing Legal Metaphors: Should We Let
Our Conscience (and Our Contracts) Be Our Guide?," Villanova Law Review 38 (1993): 487;
Johnson and Post,"Law and Borders";David G. Post, "Anarchy, State,and the Internet: An Ess ay on Law - Making in Cybers p ace ," Jou rnal of Online Law ( 1 9 9 5 ) : a rti cle 3, ava i l a ble at
http://www.law.cornell.edu/jol/post.html (visited May 30, 1999).

39. See Phillip E. Areeda et al., Antitrust Law, vol.2A (Boston:Little, Brown,1995),85–87.
40. See Post, "Anarchy, State,and the Internet," 29–30.

2 8 4

41. This was not quite t rue of MUDing in the past. When the communities were smaller,
there were portals that allowed characters to move from one MUD to another. Famous MUD
characters became well known in many different communities, and it was unethical to take
the name of a well-known MUDder, even from a different MUD. But as the world of MUDing
has grown,the ability to port yourself elsewhere is less meaningful. The communities here are
simply associations,and the associations do not transfer.

42.I am not saying that this situation could not be different. We might imagine regions of
communities in cyberspace that facilitate mo ving between communities.I am speaking only
about the space as it is now.

43. See Post, "Anarchy, State, and the Internet," 82–83, 100.
44. Ibid.,100.
4 5 . See , for ex a m p l e , G eor ge A . Berm a n n , "Taking Su b s i d i a ri ty Seri o u s ly: Federalism in
the European Community and the United States," Columbia Law Review 94 (1994): 331; Albert Breton et al.,"Decentralization and Subsidiarity: Toward a Theoretical Reconciliation,"
Un ivers i ty of Pen n s Pennsylvania Jou rnal of In tern a tional Economic Law 19 (1998): 2 1 ; Cl ayton P.
G i ll et te , "The Exercise of Trumps by Decen tra l i zed Govern m en t s ," Vi rginia Law Revi ew 8 3
(1997):1347.

46. See, for example, George A. Bermann, "Subsidiarity and the European Community,"
Hastings International and Comparative Law Review 17 (1993):97, 103,105; Bermann, "Taking Subsidiarity Seriously," 452–53.

47.Or at least three of the four regions in the early United States shared this history; see

Fischer, Albion's Seed, 827–28.

4 8 . Arti cle V of the Con s ti tuti on states (ob s c u rely no do u bt) that "provi ded that no Am en dm ent wh i ch may be made pri or to the Year One thousand ei ght hu n d red and ei ght shall in any
Ma n n er affect the first and fo u rth Clauses in the Ninth Section on of the first Arti cl e ." These cl a u s e s
s t a te : "(1) The Mi gra ti on or Im port a ti on of su ch Pers ons as any of the States now ex i s ting shall
think proper to ad m i t ,s h a ll not be pro h i bi ted by the Con gress pri or to the Year one thousand
ei ght hu n d red and ei gh t , but a Tax or duty may be impo s ed on su ch Im port a ti on , not exceeding ten Do ll a rs for each Pers on" ; and "(4) No Ca p i t a ti on , or other direct , Tax shall be laid, u nless in Proportion on to the Cen sus or Enu m era ti on herein before directed to be taken ."
49. See John F. Kennedy, Profiles in Courage (New York: Harper, 1956), ch.3.
5 0 . For ex a m p l e , in its devel opm ent of PI C S , the World Wi de Web con s consortium made a
commitment to both value and vendor neutrality; see "Platform for Internet Content Selection (PICS)," available at http://www.w3.org/PICS (last modified June 4,1998).

5 1 . See World In tell ectual Property Orga n i z a ti on , "Final Report of the WIPO In tern et
Domain Name Process," April 30, 1999, forthcoming in hardcover as WIPO Publication No.
9 2 – 8 0 5 – 0 7 7 9 – 6 , ava i l a ble at http : / / wi po 2 . wi po. i n t / proce s s / en g / f i n a l _ report . h tml (vi s i ted
May 30,1999).

5 2 . Q u o ted in Bri n , The Tra n s pa rent Soci ety, 2 1 8 . For an excell ent account of the more
gen eral qu e s ti on , s ee A . Mi ch ael Froom k i n , "The In tern et as a So u rce of Reg u l a tory Arbitrage," in Borders in Cyberspace: Information Policy and the Global Information Infrastructure,
ed i ted by Brian Kahin and Ch a rles Ne s s on (Ca m bri d ge , Ma s s . : MIT Pre s s , 1 9 9 7 ) , 1 2 9 .
Froomkin considers both the technological features of the Net that enable arbitrage and the
limits on arbitrage that we might expect.

5 3 . Ethan Katsh makes a similar point in "Sof t w a re Worlds and the First Am en d m en t ,"
wh ere he argues that legi s l a tors wi ll come to understand the plastic c i ty and reg u l a ti on in
code . Tim Wu makes the same point in "Cybers p ace and the In tern a ti onal Sys tem ." For a
t h o u gh tful account of h ow a federalist stru ctu re in cybers p ace might loo k ,s ee Dan L. Bu rk ,
" Federalism in Cybers p ace ," Co n n e Connecticut Law Revi ew 28 (1996): 1 0 9 5 . Bu Burk's analys i s ,m ade
f rom the pers pective of Am erican federa l i s m , is a tem p l a te for the same qu e s ti ons ra i s ed intern a ti on a lly.

2 8 5

54. Some conceive of constitutional values, for example, as constraints on efficiency; see
Brin, The Transparent Society, 223, quoting Godwin: "Governments have to sacrifice some efficiency to preserve those rights."

C H A P T E R F I F T E E N

1. Missouri v Holland, 252 US 416,433 (1920).
2. See, for example, Jack N. Rakove, Original Meanings: Politics and Ideas in the Making of
the Constitution (New York: Alfred A. Knopf, 1996), 289–90; see also Akhil Reed Amar, "The
Bill of Rights as a Constitution" (Yale Law Journal 100 [1991]:1131), for another such understanding of the Bill of Rights.

3. This is not to deny that some aspects of the equality delineated in the Civil War amendm ents ech oed in our con s ti tuti onal past. The abo l i ti on i s t s , of co u rs e , m ade great wei ght of
the Decl a ra ti on of In depen den Declaration claims to equ a l i ty; s ee , for ex a m p l e , Trisha Ol s on , "Th e
Natural Law Foundation of the Privileges or Immunities Clause of the Fourteenth Amendment," Arkansas Law Review 48 (1995):347,364. An amendment can be transformative,however, even if it is simply recalling a part of the past and reestablishing it—as Germany did, for
example,after World War II.

4. See Plessy v Ferguson, 163 US 537 (1896).
5. See A. Leon Higginbotham Jr.,"Racism in American and South African Courts: Similarities and Differences," New York University Law Review 65 (1990): 479,495–96.

6. These laws permitted compelled labor to pay a debt;see Bailey v Alabama, 219 US 219

(1911) (striking peonage laws under the Thirteenth Amendment).

7. Brown v Board of Education, 347 US 483 (1954).
8. See, for example, Dennis v United States, 341 US 494 (1951) (upholding convictions under the Smith Act, which banned certain activities of the Communist Party).

9. See Korematsu v United States, 323 US 214 (1944).
10. See, for example, John Hart El y, Democracy and Distrust: A Theory o f Judicial Review

(Cambridge, Mass.: Harvard University Press,1980).

1 1 . I 've overs t a ted the sec u ri ty of the Am erican ju d i c i a ry. A recent incident with Di stri ct Co u rt Ju d ge Ha Harold Baer su ggests con ti nu ed insec u ri ty, e s pec i a lly in the con text of t h e
war on dru gs . Baer rel e a s ed a criminal defendant after su ppressing a search that had discovered ei gh ty pounds of n a rco ti c s ; Don Van Natta Jr. , " Ju d ge's Drug Ruling Likely to
S t a n d ," New Yo rk Ti m e s , Ja nu a ry 28, 1 9 9 6 , 2 7 . The dec i s i on was then attacked by pre s i dential candidate Robert Do l e , who call ed for Baer 's impeachment ach m en t ; Ka t h a rine Q. Seelye , "A Get
To u gh Me s s a ge at Ca l i forn i a's Death Row," New Yo rk Ti m e s , Ma rch 24, 1 9 9 6 , 2 9 . Pre s i den t
Cl i n ton then joi n ed the bandwagon a gon , su gge s ting that he might ask for Baer 's re s i gn a ti on if
Baer did not reverse his dec i s i on ; Al i s on Mi tch ell , "Cl i n ton Pressing Ju d ge to Rel en t ," New
Yo rk Ti m e s , Ma rch 22, 1 9 9 6 , 1 . Baer then did reverse his dec i s i on ; Don Van Natta Jr. ," Under Pre s su re , Federal Ju d ge Reverses Dec i s i on in Drug Ca s e ," New Yo rk Ti m e s , April 2, 1 9 9 6 ,
1 . Ch i ef Ju d ge Jon Newm a n , of the Second Ci rcuit Co u rt of Appe a l s , a l ong with other
ju d ge s , t h en cri ti c i zed Do l e's cri ticism of Baer, arguing that he went "too far"; Don Va n
Natta Jr. ," Ju d ges Defend a Co lleague from At t ack s ," New Yo rk Ti m e s , Ma rch 29, 1 9 9 6 , B 1 .
Sovi et citi zens would recogn i ze the pattern .

12. I describe the Court's conception of its role in more detail in Lessig, "Translating Federalism."

1 3 . Robert H. Bork , The An ti trust Pa ra d ox: A Policy at War with It sel f ( New York : Ba s i c

Books, 1978),83.

14. See, for example, Felix Frankfurter, The Commerce Clause Under Marshall, Taney, and

Waite (Chapel Hill: University of North Carolina Press,1937): 82.

2 8 6

15. The relationship between a c contested ground and a political judgment is more complex than this suggests. I discuss it more extensively in Lawrence Lessig, "Fidelity and Constraint," Fordham Law Review 65 (1997): 1365.

16. ACLU v Reno, 929 FSupp 824 (EDPa 1996); Shea v Reno, 930 FSupp 916 (SDNY 1996).
17. I discuss this in Lessig, "Fidelity and Constraint."
18. One could well argue that during the crisis of the Depression deference by the Court
to the Congress would have been well advised;see, for example, Sunstein, Democracy and the
Problem of Free Speech, 39.

19. Fischer (Albion's Seed) shows how town planning in the United States followed habits

in Europe.

20. David P. Currie, The Constitution of the Federal Republic of Germany (Chicago: University of Chicago Press,1994),182–87.

21.This is the system that associates a name on the Internet (for example, "cyber.law.harvard.edu") with an Internet protocol address (for example,128.12.12.01). People register domain names,now primarily through a company called Network Solutions. Their name,if it is
available, is then associated with a particular server.

22. Payne v Tennessee, 501 US 808,844 (1991) (Justice Thurgood Marshall dissenting).
23. In 1999 it was revealed that with some versions of Microsoft Word a unique identifier
was embedded in Word documents. Microsoft subsequently provided an upgrade to remove
the identifier data.

C H A P T E R S I X T E E N

1. Deborah Hellman,in "The Importance of Appearing Principled" (Arizona Law Review
37 [1995]: 1107), describes the illegitimacy costs that courts incur when they overrule precedents for apparently political reasons.

2 . Gu i do Ca l a bre s i , A Common Law for the Age of St a tu te s ( Ca m bri d ge , Ma s s . : Ha rva rd
Un ivers i ty Pre s s , 1 9 8 2 ) , 1 6 – 3 2 ; Gu i do Ca l a bre s i , "The Su preme Co u rt , 1990 Term — Foreword : An ti d i s c ri m i n a ti on and Con s ti tuti onal Acco u n t a bi l i ty (What the Bork - Brennan Debate Ignores)," Harvard Law Review 105

(1991):80,83,103–7,119–20.

3. Or come close to doing so;see Richard A. Posner, The Problems of Jurisprudence (Cambridge, Mass.: Harvard University Press,1990),300–301.

4 . I am gra teful to Vi k tor Mayer- S ch ö n ber ger for dem on s tra ting this point to me. Ha l
Abelson points out that the components would have to be verifiable if they were not themselves open. Otherwise, components could function as Trojan Horses—pretending to be one
thing while in reality being something else.

5 . Ma rk A . Lem l ey and David W. O' Bri en ," E n co u ra ging Sof t w a re Reu s e ," St a n fo rd Law

Review 49 (1997): 255.

6. For an extraordinary account of the damage done by copyright law to software development, see Mark Haynes,"Black Holes of Innovation in the Software Arts," Berkeley Tech -
nology Law Journal 14 (1999): 503.

7. Kennedy, Profiles in Courage, 71.
8. Negroponte, Being Digital, 238.
9. See Buckley v Valeo, 424 US 1 (1976) (striking campaign finance reform under the First

Amendment).

1 0 . See , for ex a m p l e , James S. F i s h k i n , The Vo i ce of the Pe opl e ( New Haven , Con n . : Ya l e

University Press,1995).

11. Dean Henry H. Perritt Jr. provides a well-developed picture of what "self-regulation"
in the Internet context might be,drawing on important ideals of democracy; see "Cyberspace
Self-government: Town Hall Democracy or Rediscovered Royalism?," Berkeley Technology Law
Journal 12 (1997): 413. As he describes it, the possibility of self-governance depends important o t e s

2 8 7

tantly on architectural features of the Net—not all of which are developing in ways that wil l
support democracy; see also Shapiro (The Control Revolution, 150–57,217–30), who discusses
"push-button politics" and tools of democracy.

1 2 . Al exis de Tocqu evi ll e , Dem o cracy in Am eri c a , vo l . 1 (New York : Vi n t a ge , 1 9 9 0 ) ,

2 8 4 – 8 5 .

C H A P T E R S E V E N T E E N

1. In "Accountability in a Computerized Society" (Science and Engineering Ethics 2 [1996]:
25), Helen Nissenbaum discusses the erosion in accountability within computerized societies,
including accountability about code itself.

2 . An d rew L. S h a p i ro, "The Di s a ppe a ra n ce of Cybers p ace and the Rise of Code ," S eto n

Hall Constitutional Law Journal 8 (1998): 703,721.

A P P E N D I X

1. Lessig, "The New Chicago School," 661.
2 . See H. L . A . Ha rt , The Co n cept of Law, 2d ed . ( New York : Ox ford Un ivers i ty Pre s s ,

1994),6–13,27–33.

3. For example, Illinois law states: "The third Monday in January of each year is a holiday
to be observed throughout the State and to be known as the birthday of Dr. Martin Luther
King, Jr. Within 10 days before the birthday of Dr. Martin Luther King, Jr., in each year the
G overn or shall issue a proclamation a m a ti on announcing the holiday and de s i gn a ting the of f i c i a l
events that shall be held in honor of the memory of Dr. Martin Luther King, Jr.,and his contributions to this nation"; 5 Illinois Comprehensive Statutes Annotated 490/65 (West 1998).

4. See Robert Cooter, "Expressive Law and Economics," Journal of Legal Studies 27 (1998):

585.

5. Cf. Paul N. Bracken, The Command and Control of Nuclear Forces (New Haven, Conn.:
Yale University Press,1983),179–237; Christopher Chant and Ian Hogg, The Nuclear War File
(London:Ebury Press,1983),68–115.

6. On the other side,the military built into the system technological brakes on the ability
to launch, to ensure that no decision to launch was ever too easy; see also Daniel Ford, The
Button: The Nuclear Trigger—Does It Work? (London: Allen & Unwin,1985), 118–21.

7. "The phenomena of social meaning and incommensurability constrain rational choice
( i n d ivi dual and co ll ective ) . G en era l i z i n g, it is irra ti onal to treat goods as com m en su ra bl e
where the use of a quantitative metric effaces some dimension of meaning essential to one's
purposes or goals. It would be irrational, for example, for a person who wanted to be a good
colleague within an academic community to offer another scholar cash instead o f comments
on her manuscript. Against the background of social norms, the comment signification of
respect cannot be reproduced by any amount of money; even to attempt the substitution conveys that the person does not value his colleague in the way appropriate to their relationship";
Dan M. Ka h a n , " Pu n i s h m ent In com m en su ra bi l i ty," Buffalo Criminal Law Revi ew 1 (1998):
691, 695.

8 . Ma ny sch o l a rs , Robert Coo ter most prom i n en t ly among them , argue that norms are
special because they are "internalized"in a sense that other constraints are not; see Robert D.
Cooter, "Decentralized Law for a Complex Economy: The Structural Approach to Adjudicating the New Law Merchant," University of Pennsylvania Law Review 144 (1996): 1643, 1662;
Robert D. Cooter, "The Theory of Market Modernization of Law," International Review of Law
and Economics 16 (1996):141,153. By internalization, Cooter is just describing the same sort
of subjectivity that happens with the child and fire: the constraint moves from being an o b-

2 8 8

jectively ex post constraint to a subjectively ex ante constraint. The norm becomes a part of
the pers on , su ch that the pers on feels its re s i s t a n ce before he act s , and hen ce its re s i s t a n ce
controls his action before he acts.Once internalized,norms no longer need to be enforced to
have force; their force has moved inside, as it were, and continues within this subjective perspective. In my view, we should see each constraint functioning in the same way: we subjectively come to account for the con s traint thro u gh a process of i n tern a l i z a ti on . Som e
internalization incentives may be stronger than others, of course. But that is just a difference.
9. Cf.Dan M. Kahan,"Ignorance of Law Is an Excuse—But Only for the Virtuous," Michi -

gan Law Review 96 (1997): 127.

10. See, for example,Schuster et al., Preserving the Built Heritage; Peter Katz, The New Ur -
urbanism: Toward rd an Arch i te ctu re of Co m mu n i ty ( New York : Mc Graw - Hi ll , 1 9 9 4 ) ; Du a ny and
Plater-Zyberk, Towns and Town-Making Principles.

11. Michael Sorkin, Local Code: The Constitution of a City at 42˚N Latitude (New York:

Princeton Architectural Press,1993), 11,127.

I N D E X

Abortion, 95, 96–97, 118
Abrams, Floyd, 168, 170
Accountability, 96, 153, 199
Ackerman, Bruce, 59
Advertising, 153–54, 198
African Americans, 98, 214
Agency, 237
Agreements, incompletely theorized, 149
Airline industry, 92, 155, 158–59, 171–72
Airplane crashes, 171–72. See also Airline

industry

Airport security, 158–59. See also Airline

industry

Alcohol, 91
Algorithms, 39–40
Alien and Sedition Acts, 148
Amazon.com, 31, 34
Ambiguity, latent, 22–23, 110, 119–20, 223;
in agreements, 149; and codifying
constitutions, 215; and democracy,
227; and free speech rights, 181; and
sovereignty, 191; and translation,
211–12

American Lawyer Media, L.P., 72
Americans with Disabilities Act, 91
American Telephone & Telegraph (AT&T),

44, 117, 150

America Online (AOL), 59, 83, 166; basic

description of, 66–71; chat, 21, 67–69,
71, 74; and Counsel Connect (CC),
73, 78; filtering features, 198; screen
names, 34, 67–68

Anarchism, 28, 214
"Anarchy, State, and the Internet" (Post),

Angola, 228

Anonymity, 26, 28, 217; and authentication,
31; and free speech rights, 166; and
intellectual property issues, 138–41;
and newsgroups, 80, 82

AOL (America Online), 59, 83, 166; basic

description of, 66–71; chat, 21, 67–69,
71, 74; and Counsel Connect (CC),
73, 78; filtering features, 198; screen
names, 34, 67–68
Apple Computer, 105
Articles of Confederation, 5–6
AT&T (American Telephone & Telegraph),

44, 117, 150
ATM networks, 27
Authentication, 30–36, 39–40, 42
Authorization, 40
Avatar space, 11–13, 20, 66. See also Virtual

reality

Baker, Stewart, 36
Bandwidth, 66
Barlow, John Perry, 108, 218
Baud rates, 64
BBSs (bulletin board services), 63, 67, 71
Benkler, Yochai, 185, 280n65
Berlin Wall, 77
Berners-Lee, Tim, 103
Bickel, Alexander, 168
Bill of Rights, 7, 213–14
Blind individuals, 65–66. See also Disabled

individuals
Body scans, 158
Borders, notion of, 9–13, 206
Bovinity, 57
Boyle, Jamie, 18, 131, 141

2 9 0

I n d e x

Brandeis, Louis, 111, 115, 117–18, 139, 144
Breyer, Stephen, 124
Brin, David, 60, 153
Britain, 5, 113. See also England
Broadcasting, 182–85
Brown v Board of Education, 214
Browsers: access control features for,

176–77; and cookies, 34–35, 41–42;
and intellectual property issues, 123;
and protocols, 102

Buddy lists, 69–70

Cahill, Gordon (law firm), 168
Cailliau, Robert, 103
Calabresi, Guido, 223
CALEA (Communications Assistance for
Law Enforcement Act), 44–46, 106

Camp, Jean, 220–21
Campaign financing, 227
Canada, 35, 207
Carnegie Mellon University, 77
Case, Steve, 68
Cases: Brown v Board of Education, 214;
Ginsberg v New York, 173, 175, 176,
178–79; Hudgson v Minnesota, 95;
Katz v United States, 116–17; Maher v
Roe, 95; Maryland v Craig, 119; Near v
Minnesota, 169; New York v United
States, 96, 97, 98; Olmstead v United
States, 111–12, 114, 116–17, 149;
ProCD v Zeidenberg, 136; Roe v Wade,
95; Rust v Sullivan, 95–98; Shelley v
Kramer, 97
Catalfo, Phil, 63
Cates, Richard, 229
CC (Counsel Connect), 71–74, 78–79, 83
CDA (Communications Decency Act),

174–75, 177–79, 216

CDs (compact discs), 46–47, 49, 128
Cellular telephones, 45–46, 146. See also

Telephones

Censorship, 178, 181, 205, 233. See also Free

speech
CERN, 103
Certificates, digital, 35, 38–39, 42, 49–53,

176, 207–8

Chat, 65–66; on American Online, 21,

67–69, 71, 74; Internet Relay Chat
(IRC), 64

Chicago Tribune, 169
Children, 71, 92; access control for, 33,
175–82; and COPA (Child Online
Protection Act), 177; protection of,
from pornography, 173–76; and rating
systems, 47; and television, 47. See also
Education
China, 56, 143, 167
Christian Right, 177
Circumvention, 49
Cisco, 52–53
Citibank, 206
Citizenship, 35, 41, 56; and education,

Marshall on, 92–93; and sovereignty,
199, 202, 205, 207; in a state, versus in
a nation, 226
Civil War, 213–14, 226
Click-wrap (shrink-wrap) licenses, 135, 206
Clinton, Bill, 229
Clinton, Hillary Rodman, 229
Clipper chip, 47–48, 248n18, 258n53
Coase, Ronald, 183
Codifying constitution, 213–15
Coercion, 85
Cohen, Julie, 139, 140
Cohen Theorem, 139, 140
Commerce Department, 125
Commons, 141, 225
Communications Decency Act (CDA),

174–75, 177–79, 216

Communism, 3–5, 8, 58, 209; and the First

Amendment, 214; and intellectual
property issues, 131, 134; in Vietnam,
188, 189

Compaq, 57
Competition, 207
Computer Fraud and Abuse Act, 195
Confidentiality, 35–36. See also Privacy
Congress, 45–47, 53–54, 69, 191, 216; Alien
and Sedition Acts, 148; Americans
with Disabilities Act, 91; CALEA
(Communications Assistance for Law
Enforcement Act), 44–46, 106; CDA
(Communications Decency Act),
174–75, 177–79; Computer Fraud and
Abuse Act, 195; COPA (Child Online
Protection Act), 177; Digital
Millennium Copyright Act, 49,
264n19; House Committee on
Impeachment, 229; Low Level

2 9 1

Radioactive Waste Policy
Amendments Act, 95–96;
Telecommunications Act of 1996, 47

Congressional Record, 168
Constitution. See Bill of Rights; specific

amendments

Contraceptives, 148
Contracts, 136, 196, 198
Controlled use, 150–56
Cookies, 34–35, 41–42
COPA (Child Online Protection Act), 177
Copyright law, 49, 88–89; and CDs, 46;

overview of, 122–41; for software, 225;
and sovereignty, 193, 197, 198, 205–6;
and trusted systems, 127–30; and Web
pages, 103. See also Intellectual
property

Cornell University, 195
Counsel Connect (CC), 71–74, 78–79, 83
Craswell, Richard, 258n45
Credentials, 28–29, 31
Credit cards: secure servers and, 39–40;
usage of, collection of data on, 19,
148, 150; validation of, 41

Crime, 21–22, 31–32, 44; drug trafficking,
94–95; hackers, 194–96; theft, 90–91,
123. See also Criminal; Drugs, illegal

Criminal: evidence, 148; trials, rights of
defendants in, 119. See also Crime

Cryptography, 35–39. See also Encryption
Cybernetics, 5
Czech Republic, 92

DAT (digital audio tape), 46–47, 49, 128
"David Lynch effect," 82
Deaf individuals, 65–66. See also Disabled

individuals

"Declaration of the Independence of
Cyberspace" (Barlow), 218

Defamation laws, 88–89
Defense Department, 4, 168, 169, 217,

282n17

Diffie-Hellman system, 36–37
Digital certificates, 35, 38–39, 42, 49–53,

176, 207–8

Digital IDs, 38–39, 41–42, 50, 54–60
Digital Millennium Copyright Act, 49,

264n19
Digital signatures, 42
Dignity, 147–48, 155, 161
Disabled individuals, 65–66, 91, 94–95, 164
Discrimination, 94, 156, 164
Distribution, 182–85
Diversity, 82
DNA, 102
Downloading, 64, 71
Drugs, illegal, 93–94, 111, 165–66
Due process, 7
Durham, Ivor, 77
DuVal, Richard, 16

East Coast Code, 53–54, 99, 221
Easterbrook, Frank, 136, 197
Education, 92–94, 126, 128. See also

Children

Effectiveness, 224
Efficiency, 156–57, 208–9
Elections, 227, 228
Ellsberg, Daniel, 168
E-mail, 49, 188, 198; through AOL, 67, 68;
content, monitoring of, 144–45; and
cryptography, 38; and free speech
rights, 167; and newbies, 64;
protocols, 195; servers, 102

Encryption, 35–40, 42, 47–49, 89; and the
Clipper chip, 47–48, 248n18, 258n53;
and free speech rights, 166; history of,
52; and monitoring practices, 157;
and secure servers, 39–40;

and sovereignty, 205
Energy Department, 170
England, 85, 138. See also Britain
Environmental issues, 95–96
EPIC (Electronic Privacy Information

Democracy, 3, 82–83, 218–20, 225–30; and

Center), 161

the courts, 214; and judicial review,
223; and virtual communities, 76–78,

Equality, 154–56, 180, 214, 217
Essence, notion of, 24–25
Europe, 3–5, 8, 58, 191, 226; and

Dibbell, Julian, 74–75
Dictatorships, 36
Diffie, Whitfield, 36

communism, 188, 209; constitutional
courts in, 92; and free speech rights,
167; and intellectual property issues,

2 9 2

Europe (cont.)

134; and monitoring practices, 159.
See also European Union; specific
countries

European Union, 55. See also Europe;

specific countries

Evidence, 148

Fair use, 134, 137–39, 197
FBI (Federal Bureau of Investigation), 17,

45–46, 146, 231

FCC (Federal Communications

Commission), 45, 166, 182, 183

Fidelity, 115, 118–19, 215
Fifth Amendment, 148
Filtering, 176–82, 186–87, 198, 233
FINGER command, 77
Fingerdaemon, 195
First Amendment, 26, 148, 165–69, 174,
203–4; clarity of, 214; Madisonian
conception of, 180–81; and television,
47. See also Free speech

"First sale" doctrine, 134
Fish, Stanley, 9
Fishkin, James, 228
Ford, Richard, 199–200
"Forget Big Brother" (Lewis), 152
Formalism, 221
Fourteenth Amendment, 120, 199, 204
Fourth Amendment, 17–18, 111–18,

148–49

France, 91, 106–7, 167, 213
Frankfurter, Felix, 183
Free software, 7–8
Free Software Foundation, 104
Free speech, 7–8, 164–85; and AOL, 69; and
publications, 168–73; and sovereignty,
196, 203–4; state suppression of, 85.
See also First Amendment

French Revolution, 91
Frequent flyer mile programs, 155
Friedman, Milton, 165
Froomkin, Michael, 39, 258n53
FTP (file transfer protocol), 101, 102

Gambling, 14, 19, 50, 54–55, 116–17, 198
Gandy, Oscar, 153
George II (king), 17–18
George III (king), 17–18

Georgetown University Law Review, 174
Germany, 92, 166, 190
Gibson, William, 5
Ginsberg v New York, 173, 175, 176, 178–79
GNU, 104–5
God, 12, 90
Godwin, Mike, 63, 254n34
Goldsmith, Jack, 193, 197
Goodale, James, 168
GPL (general public license), 105
Grant, Gail L., 40

Hackers, 194–96
Hafner, Katie, 77
Hansen, Chuck, 170
Harter, Peter, 106
Harvard Law School, 26–29, 38, 79
Headers, 28
Hellman, Martin, 36
Herz, J. C., 25–26
Hewlett Packard, 145
Hierarchies, social, 155
Holmes, Oliver Wendell, 6
Homelessness, 180
Hoover, Herbert, 182
Hotels, 92
House Committee on Impeachment, 229
HTML (HyperText Markup Language),

102, 103

HTTP (hypertext transfer protocol), 101–3
Hudgson v Minnesota, 95
Hungary, 167, 191
Hunt, 101
Hurst, Paul, 36
Hustler, 16

IBEX, 78–82
IBM (International Business Machines), 52,

59, 105, 177

Identification, 30–39, 67–68. See also

Certification

Identity, 30–34
IETF (Internet Engineering Task Force), 52,

102, 207

Ignition-locking systems, 94
Imperialism, 203
Incentives, 41
Independence Day (film), 58
Indirection, problem of, 95–98

2 9 3

Industry Standard, The, 98
Innateness, notion of, 24–25
Innocence, 152
Integrity, 40, 41, 98, 204
Intel, 105
Intellectual property, 8, 122–41, 186; and
monitoring practices, 162; promise
for, in cyberspace, 127–30. See also
Copyright law

"Intellectual Property and the National
Information Infrastructure"
(Commerce Department), 125–27

Inter–active WeekOnline, 24
Internet Engineering Task Force (IETF), 52,

102, 207

Internet Service Providers (ISPs), 51–53,

201–2

IP (Internet Protocol) addresses, 32–33, 101
IRC (Internet Relay Chat), 64. See also Chat
"Is-isms," fallacy of, 24–29
ISPs (Internet Service Providers), 51–53,

201–2

"Jake's communities," 14–17, 21, 83, 166,

190, 198

Japan, 214
Japanese Americans, 214
Java, 102
Jefferson, Thomas, 132, 141, 233
Jim Crow laws, 154
Johnson, David, 24, 71, 192–93, 201
Johnson, Steven, 154, 252n6
Jones, Martha, 9–10
Jury system, 229

Kaker, Jake, 190
Kapor, Mitch, 20
Katsh, Ethan, 90, 143
Katz, Charles, 117
Katz v United States, 116–17
Kennedy, John F., 171, 225–26
Kennedy School of Government, 220
Kids. See Children
Kids-ID box, 176, 177, 179
Kundera, Milan, 193

Labor movement, 85
Laffer Curve, 94

Laissez-faire policy, 87, 163, 206
LamdaMOO, 74–78, 83. See also MOOs

(virtual worlds)

Latent ambiguity, 22–23, 110, 119–20, 223;
in agreements, 149; and codifying
constitutions, 215; and democracy,
227; and free speech rights, 181; and
sovereignty, 191; and translation,
211–12

.law.cyber newsgroup, 78–83. See also

Newsgroups

Lawyers, vilification of, 229–30. See also CC

(Counsel Connect);

.law.cyber newsgroup
Legal cases: Brown v Board of Education,
214; Ginsberg v New York, 173, 175,
176, 178–79; Hudgson v Minnesota,
95; Katz v United States, 116–17;
Maher v Roe, 95; Maryland v Craig,
119; Near v Minnesota, 169; New York
v United States, 96, 97, 98; Olmstead v
United States, 111–12, 114, 116–17,
149; ProCD v Zeidenberg, 136; Roe v
Wade, 95; Rust v Sullivan, 95–98;
Shelley v Kramer, 97

Legi s l a ti on : Al i en and Sed i ti on Act s ,1 4 8 ;
Am ericans with Di s a bi l i ties Act ,9 1 ;
CALEA (Com mu n i c a ti ons As s i s t a n ce
for Law Enforcem ent Act ) ,4 4 – 4 6 ,
1 0 6 ;C DA (Com mu n i c a ti ons Decen c y
Act ) ,1 7 4 – 7 5 ,1 7 7 – 7 9 ; Com p uter
Fraud and Abuse Act ,1 9 5 ;C O PA
( Child Online Pro tecti on Act ) ,1 7 7 ;
Di gital Mi ll en n ium Copyri ght Act ,
4 9 ,2 6 4n1 9 ; Low Level Rad i oactive
Wa s te Policy Am en d m ents Act ,
9 5 – 9 6 ; Tel ecom mu n i c a ti ons Act of
1 9 9 6 ,4 7
Lemley, Mark, 225
Lenin, V. I., 188
Lewis, Peter, 152
Lexis, 34, 72
Liability, 10, 112–13, 161, 232
Libertarianism, 3–6, 54–55, 219; and

Declan, 232; and Mill, 85; and Net95,
28–29; and sovereignty, 206
Licenses: click-wrap (shrink-wrap), 135,
206; general public (GPL), 105

Limbaugh, Rush, 221
Linux, 105
Litman, Jessica, 193

2 9 4

Louisiana purchase, 217
Low Level Radioactive Waste Policy
Amendments Act, 95–96

Lyon, Matthew, 77

MacArthur Foundation, 104
McCullagh, Declan, 231–33
Maddox, Tom, 6
Maher v Roe, 95
Malpractice insurance, 172
Marshall, Thurgood, 92–93, 220
Marx, Karl, 5, 188
Maryland v Craig, 119
Meares, Tracey, 94
Merkle, Ralph, 127
Microsoft, 6, 177; Windows, 104, 105;

Word, 144, 221, 286n23

MicroWarehouse, 38
Mill, John Stuart, 85
Minimalism, 33
MIT (Massachusetts Institute of

Technology), 53

Mitchell, John, 169
Mitchell, William, 6, 60, 89–90
Mnookin, Jennifer, 78
Mobility, economic, 155
Modularity, 225
Monarchy, 17–18
Monitoring, 143–63
MOOs (virtual worlds), 11–12, 13, 64;
LamdaMOO, 74–78, 83; tinySex
behavior in, 142–43

Morland, Howard, 170
Morris, Robert Tappin, 195
Moses, Robert, 92
Motion Picture Association, 47
Mozilla, 105
MP3 file format, 49
MUDs (virtual worlds), 11–12, 13, 74,

284n41; competition among, 202;
spoofing someone's identity in, 89;
tinySex behavior in, 142–43

Mysticism, 64

Napoleon III, 91
National Enquirer, 171–72
Na ti onal Scien ce Fo u n d a ti on (NSF), 3 9 ,2 1 9

National Security Agency (NSA), 17, 35,

144, 145

National Transportation Safety Board

(NTSB), 171

Nature, concept of, 24–25, 30, 82
Nazi Party, 166
Near v Minnesota, 169
Negroponte, Nicholas, 28, 226, 264n15
Net95, 27–28, 33, 53
Netizens, 90
Netscape, 39–40, 52, 105–6, 176–77; and

PICS, 177; and SSL, 106

Network Associates, 52
Network Solutions, 219
"Newbies," 64
New Deal, 159
Newsgroups, 15, 64, 72, 81, 170, 174; AOL

access to, 68; .law.cyer newsgroup,
78–83

News reporting, 228
Newsweek, 174
New Yorker, The, 28
New York Times, 25–26, 129, 152, 168–72,

179–180, 183

New York v United States, 96, 97, 98
Nike, 4, 152
Nixon, Richard M., 229
NNTP (Network News Transfer Protocol),

Nonprofit organizations, 219–20
Nonrepudiation, 40
Norms, 85–88, 92–95, 123, 159–60, 235–38;

and free speech rights, 164–65, 173;
use of the term, 235

North Korea, 167
NSA (National Security Agency), 17, 35,

144, 145

NTSB (National Transportation Safety

Board), 171
Nuclear waste, 95–96

O'Brian, David, 225
Obscenity laws, 88–89
Olmstead v United States, 111–12, 114,

116–17, 149
On Liberty (Mill), 85
Open code, 7, 224–25
Open source software, 7–8, 100–108

2 9 5

Originalism, one-step, 114
OSI (open systems interconnect) model,

Ownership, 7–8, 13, 61

P3P, 160, 162–63, 177, 181
Packets, 28, 32, 44
"Panoptic sort," 153
Parking garages, 92
Parking tickets, 90–91
Passwords, 34–35
Pearl Harbor, 214
Pentagon Papers, 168–70, 172
PGP (Pretty Good Privacy), 52
Photocopying, 124, 128, 168
PICS, 177–78, 181
PKI (public key infrastructure), 38, 41, 52
Polling, 228
Pornography, 15–17, 33, 191; and free

speech rights, 173–75; in Vietnam,
189; and virtual communities, 74–75

Posner, Richard, 45, 165
Post, David, 24, 192–93, 201–2
Post, Robert, 116
Postel, Jon, 219
PowerPC chip, 105
Press-Connection, 170
Printing press, 124, 183
Privacy, 8, 142–63, 186–87, 217; and the Bill
of Rights, 7; conception of, choosing,
149–50; as dignity, 147–48; to
minimize burden, 146–47; and
protocols, 40–41; reasonable
expectation of, notion of, 117–18; and
search and seizure, 112–14; and
sovereignty, 206, 208; as substantive,
148–49; and trespass law, 111–14; and
wiretapping, 111–12, 114, 116–17,
139, 149; and worms, 17–19, 23. See
also Confidentiality

Privacy Now! (organization), 161
ProCD v Zeidenberg, 136
Profiles in Courage (Kennedy), 225
Profiling, 155
Progressive, The, 170
Prohibition, 111
Property law, 122–23, 130–35; and

sovereignty, 198. See also Intellectual
property

Protocols, 32–33, 89; four layers of, 101–2;
and free speech rights, 166, 184;
Internet mail, 195; and monitoring
practices, 160; and open source
software, 101–2, 106; and sovereignty,
106, 195

Pseudonyms, 82
Public forums, 69
Public key encryption, 35–39, 40. See also

Encryption

Public transportation, 92
Punishment, 85, 90–91, 125, 214

Radio, 182–85
Radio Act, 182
Rand, Ayn, 131
RAND Corporation, 168
Rape, 75
Rating systems, 47, 279n46
Reagan, Ronald, 96
Reconstruction, 226
Reeves, Harold, 122–23
Reid, Elizabeth, 74
Rehnquist, William, 215
Roe v Wade, 95
Rotenberg, Marc, 161
Router technology, 52–53
Russia, 5–6, 207
Rust v Sullivan, 95–98

Salinger, Pierre, 171
Scalia, Anthony, 97, 147–48
Scanning, 128
Screen names, 34, 67–68
Search and seizure, 112–14
Search engines, 123, 153
Seatbelts, 93–94, 224, 257n34
Sedition, evidence of, 148
Segregation, 98, 154, 164, 214
Self-regulation, 159, 287n11
Self-sufficiency, 130
SENDMAIL, 104, 195
Servers, 39–40, 42, 55, 198, 207
SET (secure electronic transaction)

monitoring practices, 159–62; and

protocol, 40

2 9 6

Shamans, Software, and Spleens (Boyle), 141
Shapiro, Andrew, 233
Shelley v Kramer, 97
Shrink-wrap (click-wrap) licenses, 135, 206
Sixth Amendment, 148
Skorkin, Michael, 239
Slavery, 204–5, 214, 226
Smoking, 87, 91
SMTP (simple mail transport protocol),

101, 102

Sola Pool, Ithiel de, 180–81
Soros, George, 108, 165–66
Sovereignty, 8, 21–22, 187–209
Soviet Union, 107, 182, 185, 234
SSL (secure socket layer) protocol, 39, 40,

Stalin, Josef, 107, 125
Stallman, Richard, 104, 105
Stanford Law Review, 24
States, jurisdiction of, 54–56, 198, 203
Stefik, Mark, 6, 127–29, 135, 137
Steinert-Threlkeld, Tom, 24
Stewart, Potter, 117–18
Stone, Geof, 26, 181
Streets, design of, 92
Stuntz, William, 45, 148
Subjection of Women, The (Mill), 85
Sunstein, Cass, 149, 180, 181
Sweden, 207
Switching technologies, 44

Taft, William H., 114–17, 144
Taiwan, 56, 177
Taxation, 50–51, 69, 91
TCP/IP (Transmission Control

Protocol/Internet Protocol), 27,
32–34, 101–2, 175, 211

Telecommunications Act of 1996, 47
Telegraph, 39
Telephone(s), 19, 44–46, 106, 157; cellular,

45–46, 146; records, 148, 150; and
sovereignty, 196. See also Wiretapping

Television, 47, 124–25; and free speech

rights, 166; shows, lifestyle alternatives
portrayed in, 191; and sovereignty,

Theft, 90–91, 123. See also Crime
Themes, 19–23
Thumbprint readers, 57–58

Tiebout, Charles, 201
Time, 174
Tipping, 155–56
Tocqueville, Alexis de, 229
Tomlin, Lily, 39
Torvalds, Linus, 104
Traceability, 51, 140
Trademarks, 206. See also Intellectual

property

Transformative constitution, 213–14
Transience, 82
Translation, 109–21, 158, 222–23; and

intellectual property issues, 139, 149;
and latent ambiguities, 211–12; use of
the term, 261n15
Transparency, 96, 224, 225
Trespass law, 111–14, 117, 198
Tribe, Laurence, 117–19
Trusted systems, 127–30, 135, 137–39,

205–6

TWA Flight 800, 171, 172
Twilight of Sovereignty, The (Wriston), 206

UDP (User Datagram Protocol), 101
"Ugly" individuals, 65–66
Unger, Roberto, 59
University of Chicago, 3, 26, 27, 79, 122
University of Helsinki, 104
University of Illinois, 53
University of Michigan, 21
UNIX, 77, 194
USENET newsgroups, 15, 64, 72, 81, 170,
174; AOL access to, 68;.law.cyer
newsgroup, 78–83

Utopianism, 4, 29

V-chip, 47, 106
Verification, 34–35. See also Authentication
VeriSign, 38, 246n31
Videotape, 74, 124–25, 145–148, 151
Vietnam, 168, 188, 189
Village Voice, 74
Vinge, Vernor, 6
Violent content, 15–17, 74–75
Virtual reality, 74–78, 83. See also MOOs

(virtual worlds); MUDs (virtual
worlds)
Viruses, 17, 71

2 9 7

Visa, 40
V-mail (voice mail), 145
Vote, right to, 199–200, 209, 214

W3C (World Wide Web Consortium), 102,

Wall, the, 79–80
Wall Street Journal, 179–180, 183
Warrants, 112–13
Warren, Earl, 45, 215
Warren, Robert, 170
Warren Court, 45, 215
Weapons, concealed, 158
Web browsers: access control features for,
176–77; and cookies, 34–35, 41–42;
and intellectual property issues, 123;
and protocols, 102. See also Web sites
Web sites: access control and, 176–77; and

data collection techniques, 153–54;
and free speech rights, 167; and
sovereignty, 195. See also Web
browsers; World Wide Web

Webster, Daniel, 225–26
WELL, The, 63, 64
West Coast Code, 53–54, 98–99, 221
White Papers, 125–27, 219
Williams, Bernard, 120

Windows (Microsoft), 104, 105
Winn, Jane, 39
Wired News, 231
Wiretapping, 111–12, 114, 116–17, 139, 149
Wood, Gordon, 154
Word (Microsoft), 144, 221, 286n23
World War II, 205, 214
World Wide Web, 66, 102–3. See also Web

browsers; Web sites

World Wide Web Consortium (W3C), 102,

Worms, 17–19, 22, 110, 144–50, 195
Wriston, Walter, 206
Wu, Tim, 102

Xerox PARC, 127

Y2K issues, 104, 231–32
Yahoo!, 35
Yale Law School, 79, 82, 168

Zelizer, Viviana, 155–56
Zoning, 28, 57, 216; and free speech rights,
175–79, 181; and the ideal of equality,
154; and segregation, 98

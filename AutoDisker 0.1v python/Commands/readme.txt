A)

Program executes our .txt files in sequence.

first: 'commands.txt'
(2sec sleep)
second: 'commands1.txt'
(2sec sleep)
third: 'commands2.txt'
(2sec sleep)

and so on.

B)

Every .txt file called 'commands.txt', 'commands1' etc. you can edit depends on your needs.
for example: 'commands.txt' contains code: 

"

select volume 1
assign mount = C:\our_directories\hard_drive-1
select volume 2
assign mount = C:\our_directories\hard_drive-2
select volume 3
assign mount = C:\our_directories\hard_drive-3
select volume 4
assign mount = C:\our_directories\hard_drive-4
select volume 5
assign mount = C:\our_directories\hard_drive-5
select volume 6
assign mount = C:\our_directories\hard_drive-6
select volume 7
assign mount = C:\our_directories\hard_drive-7
select volume 8
assign mount = C:\our_directories\hard_drive-8
select volume 9
assign mount = C:\our_directories\hard_drive-9
select volume 10
assign mount = C:\our_directories\hard_drive-10

"
you can change anything you want eg:
select volume 1
assign mount = C:\our_directories\hard_drive-1
select volume 2
assign mount = C:\our_directories\hard_drive-2
select volume 3
assign mount = C:\our_directories\hard_drive-3
select volume 4
assign mount = C:\our_directories\hard_drive-4
select volume 5
assign mount = C:\our_directories\hard_drive-5
select volume 6
assign mount = C:\our_directories\hard_drive-6
select volume 7
assign mount = C:\our_directories\hard_drive-7
select volume 8
assign mount = C:\our_directories\hard_drive-8
select volume 9
assign mount = C:\our_directories\hard_drive-9
select volume 10
assign mount = C:\our_directories\hard_drive-10

change to:

hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world

----------------------------------------------------------------------------------


C) you can leave only one .txt file to execute.
just delete rest of them and leave for example 'commands.txt' alone.
save it and run.
if you don't want to delete them just delete the content in .txt files, but don't delete .txt files or just make a backup of them and when you'll need them just copy and paste to the directory.

D) if you want to put more than 60 disks into folders that you made just go to edit 'commands.txt'  from:
select volume 1
assign mount = C:\our_directories\hard_drive-1
select volume 2
assign mount = C:\our_directories\hard_drive-2
select volume 3
assign mount = C:\our_directories\hard_drive-3
select volume 4
assign mount = C:\our_directories\hard_drive-4
select volume 5
assign mount = C:\our_directories\hard_drive-5
select volume 6
assign mount = C:\our_directories\hard_drive-6
select volume 7
assign mount = C:\our_directories\hard_drive-7
select volume 8
assign mount = C:\our_directories\hard_drive-8
select volume 9
assign mount = C:\our_directories\hard_drive-9
select volume 10
assign mount = C:\our_directories\hard_drive-10

add:

select volume 1
assign mount = C:\our_directories\hard_drive-1
select volume 2
assign mount = C:\our_directories\hard_drive-2
select volume 3
assign mount = C:\our_directories\hard_drive-3
select volume 4
assign mount = C:\our_directories\hard_drive-4
select volume 5
assign mount = C:\our_directories\hard_drive-5
select volume 6
assign mount = C:\our_directories\hard_drive-6
select volume 7
assign mount = C:\our_directories\hard_drive-7
select volume 8
assign mount = C:\our_directories\hard_drive-8
select volume 9
assign mount = C:\our_directories\hard_drive-9
select volume 10
assign mount = C:\our_directories\hard_drive-10
select volume 1
assign mount = C:\our_directories\hard_drive-11
select volume 2
assign mount = C:\our_directories\hard_drive-12
select volume 3
assign mount = C:\our_directories\hard_drive-13
select volume 4
assign mount = C:\our_directories\hard_drive-14
select volume 5
assign mount = C:\our_directories\hard_drive-15
select volume 6
assign mount = C:\our_directories\hard_drive-16
select volume 7
assign mount = C:\our_directories\hard_drive-17
select volume 8
assign mount = C:\our_directories\hard_drive-18
select volume 9
assign mount = C:\our_directories\hard_drive-19
select volume 10
assign mount = C:\our_directories\hard_drive-20

just add some code in .txt files and save it.



# 0x03. Shell, init files, variables and expansion

## Expansion
- With expansion, we type something and it is expanded into something else before the shell can acts upon it.
- "*" is wildcards for matching any characters in a filename.

## Pathname Expansion
- Example
	1. `echo /usr/*/share`
	2. `echo *s`

## Tilde Expansion
- Tilde character ("~") has a special meaning. When used at the beginning of a word, it expands into name of the home directory of the named user, or if no user is named, the home directory of the current user.
- Example 
	- `echo ~`

## Arithmetic Expansion
- The shell allows arithmetic to be performed by expansion. This allow us to use te shell prompt as a calculator.
- Example
	- `echo $((20 * 45))`
- Arithmetic expansion uses the form:
	- `$((expression))`
	
## Brace Expansion
- With brace expansion, we can create multiple text strings from a pattern containing braces.
- Example
	1. `echo Front-{A,B,C}-Back`    Output    `Front-A-Back Front-B-Back Front-C-Back`
	2. `echo Number_{1..5}`
	3. `echo {Z..A}`
	4. `echo a{A{1,2},B{3,4}}b`

## Parameter Expansion
- Many of its capabilities have to do with system's ability to store small chunks of data and to give each chunk a name. Many such chunks, more properly called variables, are available for examination.
- Example
	1. The variable `USER` contains our user name.
		-`echo $USER`
	To see a list available variables
		- `printenv | less`
		
## Command Substitution
- Allows us to use the output of a command as an expression:
- Example
	1. `echo $(ls)`
	2. `ls -l $(which cp)`

## Quoting

## Escape characters
1. \n
2. \t
3. \\
4. \a
5. \f

## Alias Command

- Lets you create shortcuts for long commands, making them easier to remember and use.
- It will the same functionality as if the whole command is run.

### How to create your own linux commands

- Using the `alias` command, you'll able to create your own commands. It's so simple to create your own commands.
- Here's the syntax for the `alias` command:

	`alias [alias-name[=string]...]`

- Example:
	Assume that you want to create a command called `cdv`, and entering the command in the terminal should take you to the videos directory

	`alias cdv="cd Videos"`

### How to View Created Alias Commands

`alias -p`

### How to Remove an Alias Command in Linux
- Syntax
	`unalias alias-name`

### How to Remove All Alias Commands in Linux
	`unalias -a`

	More on aliases visit https://www.freecodecamp.org/news/how-to-create-your-own-command-in-linux/
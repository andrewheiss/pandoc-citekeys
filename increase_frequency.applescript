# Set a custom TextExpander group refresh time
#
# Change the values for groupName and refreshTime and run the script.
#
# Returns 0 if nothing was changed, 1 if a group was successfully changed
#
# Note from Brian at TextExpander support:
#     Once the script runs, the popup menu showing the update frequency for that
#     group will be "weird". It should hold your custom minute setting until or
#     unless you actually mess with the popup -- then it might change it to one of
#     the pre-set values.

set groupName to "citekeys"
set refreshTime to 120

set changeCount to 0
tell application "TextExpander"
	repeat with theGroup in groups
		if (((name of theGroup) = groupName) and ((source of theGroup) ­ "")) then
			set update frequency of theGroup to refreshTime
			set changeCount to changeCount + 1
		end if
	end repeat
end tell
return changeCount

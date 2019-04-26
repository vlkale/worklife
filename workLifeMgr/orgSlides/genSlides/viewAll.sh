make clean
make privateNotes
open privateNotes.pdf
make publicNotes
open publicNotes.pdf
make uSchedPoster-vk
open uSchedPoster-vk.pdf
make codingNotes
open codingNotes.pdf

echo "generating workNotes"
make workNotes
open workNotes.pdf

echo "generating lifeNotes"
make lifeNotes
open lifeNotes.pdf

echo "all pdf generation complete"


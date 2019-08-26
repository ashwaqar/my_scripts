ls -lrth
ls -lrth | wc -l
ls -lrth > shell_results.txt
ls -lrth | wc -l >> shell_results.txt
echo "Results saved to shell_results.txt"
cat shell_results.txt
mkdir testing_copy

for f in *.txt
do
   cp -v "$f" testing_copy/"${f%.txt}"$(date +%m%d%y).txt
done

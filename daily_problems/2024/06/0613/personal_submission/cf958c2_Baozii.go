package main
 
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)
 
func main() {
	reader := bufio.NewReader(os.Stdin)
	input := readInts(reader)
	n, k, p := input[0], input[1], input[2]
	nums := readInts(reader)
	for i := range nums {
		nums[i] = nums[i] % p
	}
 
	acc := make([]int, n+1)
	for i := 1; i <= n; i++ {
		acc[i] = acc[i-1] + nums[i-1]
	}
 
	dp := make([]int, k)
	idx := make([]int, k)
 
	for i := 1; i < n; i++ {
		for j := k - 1; j > 0; j-- {
			if dp[j-1]+(acc[i]-acc[idx[j-1]])%p > dp[j] {
				dp[j] = dp[j-1] + (acc[i]-acc[idx[j-1]])%p
				idx[j] = i
			}
		}
	}
 
	fmt.Println(dp[k-1] + (acc[n] - acc[idx[k-1]]) % p)
}
 
func readInts(reader *bufio.Reader) (result []int) {
	line, _ := reader.ReadString('\n')
	strs := strings.Fields(line)
	for _, str := range strs {
		num, _ := strconv.Atoi(str)
		result = append(result, num)
	}
	return
}

package main

import "fmt"

func trap(height []int) int {
    var water int
    n := len(height)
    if n == 0 {
        return 0 
    }
    var i int = 0
    for i < n {
        if height[i] == 0 {
            i++
            continue
        }
        var maxIndex int = -1
        var maxHeight int = 0
        var waterLine int = 0
        for j := i + 1; j < n; j++ {
            if height[j] >= height[i] {
                maxIndex = j
                waterLine = height[i]
                break
            } else if height[j] > maxHeight {
                maxHeight = height[j]
                maxIndex = j
            }
        }

        if maxIndex != -1 {
            if waterLine == 0 { 
                waterLine = maxHeight
            }
            var blockWater int = 0
            for k := i + 1; k < maxIndex; k++ {
                blockWater += height[k]
            }
            water += (maxIndex - i - 1) * waterLine - blockWater
            i = maxIndex
        } else {
            i++
        }
    }

    return water
}

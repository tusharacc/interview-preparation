
async function selectionSort<T>(array: T[]): Promise<T[]> {
 
    let index: number = 0;
    while (index < array.length-1){
        let innerIndex: number = index + 1;
        while (innerIndex < array.length){
            if (array[index] > array[innerIndex]){
                [array[index], array[innerIndex]] = [array[innerIndex], array[index]]
            }
            innerIndex += 1
            
        }
        
        index += 1;
    }

    return array
}

const numberArray: number[] = [5,2,9,1,-8,4]
console.log("Sorted number array:", selectionSort(numberArray));

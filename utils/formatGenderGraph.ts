type DataType = {
  性別: string
  小計: number
}

export type GraphDataType = {
  label: string
  transition: number
  cumulative: number
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType[]) => {
  const graphData: GraphDataType[] = []
  let patSum = 0
  data.forEach(d => {
    const gender = d['性別']
    const subTotal = d['小計']
    if (!isNaN(subTotal)) {
      patSum += subTotal
      graphData.push({
        label: gender,
        transition: subTotal,
        cumulative: patSum
      })
    }
  })
  return graphData
}

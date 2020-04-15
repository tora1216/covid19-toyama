type DataType = {
  年代: string
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
    const age = d['年代']
    const subTotal = d['小計']
    if (!isNaN(subTotal)) {
      patSum += subTotal
      graphData.push({
        label: age,
        transition: subTotal,
        cumulative: patSum
      })
    }
  })
  return graphData
}

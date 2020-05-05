type DataType = {
  children: [
    {
      attr: '陽性人数'
      value: number
    },
    {
      attr: '陰性人数'
      value: number
    }
  ]
}

type TestedCasesType = {
  陽性率: number
  累計人数: number
  陽性人数: number
  陰性人数: number
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType) => {
  const formattedData: TestedCasesType = {
    陽性率: (Math.round(data.children[0].value / (data.children[0].value + data.children[1].value) * 100 * 10)) / 10,
    累計人数: data.children[0].value + data.children[1].value,
    陽性人数: data.children[0].value,
    陰性人数: data.children[1].value
  }
  return formattedData
}

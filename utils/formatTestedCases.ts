type DataType = {
  children: [
    {
      attr: '陽性患者数'
      value: number
    },
    {
      attr: '陰性患者数'
      value: number
    }
  ]
}

type TestedCasesType = {
  累計件数: number
  累計人数: number
  陽性患者数: number
  陰性患者数: number
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType) => {
  const formattedData: TestedCasesType = {
    累計件数: data.children[0].value + data.children[1].value,
    累計人数: data.children[0].value + data.children[1].value,
    陽性患者数: data.children[0].value,
    陰性患者数: data.children[1].value
  }
  return formattedData
}

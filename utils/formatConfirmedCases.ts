type DataType = {
      attr: '陽性患者数'
      value: number
      children: [
        {
          attr: '入院中'
          value: number
          children: [
            {
              attr: '無症状・軽症・中等症'
              value: number
            },
            {
              attr: '重症'
              value: number
            }
          ]
        },
        {
          attr: '死亡'
          value: number
        },
        {
          attr: '退院'
          value: number
        }
      ]
}

type ConfirmedCasesType = {
  陽性患者数: number
  入院中: number
  無症状軽症中等症: number
  重症: number
  死亡: number
  退院: number
}

/**
 * Format for *Chart component
 *
 * @param data - Raw data
 */
export default (data: DataType) => {
  const formattedData: ConfirmedCasesType = {
    陽性患者数: data.value,
    入院中: data.children[0].value,
    無症状軽症中等症: data.children[0].children[0].value,
    重症: data.children[0].children[1].value,
    死亡: data.children[1].value,
    退院: data.children[2].value
  }
  return formattedData
}

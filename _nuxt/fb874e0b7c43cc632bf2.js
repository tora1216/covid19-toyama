(window.webpackJsonp=window.webpackJsonp||[]).push([[14],{516:function(e,t,r){"use strict";r.r(t);var o=r(351),n=r(410),c=r(409),d=r(412),m=r(423),h=r(414),l=r(418),f=r(422),$=r(421),v=r(413),_=r(416),C=r(355),y={components:{TimeBarChart:r(361).a},data:function(){var e=Object(C.a)(o.inspection_persons.data),data={Data:o,graphData:e};return data}},k=r(4),D=Object(k.a)(y,(function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("v-col",{staticClass:"DataCard",attrs:{cols:"12",md:"6"}},[r("time-bar-chart",{attrs:{title:e.$t("検査実施人数"),"title-id":"number-of-inspection-persons","chart-id":"number-of-inspection-persons","chart-data":e.graphData,date:e.Data.inspection_persons.date,unit:e.$t("人"),url:"http://opendata.pref.toyama.jp/dataset/covid19"},scopedSlots:e._u([{key:"description",fn:function(){return[r("ul",{},[r("li",[e._v("\n          "+e._s(e.$t("（注）日付は検査結果判明日を基準にしている"))+"\n        ")]),e._v(" "),r("li",[e._v("\n          "+e._s(e.$t("（注）2/27には、2/26までの累計数を含む"))+"\n        ")]),e._v(" "),r("li",[e._v("\n          "+e._s(e.$t("（注）医療機関等実施分および抗原検査分は含まれていない"))+"\n        ")]),e._v(" "),r("li",[e._v("\n          "+e._s(e.$t("（注）把握には一定の期間を要しており、更新日の情報とは異なる場合あり"))+"\n        ")])])]},proxy:!0}])})],1)}),[],!1,null,null,null).exports,w=r(415),N=r(420),P=r(419),T=r(417),j={components:{ConfirmedCasesDetailsCard:d.a,ConfirmedCasesNumberCard:m.a,ConfirmedCasesAttributesCard:h.a,PatientsByResidenceCard:l.a,DeadPersonsNumberCard:f.a,DischargedPersonsNumberCard:$.a,TestedCasesDetailsCard:v.a,PositiveRateCard:_.a,InspectionPersonsNumberCard:D,TestedCasesNumberCard:w.a,TelephoneAdvisoryReportsNumberCard:N.a,ConsultationDeskReportsNumberCard:P.a,PopulationCard:T.a},data:function(){var title,e;switch(this.$route.params.card){case"details-of-confirmed-cases":title=this.$t("検査陽性者の状況"),e=o.main_summary.date;break;case"number-of-confirmed-cases":title=this.$t("陽性患者数"),e=o.patients_summary.date;break;case"attributes-of-confirmed-cases":title=this.$t("陽性患者の属性"),e=o.patients.date;break;case"patients-by-residence":title=this.$t("陽性患者数(居住地別)"),e=o.patients_by_residence.date;break;case"number-of-dead-persons":title=this.$t("死亡者数"),e=o.dead_persons.date;break;case"number-of-discharged-persons":title=this.$t("退院者数"),e=o.discharged_persons.date;break;case"details-of-tested-cases":title=this.$t("検査実施状況"),e=o.inspection_status_summary.date;break;case"rate-of-confirmed-cases":title=this.$t("検査陽性率"),e=o.positive_rate.date;break;case"number-of-inspection-persons":title=this.$t("検査実施人数"),e=o.inspection_persons.date;break;case"number-of-tested-cases":title=this.$t("検査実施数"),e=c.date;break;case"number-of-reports-to-covid19-telephone-advisory-center":title=this.$t("新型コロナウイルス感染症に関する一般相談件数"),e=o.contacts.date;break;case"number-of-reports-to-covid19-consultation-desk":title=this.$t("帰国者・接触者相談センターへの相談件数"),e=o.querents.date;break;case"changes-of-population-around-toyama-station":title=this.$t("富山駅周辺の人口の推移（参考値）"),e=n.date}var data={title:title,updatedAt:e};return data},head:function(){var e="https://stopcovid19-toyama.netlify.app/",t=(new Date).getTime(),r="ja"===this.$i18n.locale?"".concat(e,"/ogp/").concat(this.$route.params.card,".png?t=").concat(t):"".concat(e,"/ogp/").concat(this.$i18n.locale,"/").concat(this.$route.params.card,".png?t=").concat(t),o="".concat(this.updatedAt," | ").concat(this.$t("当サイトは新型コロナウイルス感染症 (COVID-19) に関する最新情報を提供するために、有志が開設したものです。"));return{title:this.title,meta:[{hid:"og:url",property:"og:url",content:e+this.$route.path+"/"},{hid:"og:title",property:"og:title",content:this.title+" | "+this.$t("富山県公認")+" "+this.$t("新型コロナウイルス感染症")+" "+this.$t("対策サイト")},{hid:"description",name:"description",content:o},{hid:"og:description",property:"og:description",content:o},{hid:"og:image",property:"og:image",content:"https://raw.githubusercontent.com/Terachan0117/covid19-toyama/development/static/ogp.png"},{hid:"twitter:image",name:"twitter:image",content:r}]}}},A=Object(k.a)(j,(function(){var e=this.$createElement,t=this._self._c||e;return t("div",["details-of-confirmed-cases"==this.$route.params.card?t("confirmed-cases-details-card"):"number-of-confirmed-cases"==this.$route.params.card?t("confirmed-cases-number-card"):"attributes-of-confirmed-cases"==this.$route.params.card?t("confirmed-cases-attributes-card"):"number-of-confirmed-cases-by-residence"==this.$route.params.card?t("patients-by-residence-card"):"number-of-dead-persons"==this.$route.params.card?t("dead-persons-number-card"):"number-of-discharged-persons"==this.$route.params.card?t("discharged-persons-number-card"):"details-of-tested-cases"==this.$route.params.card?t("tested-cases-details-card"):"rate-of-confirmed-cases"==this.$route.params.card?t("positive-rate-card"):"number-of-inspection-persons"==this.$route.params.card?t("inspection-persons-number-card"):"number-of-tested-cases"==this.$route.params.card?t("tested-cases-number-card"):"number-of-reports-to-covid19-telephone-advisory-center"==this.$route.params.card?t("telephone-advisory-reports-number-card"):"number-of-reports-to-covid19-consultation-desk"==this.$route.params.card?t("consultation-desk-reports-number-card"):"changes-of-population-around-toyama-station"==this.$route.params.card?t("population-card"):this._e()],1)}),[],!1,null,null,null);t.default=A.exports}}]);
(window.webpackJsonp=window.webpackJsonp||[]).push([[17],{349:function(t,e,n){var content=n(352);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(11).default)("5d594f7f",content,!1,{sourceMap:!1})},351:function(t,e,n){"use strict";var r=n(349);n.n(r).a},352:function(t,e,n){(e=n(10)(!1)).push([t.i,".header[data-v-174a4490]{display:flex;align-items:flex-end;flex-wrap:wrap}.pageTitle[data-v-174a4490]{font-size:30px;font-size:1.875rem;color:#4d4d4d;display:flex;align-items:center;line-height:1.35;font-weight:normal;margin:0 .5em 0 0}@media screen and (max-width: 600px){.pageTitle[data-v-174a4490]{font-size:20px;font-size:1.25rem}}",""]),t.exports=e},354:function(t,e,n){"use strict";var r=n(2).default.extend({props:{icon:{type:String}}}),o=(n(351),n(4)),component=Object(o.a)(r,(function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"header"},[e("h2",{staticClass:"pageTitle"},[this.icon?e("v-icon",{staticClass:"mr-2",attrs:{size:"40"}},[this._v("\n      "+this._s(this.icon)+"\n    ")]):this._e(),this._v(" "),this._t("default")],2)])}),[],!1,null,"174a4490",null);e.a=component.exports},383:function(t,e,n){var content=n(460);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(11).default)("6239357a",content,!1,{sourceMap:!1})},395:function(t,e,n){var content=n(486);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,n(11).default)("29fcb188",content,!1,{sourceMap:!1})},459:function(t,e,n){"use strict";var r=n(383);n.n(r).a},460:function(t,e,n){(e=n(10)(!1)).push([t.i,".StaticInfo{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;background-color:#fff;border:1px solid #d9d9d9;box-shadow:0 0 2px rgba(0,0,0,.15);border-radius:4px;padding:.5em 1em;font-size:14px;font-size:0.875rem;color:#006ca8 !important;text-decoration:none}.StaticInfo:hover{text-decoration:underline}.StaticInfo-Button{flex:1 0 auto;text-align:right}.StaticInfo-Button>span{padding:4px 8px;font-size:14px;font-size:0.875rem;display:inline-block;border-radius:4px;background-color:#fff;border:1px solid #008830;color:#008830;cursor:pointer}.StaticInfo-Button>span:hover{background-color:#008830;color:#fff}.StaticInfo-Button>span:hover>i{color:#fff !important}@media screen and (max-width: 600px){.StaticInfo-Button{margin-top:4px}}",""]),t.exports=e},461:function(t){t.exports=JSON.parse('{"newsItems":[]}')},485:function(t,e,n){"use strict";var r=n(395);n.n(r).a},486:function(t,e,n){(e=n(10)(!1)).push([t.i,".MainPage .Header[data-v-99b6c1fe]{display:flex;flex-wrap:wrap;align-items:flex-end}@media screen and (max-width: 600px){.MainPage .Header[data-v-99b6c1fe]{flex-direction:column;align-items:baseline}}.MainPage .UpdatedAt[data-v-99b6c1fe]{font-size:14px;font-size:0.875rem;color:#707070;margin-bottom:.2rem}.MainPage .Annotation[data-v-99b6c1fe]{font-size:12px;font-size:0.75rem;color:#707070}@media screen and (min-width: 601px){.MainPage .Annotation[data-v-99b6c1fe]{margin:0 0 0 auto}}.MainPage .TwitterTimelineBlock[data-v-99b6c1fe]{margin:20px 0;background-color:#fff;box-shadow:0 0 2px rgba(112,15,15,.15);border:.5px solid #d9d9d9 !important;border-radius:4px;padding:10px}.MainPage .TwitterTimelineBlock .EmbeddedTwitterTimeline[data-v-99b6c1fe]{display:block;width:50%;margin:auto}@media screen and (max-width: 768px){.MainPage .TwitterTimelineBlock .EmbeddedTwitterTimeline[data-v-99b6c1fe]{width:75%}}@media screen and (max-width: 600px){.MainPage .TwitterTimelineBlock .EmbeddedTwitterTimeline[data-v-99b6c1fe]{width:100%}}.MainPage .EmergencyBlock[data-v-99b6c1fe]{margin:20px 0;background-color:#fff;box-shadow:0 0 2px rgba(112,15,15,.15);border:.5px solid #d9d9d9 !important;border-radius:4px;padding:10px}.MainPage .EmergencyBlock .EmergencyImage[data-v-99b6c1fe]{display:block;width:50%;margin:auto}@media screen and (max-width: 768px){.MainPage .EmergencyBlock .EmergencyImage[data-v-99b6c1fe]{width:75%}}@media screen and (max-width: 600px){.MainPage .EmergencyBlock .EmergencyImage[data-v-99b6c1fe]{width:100%}}.MainPage .DataBlock[data-v-99b6c1fe]{margin:20px -8px}@media screen and (min-width: 769px){.MainPage .DataBlock .DataCard[data-v-99b6c1fe]{padding:10px}}@media screen and (max-width: 600px){.MainPage .DataBlock .DataCard[data-v-99b6c1fe]{padding:4px 8px}}",""]),t.exports=e},501:function(t,e,n){"use strict";n.r(e);var r=n(2),o=n(354),d=r.default.extend({props:{url:{type:String,default:""},text:{type:String,default:""},btnText:{type:String,default:""}},computed:{linkTag:function(){return this.isInternalLink?"nuxt-link":"a"},linkAttrs:function(){return this.isInternalLink?{to:this.url,class:"StaticInfo"}:{href:this.url,class:"StaticInfo"}},isInternalLink:function(){return!/^https?:\/\//.test(this.url)}}}),c=(n(459),n(4)),l=Object(c.a)(d,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n(t.linkTag,t._b({tag:"component"},"component",t.linkAttrs,!1),[n("span",[t._v(t._s(t.text))]),t._v(" "),t.btnText?n("div",{staticClass:"StaticInfo-Button"},[n("span",[t._v("\n      "+t._s(t.btnText)+"\n    ")])]):t._e()])}),[],!1,null,null,null).exports,m=n(350),f=n(461),v=n(418),h=n(410),x=n(407),_=n(408),w=n(416),C=n(411),y=n(415),k=n(414),T=n(412),I=n(417),P=n(409),B=r.default.extend({components:{PageHeader:o.a,StaticInfo:l,ConfirmedCasesNumberCard:v.a,ConfirmedCasesAttributesCard:h.a,ConfirmedCasesDetailsCard:x.a,TestedCasesDetailsCard:_.a,InspectionPersonsNumberCard:w.a,PositiveRateCard:C.a,TelephoneAdvisoryReportsNumberCard:y.a,ConsultationDeskReportsNumberCard:k.a,PatientsByResidenceCard:T.a,PatientsByAgeCard:I.a,PatientsByGenderCard:P.a},data:function(){var data={Data:m,headerItem:{icon:"mdi-chart-timeline-variant",title:this.$t("県内の最新感染動向")},newsItems:f.newsItems};return data},head:function(){return{title:this.$t("県内の最新感染動向")}}}),E=(n(485),Object(c.a)(B,(function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"MainPage"},[n("div",{staticClass:"Header mb-3"},[n("page-header",{attrs:{icon:t.headerItem.icon}},[t._v("\n      "+t._s(t.headerItem.title)+"\n    ")]),t._v(" "),n("div",{staticClass:"UpdatedAt"},[n("span",[t._v(t._s(t.$t("最終更新"))+" ")]),t._v(" "),n("time",{attrs:{datetime:t.updatedAt}},[t._v(t._s(t.Data.lastUpdate))])]),t._v(" "),["ja","ja-basic"].includes(t.$i18n.locale)?t._e():n("div",{staticClass:"Annotation"},[n("span",[t._v(t._s(t.$t("注釈"))+" ")])])],1),t._v(" "),n("div",{staticClass:"TwitterTimelineBlock mb-4"},[n("h3",{staticClass:"WhatsNew-heading"},[n("i",{staticClass:"v-icon notranslate WhatsNew-heading-icon mdi mdi-information theme--light",staticStyle:{"font-size":"24px"},attrs:{"aria-hidden":"true"}}),t._v("\n      "+t._s(t.$t("最新のお知らせ"))+" \n    ")]),t._v(" "),t._m(0),t._v(" "),n("script",{attrs:{async:"",src:"https://platform.twitter.com/widgets.js",charset:"utf-8"}})]),t._v(" "),n("div",{staticClass:"EmergencyBlock mb-4"},[n("h3",{staticClass:"WhatsNew-heading"},[n("i",{staticClass:"v-icon notranslate WhatsNew-heading-icon mdi mdi-bullhorn theme--light",staticStyle:{"font-size":"24px"},attrs:{"aria-hidden":"true"}}),t._v("\n      "+t._s(t.$t("富山県対策指針 策定"))+" \n    ")]),t._v(" "),t._m(1),t._v(" "),n("p",[t._v("富山県では、外出自粛や休業要請を定めた３段階のステージを設定しています。")]),t._v(" "),n("p",[t._v("直近１週間の新規感染者数など５項目の指標を設けており、全ての指標が基準を下回る状況が続けば、政府の方針も踏まえつつ、ステージを段階的に変えていきます。")]),t._v(" "),n("img",{staticClass:"EmergencyImage",attrs:{src:"/roadmap1.jpg",alt:"roadmap1"}}),t._v(" "),n("img",{staticClass:"EmergencyImage",attrs:{src:"/roadmap2.jpg",alt:"roadmap2"}}),t._v(" "),n("a",{attrs:{href:"http://www.pref.toyama.jp/cms_sec/1205/kj00022037.html",target:"_blank"}},[t._v(t._s(t.$t("新型コロナウイルス感染拡大にかかる富山県対策指針について（令和2年5月14日策定）")))])]),t._v(" "),n("static-info",{staticClass:"mb-4",attrs:{url:t.localePath("/flow"),text:t.$t("自分や家族の症状に不安や心配があればまずは電話相談をどうぞ"),"btn-text":t.$t("相談の手順を見る")}}),t._v(" "),n("v-row",{staticClass:"DataBlock"},[n("confirmed-cases-details-card"),t._v(" "),n("confirmed-cases-number-card"),t._v(" "),n("confirmed-cases-attributes-card"),t._v(" "),n("patients-by-residence-card"),t._v(" "),n("patients-by-age-card"),t._v(" "),n("patients-by-gender-card"),t._v(" "),n("tested-cases-details-card"),t._v(" "),n("positive-rate-card"),t._v(" "),n("inspection-persons-number-card"),t._v(" "),n("telephone-advisory-reports-number-card"),t._v(" "),n("consultation-desk-reports-number-card")],1)],1)}),[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"EmbeddedTwitterTimeline"},[e("a",{staticClass:"twitter-timeline",attrs:{"data-height":"300px","data-chrome":"noheader nofooter",href:"https://twitter.com/stopcovidtoyama?ref_src=twsrc%5Etfw"}},[this._v("Loading...")])])},function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticStyle:{border:"4px solid #ffd700"}},[e("p",[this._v("富山県は現在「Stage２」の措置を実施しています。")])])}],!1,null,"99b6c1fe",null));e.default=E.exports}}]);
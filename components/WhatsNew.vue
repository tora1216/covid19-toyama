<template>
  <div class="WhatsNew">
    <h3 class="WhatsNew-heading">
      <v-icon size="24" class="WhatsNew-heading-icon">
        mdi-bullhorn
      </v-icon>
      {{ $t('富山県の対策指針') }}
    </h3>
    <p>{{ $t('富山県では、感染拡大防止のための措置として外出自粛や休業要請を定めた3段階のステージを設定しています。') }}</p>
    <div class="RoadMap-stage-alert">
      <h4>{{ $t('「富山アラート」発令中') }}</h4>
      <p>
        {{ $t('今後さらに感染が拡大すると、「Stage2」に移行となり、夜間の外出自粛や感染拡大地域への移動自粛などをお願いせざるを得ない状況となります。以下、改めてのお願いです。') }}
      </p>
      <ul>
        <li>{{ $t('3密の徹底的な回避、手洗いやマスクの着用など「新しい生活様式」の徹底') }}</li>
        <li>{{ $t('感染者が多く発生している地域との往来は特に緊要度の高いものを除き自粛') }}</li>
        <li>{{ $t('親族や友人が集まり会食する機会等における感染防止対策の徹底') }}</li>
        <li>{{ $t('業種ごとの感染拡大防止ガイドラインの遵守') }}</li>
        <li>{{ $t('重症化しやすい高齢者への感染予防行動の徹底、大声をあげる環境の徹底的な回避') }}</li>
      </ul>
    </div>
    <div class="row" style="margin-bottom:16px;">
      <div class="col-sm-12 col-md-6 col-lg-6 col-12">
        <div class="RoadMap-stage">
          <p class="RoadMap-stage-label">{{ $t('現在「Stage1」を適用中です') }}</p>
          <ul class="RoadMap-stages">
            <li class="RoadMap-stages-stage1">Stage1</li>
            <li>Stage2</li>
            <li>Stage3</li>
          </ul>
          <table class="RoadMap-stage-content">
            <thead>
              <tr>
                <th></th>
                <th class="RoadMap-stages-stage1">Stage1</th>
                <th class="RoadMap-stages-stage2">Stage2</th>
                <th class="RoadMap-stages-stage3">Stage3</th>
              </tr>
            </thead>
            <tbody>
            <tr>
              <th>{{ $t('外出') }}</th>
              <td>〇</td>
              <td>△</td>
              <td>×</td>
            </tr>
            <tr>
              <th>{{ $t('県外への移動') }}</th>
              <td>△</td>
              <td>△</td>
              <td>×</td>
            </tr>
            <tr>
              <th>{{ $t('接待を伴う飲食店の利用') }}</th>
              <td>〇</td>
              <td>×</td>
              <td>×</td>
            </tr>
            <tr>
              <th>{{ $t('大規模催物の開催') }}</th>
              <td>△</td>
              <td>△</td>
              <td>×</td>
            </tr>
            <tr>
              <th>{{ $t('店舗等の営業') }}</th>
              <td>〇</td>
              <td>〇</td>
              <td>△</td>
            </tr>
            </tbody>
          </table>
          <small>{{ $t('（注）〇:自粛または制限なし(「新しい生活様式」や感染防止対策が前提)、△:制限、×:自粛') }}</small>
          <a href="http://www.pref.toyama.jp/cms_sec/1205/kj00022462.html" target="_blank" rel="noopener" class="RoadMap-stage-button">{{ $t('詳細を見る') }}</a>
        </div>
      </div>
      <div class="col-sm-12 col-md-6 col-lg-6 col-12">

    <div class="DataView-Header"><h3 class="DataView-Title">{{ $t('ステージの変更基準') }}</h3></div>
    <div class="DataView-Description">
    <ul>
      <li>{{ $t('（注）各指標は、直近1週間の平均値') }}</li>
      <li>{{ $t('（注）新規陽性者数と感染経路不明者数は、人口100万人当たりの値') }}</li>
    </ul>
    </div>
    <div class="DataView-CardText">
    <div style="overflow-y:scroll;box-shadow: 0 -20px 12px -12px #0003 inset;">
    <table class="mapTable" style="box-shadow: 0 -20px 12px -12px #0003 inset;">
      <thead>
        <tr>
          <th>1.{{ $t('入院者数') }}</th>
          <th>2.{{ $t('重症病床稼働率') }}</th>
          <th>3.{{ $t('新規陽性者数') }}</th>
          <th>4.{{ $t('感染経路不明者数') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>100 {{ $t('人') }}<br>({{ $t('未満') }})</td>
          <td>30 %<br>({{ $t('未満') }})</td>
          <td>2.5 {{ $t('人') }}<br>({{ $t('未満') }})</td>
          <td>1 {{ $t('人') }}<br>({{ $t('未満') }})</td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>

        <p>{{ $t('ステージの強化は、以下の通り決定します。') }}</p>
        <ul style="margin-bottom:16px;">
          <li>{{ $t('警戒情報：指標3と4のいずれもが基準に到達し、指標1または2が一定程度上昇した際に発令') }}</li>
          <li>{{ $t('Stage2：指標3と4のいずれもが基準に到達し、指標1または2が基準の50%に到達し数日継続した際に発令') }}</li>
          <li>{{ $t('Stage3：指標1～4のすべてが基準に到達し、数日継続した際に発令') }}</li>
        </ul>
        <p>{{ $t('ステージの緩和は、全ての指標が基準を下回る状況が1～2週間続く場合に専門家の意見を踏まえ決定します。') }}</p>
      </div>
    </div>

    <div class="DataView-Header"><h3 class="DataView-Title">{{ $t('モニタリング指標の状況') }}</h3></div>
    <div class="DataView-Description">
    <ul>
      <li>{{ $t('（注）各指標は、直近1週間の平均値') }}</li>
      <li>{{ $t('（注）新規陽性者数と感染経路不明者数は、人口100万人当たりの値') }}</li>
    </ul>
    </div>
    <div class="DataView-CardText">
    <div style="overflow-y:scroll;max-height:300px;box-shadow: 0 -20px 12px -12px #0003 inset;">
    <table class="mapTable">
      <thead>
        <tr>
          <th>{{ $t('日付') }}</th>
          <th>1.{{ $t('入院者数') }}</th>
          <th>2.{{ $t('重症病床稼働率') }}</th>
          <th>3.{{ $t('新規陽性者数') }}</th>
          <th>4.{{ $t('感染経路不明者数') }}</th>
          <th>{{ $t('達成状況') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, i) in items" :key="i">
          <td>{{ item['日付'] }}</td>
          <td>{{ item['入院者数'] }} {{ $t('人') }}</td>
          <td>{{ item['重症病床稼働率'] }} %</td>
          <td>{{ item['新規陽性者数'] }} {{ $t('人') }}</td>
          <td>{{ item['感染経路不明者数'] }} {{ $t('人') }}</td>
          <td>{{ item['達成状況'] }}</td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>

    <div style="max-width:220px;">
      <a href="http://www.pref.toyama.jp/cms_sec/1205/kj00022038.html" target="_blank" rel="noopener" style="font-size:12px;display:block;overflow-wrap: break-word;text-decoration: none;">[新型コロナウイルス感染症に打ち克つためのロードマップ]富山県HP(http://www.pref.toyama.jp/cms_sec/1205/kj00022038.html)を元に作成</a>
    </div>


    <!--<ul class="WhatsNew-list">
      <li v-for="(item, i) in items" :key="i" class="WhatsNew-list-item">
        <a
          class="WhatsNew-list-item-anchor"
          :href="item.url"
          target="_blank"
          rel="noopener"
        >
          <time
            class="WhatsNew-list-item-anchor-time px-2"
            :datetime="formattedDate(item.date)"
          >
            {{ item.date }}
          </time>
          <span class="WhatsNew-list-item-anchor-link">
            {{ item.text }}
            <v-icon
              v-if="!isInternalLink(item.url)"
              class="WhatsNew-item-ExternalLinkIcon"
              size="12"
            >
              mdi-open-in-new
            </v-icon>
          </span>
        </a>
      </li>
    </ul>-->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { convertDateToISO8601Format } from '@/utils/formatDate'

export default Vue.extend({
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    isInternalLink(path: string): boolean {
      return !/^https?:\/\//.test(path)
    },
    formattedDate(dateString: string) {
      return convertDateToISO8601Format(dateString)
    }
  }
})
</script>

<style lang="scss">
.WhatsNew {
  @include card-container();

  padding: 22px;
  margin-bottom: 20px;
}

.WhatsNew-heading {
  display: flex;
  align-items: center;

  @include card-h2();

  margin-bottom: 12px;
  color: $gray-2;
  margin-left: 12px;

  &-icon {
    margin: 3px;
  }
}

.WhatsNew .WhatsNew-list {
  padding-left: 0;
  list-style-type: none;

  &-item {
    &-anchor {
      display: inline-block;
      text-decoration: none;
      margin: 5px;
      font-size: 14px;

      @include lessThan($medium) {
        display: flex;
        flex-wrap: wrap;
      }

      &-time {
        flex: 0 0 90px;

        @include lessThan($medium) {
          flex: 0 0 100%;
        }

        color: $gray-1;
      }

      &-link {
        flex: 0 1 auto;

        @include text-link();

        @include lessThan($medium) {
          padding-left: 8px;
        }
      }

      &-ExternalLinkIcon {
        margin-left: 2px;
        color: $gray-3 !important;
      }
    }
  }
}

.mapTable {
  width: 100%;
  text-align: center;
  font-size: 12px;
  border-spacing: 0;

  thead th {
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    z-index: 1;
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.12);
  }

  thead tr th {
    color: rgba(0, 0, 0, 0.6);
    padding: 8px 10px;
    background: #fff;
  }

  tbody tr {
    color: #333;
  }

  tbody tr td {
    padding: 8px 10px;
  }

  tbody tr:nth-child(odd) {
    td{
      background: rgba(217, 217, 217, 0.3);
    }
  }
}

.Data-Card{
  padding:12px;
}

.RelaxationStep-steps-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    list-style: none;
    padding: 0;
    font-weight: 700;
    white-space: nowrap;
    width: 100%;
}
.RelaxationStep-steps-item {
    flex: 1 1 auto;
    margin-bottom: 12px;
}
.RelaxationStep-steps {
    border-radius: 5px 0 0 5px;
    margin-left: 0;
    font-size: 1.4rem;
    margin-left: 1.6rem;
    padding: .5rem .5rem .5rem 2rem;
}
.RelaxationStep-steps-on {
    color: #fff;
    background-color: #008830;
}
.RelaxationStep-steps-on::before {
    left: 1.55rem;
    border-left-color: #fff;
    border-width: 1.55rem 0 1.55rem 1.55rem;
    border-style: solid;
    border-color: transparent;
    position: absolute;
    content: "";
    top: 0;
    transform: translateX(-100%);
}
.RelaxationStep-steps-on::after {
    position: absolute;
    content: "";
    top: 0;
    right: 1px;
    transform: translateX(100%);
    border-left-color: #008830;
    border-width: 1.55rem 0 1.55rem 1.55rem;
    border-style: solid;
    border-color: transparent;
}
.RelaxationStep-steps-off {
    color: #4d4d4d;
    background-color: #d9d9d9;
}
.RelaxationStep-steps-off::before {
    left: 1.55rem;
    border-left-color: #fff;
    border-width: 1.55rem 0 1.55rem 1.55rem;
    border-style: solid;
    border-color: transparent;
    position: absolute;
    content: "";
    top: 0;
    transform: translateX(-100%);
}
.RelaxationStep-steps-off::after {
    position: absolute;
    content: "";
    top: 0;
    right: 1px;
    transform: translateX(100%);
    border-left-color: #d9d9d9;
    border-width: 1.55rem 0 1.55rem 1.55rem;
    border-style: solid;
    border-color: transparent;
}
.RelaxationStep-changed-text {
    text-align: center;
    font-weight: 700;
    color: #008830;
    font-size: 1.6rem;
}
  .WhatsNew a[target='_blank']{
    text-decoration: none;
  }
  .WhatsNew a[target='_blank']::after {
    content: '\F03CC';
    margin-left: 0.1em;
    margin-right: 0.2em;
    display: inline-block;
    text-decoration: none;
    /* stylelint-disable-next-line font-family-no-missing-generic-family-keyword */
    font: normal normal normal 24px/1 'Material Design Icons';
    font-size: inherit;
    text-rendering: auto;
    line-height: inherit;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

        .RoadMap-stage-label {
          color: #00a040;
          font-size: 20px;
          font-weight: 600;
          border-bottom: 3px solid #00a040;
          padding: 4px 8px;
        }

        .RoadMap-stages {
            list-style-type: none;
            display: table;
            width: 100%;
            padding: 0 !important;
            margin: 0;
            margin-bottom: 16px;
            overflow: hidden;
        }

        .RoadMap-stages li {
            display: table-cell;
            position: relative;
            background: #d9d9d9;
            padding: 0.5em 0.5em 0.5em 2em;
            color: #4d4d4d;
            font-weight: bold;
            text-align: center;
        }

        .RoadMap-stages li:last-child {
            padding-right: 1em;
        }

        .RoadMap-stages li:last-child:before,
        .RoadMap-stages li:last-child:after {
            display: none;
        }

        .RoadMap-stages li:before,
        .RoadMap-stages li:after {
            content: "";
            position: absolute;
            width: 0;
            height: 0;
            margin: auto;
        }

        .RoadMap-stages li:before {
            top: -15px;
            right: -1em;
            border-style: solid;
            border-color: transparent transparent transparent #fff;
            border-width: 35px 0 35px 1em;
            z-index: 10;
        }

        .RoadMap-stages li:after {
            top: -15px;
            right: -.8em;
            border-style: solid;
            border-color: transparent transparent transparent #d9d9d9;
            border-width: 35px 0 35px 1em;
            z-index: 10;
        }

        .RoadMap-stages-stage1 {
            color: #fff !important;
            background: #00a040 !important;
        }
        
        .RoadMap-stages li.RoadMap-stages-stage1:after {
            border-color: transparent transparent transparent #00a040;
        }

        .RoadMap-stages-stage2 {
            color: #fff !important;
            background: #fdbe40 !important;
        }

        .RoadMap-stages li.RoadMap-stages-stage2:after {
            border-color: transparent transparent transparent #fdbe40;
        }

        .RoadMap-stages-stage3 {
            color: #fff !important;
            background: #fa1629 !important;
        }

        .RoadMap-stages li.RoadMap-stages-stage3:after {
            border-color: transparent transparent transparent #fa1629;
        }

        .RoadMap-stage-button {
            padding: 4px 8px;
            display: inline-block;
            border-radius: 4px;
            background-color: #fff;
            border: 1px solid #00a040;
            color: #00a040 !important;
            cursor: pointer;
            text-decoration: none;
            float: right;
        }

        .RoadMap-stage-button:hover {
            color: #fff !important;
            background-color: #00a040;
        }

        .RoadMap-stage-alert{
          border: 3px solid #fdbe40;
          padding: 10px;
          margin-bottom: 16px;
        }

        .RoadMap-stage-alert h4{
          color: #fa1629;
          font-size: 20px;
          font-weight: 600;
          border-bottom: 3px solid #fa1629;
          margin-bottom: 16px;
        }

        table.RoadMap-stage-content{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 8px;
        }

        table.RoadMap-stage-content thead th{
            padding: 10px 0;
        }

        table.RoadMap-stage-content tr{
            border-bottom: solid 3px #fff;
        }

        table.RoadMap-stage-content tbody tr:last-child{
            border-bottom: none;
        }

        table.RoadMap-stage-content tbody th{
          position: relative;
          width: 35%;
          background-color: #4d4d4d;
          color: white;
          text-align: center;
          padding: 10px 0;
        }
        
       table.RoadMap-stage-content tbody th:after{
         display: block;
         content: "";
         width: 0px;
         height: 0px;
         position: absolute;
         top:calc(50% - 10px);
         right:-10px;
         border-left: 10px solid #4d4d4d;
         border-top: 10px solid transparent;
         border-bottom: 10px solid transparent;
       }

      table.RoadMap-stage-content tbody td{
        text-align: center;
        background-color: #eee;
        padding: 10px;
      }
</style>

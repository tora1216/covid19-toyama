<template>
  <div class="WhatsNew">
    <h3 class="WhatsNew-heading">
      <v-icon size="24" class="WhatsNew-heading-icon">
        mdi-bullhorn
      </v-icon>
      {{ $t('富山県の対策指針') }}
    </h3>
    <p>富山県では、感染拡大防止のための措置として外出自粛や休業要請を定めた3段階のステージを設定しています。</p>
    <div class="row" style="margin-bottom:16px;">
      <div class="col-sm-12 col-md-6 col-lg-6 col-12">
        <div class="RoadMap-stage">
          <p class="RoadMap-stage-label">{{ $t('現在「Stage1」を発令中です') }}</p>
          <ul class="RoadMap-stages">
            <li class="RoadMap-stages-current">Stage1</li>
            <li>Stage2</li>
            <li>Stage3</li>
          </ul>
          <p>以下の措置を行っています。</p>
          <table class="RoadMap-stage-content">
            <tr>
              <th>外出の自粛</th>
              <td>基本的な感染防止対策等が徹底されていない施設への出入りは控えるよう要請<br>(新しい生活様式の徹底)</td>
            </tr>
            <tr>
              <th>催物の開催</th>
              <td>大規模イベント等について段階的に緩和<br>(感染防止対策の徹底)</td>
            </tr>
            <tr>
              <th>休業要請等</th>
              <td>休業要請等は行わない<br>(感染防止対策の徹底)</td>
            </tr>
          </table>
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
    <div style="box-shadow: 0 -20px 12px -12px #0003 inset;">
    <table class="mapTable" style="box-shadow: 0 -20px 12px -12px #0003 inset;">
      <thead>
        <tr>
          <th>1.{{ $t('入院者数') }}</th>
          <th>2.{{ $t('重症病床稼働率') }}</th>
          <th>3.{{ $t('新規陽性者数') }}</th>
          <th>4.{{ $t('感染経路不明者数') }}</th>
          <th>5.{{ $t('検査陽性率') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>100 {{ $t('人') }}<br>({{ $t('未満') }})</td>
          <td>30 %<br>({{ $t('未満') }})</td>
          <td>2.5 {{ $t('人') }}<br>({{ $t('未満') }})</td>
          <td>1 {{ $t('人') }}<br>({{ $t('未満') }})</td>
          <td>7 %<br>({{ $t('未満') }})</td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>

        <p>ステージの強化は、以下の通り決定します。</p>
        <ul style="margin-bottom:16px;">
          <li>警戒情報：指標3と4のいずれもが基準に到達し、指標1または2が一定程度上昇した際に発令</li>
          <li>Stage2：指標3と4のいずれもが基準に到達し、指標1または2が基準の50%に到達し数日継続した際に発令</li>
          <li>Stage3：指標1～4のすべてが基準に到達し、数日継続した際に発令</li>
        </ul>
        <p>ステージの緩和は、全ての基準が下回る状況が1～2週間続く場合に専門家の意見を踏まえ決定します。</p>
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
          <th>5.{{ $t('検査陽性率') }}</th>
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
          <td>{{ item['陽性率'] }} %</td>
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
            background: #4d4d4d;
            padding: 0.5em 0.5em 0.5em 2em;
            color: #fff;
            text-align: center;
            border-radius: 4px;
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
            border-color: transparent transparent transparent #4d4d4d;
            border-width: 35px 0 35px 1em;
            z-index: 10;
        }

        .RoadMap-stages li.RoadMap-stages-current {
            background: #00a040;
            font-weight: bold;
        }

        .RoadMap-stages li.RoadMap-stages-current:after {
            border-color: transparent transparent transparent #00a040;
        }

        .RoadMap-stages li.RoadMap-stages-next {
            background: linear-gradient(to right, #00a040, #4d4d4d);
            font-weight: bold;
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

        table.RoadMap-stage-content{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 16px;
        }

        table.RoadMap-stage-content tr{
            border-bottom: solid 3px #fff;
        }

        table.RoadMap-stage-content tr:last-child{
            border-bottom: none;
        }

        table.RoadMap-stage-content th{
          position: relative;
          text-align: left;
          width: 35%;
          background-color: #00a040;
          color: white;
          text-align: center;
          padding: 10px 0;
          border-radius: 4px;
        }
        
       table.RoadMap-stage-content th:after{
         display: block;
         content: "";
         width: 0px;
         height: 0px;
         position: absolute;
         top:calc(50% - 10px);
         right:-10px;
         border-left: 10px solid #00a040;
         border-top: 10px solid transparent;
         border-bottom: 10px solid transparent;
       }

      table.RoadMap-stage-content td{
        text-align: left;
        width: 65%;
        text-align: center;
        background-color: #eee;
        padding: 10px;
        border-radius: 4px;
      }
</style>

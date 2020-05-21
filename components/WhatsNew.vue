<template>
  <div class="WhatsNew">
    <h3 class="WhatsNew-heading">
      <v-icon size="24" class="WhatsNew-heading-icon">
        mdi-information
      </v-icon>
      {{ $t('富山県の対策指針') }}
    </h3>
    <div style="background-color: #ffe200; color: #4d4d4d; border-radius: 4px; padding: 4px 8px; font-weight: bold; margin: 16px 0px;">
      {{ $t('現在「Stage2」の措置を実施中です') }} 
    </div>
    <p style="color:#4d4d4d;">{{ $t('　富山県では、外出自粛や休業要請を定めた３段階のステージを設定しています。直近１週間の新規感染者数など５項目の指標を設けており、全ての指標が基準を下回る状況が続けば、政府の方針も踏まえつつ、ステージを段階的に変えていきます。') }} </p>
    
    <div class="Data-Card">
    <p>ステージと要請内容</p>
    <div style="overflow-y:scroll;max-height:200px;">
    <table class="mapTable">
      <thead>
        <tr>
          <th>{{ $t('ステージ') }}</th>
          <th>{{ $t('外出自粛') }}</th>
          <th>{{ $t('イベント開催') }}</th>
          <th>{{ $t('休業要請') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ $t('Stage3') }}</td>
          <td>×{{ $t('昼間') }} ×{{ $t('夜間') }} ×{{ $t('県外') }}<br>×{{ $t('繁華街の接待を伴う飲食店') }}</td>
          <td>×{{ $t('大規模イベント等') }}<br>〇{{ $t('一定の要件を満たす小規模イベント') }}</td>
          <td>{{ $t('特措法に基づく施設に限定') }}<br>{{ $t('食事提供施設は酒類の提供のみ短縮を依頼(20:00まで)') }}</td>
        </tr>
        <tr>
          <td>{{ $t('Stage2') }}</td>
          <td>〇{{ $t('昼間') }} ×{{ $t('夜間') }} ×{{ $t('県外') }}<br>×{{ $t('繁華街の接待を伴う飲食店') }}<br>({{ $t('新たな生活様式の徹底') }})</td>
          <td>×{{ $t('大規模イベント等') }}<br>〇{{ $t('一定の要件を満たす小規模イベント') }}</td>
          <td>{{ $t('クラスターが発生した施設に限定（キャバレー、カラオケ、ライブハウスなど）') }}<br>{{ $t('食事提供施設は酒類の提供のみ短縮を依頼(21:00まで)') }}</td>
        </tr>
        <tr>
          <td>{{ $t('Stage1') }}</td>
          <td>〇{{ $t('昼間') }} 〇{{ $t('夜間') }} ×{{ $t('県外') }}<small>({{ $t('特定警戒都道府県に限定') }})</small><br>〇{{ $t('繁華街の接待を伴う飲食店') }}<br>({{ $t('新たな生活様式の徹底') }})</td>
          <td>×{{ $t('大規模イベント等') }}<small>({{ $t('専門家の意見等も踏まえ別途判断') }})</small><br>〇{{ $t('一定の要件を満たす小規模イベント') }}</td>
          <td>{{ $t('休業要請等は行わない(感染防止策の徹底)') }}</td>
        </tr>
      </tbody>
    </table>
    </div>
    </div>

    <div class="Data-Card">
    <p>{{ $t('ステージの変更基準') }}</p>
    <ul class="mapNote">
      <li>{{ $t('（注）各指標は、直近1週間の平均値') }}</li>
      <li>{{ $t('（注）新規陽性者数と感染経路不明者数は、人口100万人当たりの値') }}</li>
    </ul>
    <table class="mapTable">
      <thead>
        <tr>
          <th>{{ $t('入院者数') }}</th>
          <th>{{ $t('重症病床稼働率') }}</th>
          <th>{{ $t('新規陽性者数') }}</th>
          <th>{{ $t('感染経路不明者数') }}</th>
          <th>{{ $t('検査陽性率') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ $t('100人') }}<br>{{ $t('未満') }}</td>
          <td>{{ $t('30%') }}<br>{{ $t('未満') }}</td>
          <td>{{ $t('2.5人') }}<br>{{ $t('未満') }}</td>
          <td>{{ $t('1人') }}<br>{{ $t('未満') }}</td>
          <td>{{ $t('7%') }}<br>{{ $t('未満') }}</td>
        </tr>
      </tbody>
    </table>
    </div>

    <div class="Data-Card">
    <p>{{ $t('現在の状況') }}</p>
    <ul class="mapNote">
      <li>{{ $t('（注）各指標は、直近1週間の平均値') }}</li>
      <li>{{ $t('（注）新規陽性者数と感染経路不明者数は、人口100万人当たりの値') }}</li>
    </ul>
    <div style="overflow-y:scroll;max-height:200px;">
    <table class="mapTable">
      <thead>
        <tr>
          <th>{{ $t('日付') }}</th>
          <th>{{ $t('入院者数') }}</th>
          <th>{{ $t('重症病床稼働率') }}</th>
          <th>{{ $t('新規陽性者数') }}</th>
          <th>{{ $t('感染経路不明者数') }}</th>
          <th>{{ $t('検査陽性率') }}</th>
          <th>{{ $t('達成状況') }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, i) in items" :key="i">
          <td>{{ item['日付'] }}</td>
          <td>{{ item['入院者数'] }}</td>
          <td>{{ item['重症病床稼働率'] }}</td>
          <td>{{ item['新規陽性者数'] }}</td>
          <td>{{ item['感染経路不明者数'] }}</td>
          <td>{{ item['陽性率'] }}</td>
          <td>{{ item['達成状況'] }}</td>
        </tr>
      </tbody>
    </table>
    </div>
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

  padding: 10px;
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
  box-shadow: 0 -20px 12px -12px #0003 inset;

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

.mapNote {
  list-style-type: none;
  padding: 0!important;
  font-size: 12px;
  color: #707070;
}

.Data-Card{
  padding:12px;
}
</style>

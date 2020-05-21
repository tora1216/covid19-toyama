<template>
  <div class="WhatsNew">
    <h3 class="WhatsNew-heading">
      <v-icon size="24" class="WhatsNew-heading-icon">
        mdi-information
      </v-icon>
      {{ $t('最新の状況') }}
    </h3>
    <p>{{ $t('　活動再開へのロードマップにおける、規制の強化・緩和の判断指標は以下の通りです。') }}</p>
    <ul class="note">
      <li>{{ $t('（注）各指標は、直近1週間の平均値') }}</li>
      <li>{{ $t('（注）新規陽性者数と感染経路不明者数は、人口100万人当たりの値') }}</li>
    </ul>
    <table class="mapTable">
      <thead>
        <tr>
          <th>{{ $t('日付') }}<br>({{ $t('基準') }})</th>
          <th>{{ $t('入院者数') }}<br>({{ $t('100人未満') }})</th>
          <th>{{ $t('重症病床稼働率') }}<br>({{ $t('30%未満') }})</th>
          <th>{{ $t('新規陽性者数') }}<br>({{ $t('2.5人未満') }})</th>
          <th>{{ $t('感染経路不明者数') }}<br>({{ $t('1人未満') }})</th>
          <th>{{ $t('陽性率') }}<br>({{ $t('7%未満') }})</th>
          <th>{{ $t('達成状況') }}<br></th>
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
  margin: 16px 0;
  border-spacing: 0;

  thead th {
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.12);
  }

  thead tr th {
    color: rgba(0, 0, 0, 0.6);
  }

  tbody tr {
    color: #333;
  }

  tbody tr:nth-child(odd) {
    td{
      background: rgba(217, 217, 217, 0.3);
    }
  }
}

.note {
  list-style-type: none;
  padding: 0;
  font-size: 12px;
  color: #707070;
}
</style>

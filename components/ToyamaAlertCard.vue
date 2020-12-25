<template>
  <div class="ToyamaAlert">
    <div class="ToyamaAlert-heading">
      <h3 class="ToyamaAlert-title">
        {{ $t('新型コロナウイルス感染拡大警報(富山アラート)') }}
      </h3>
      <div class="ToyamaAlert-link">
        <link-to-information-about-toyamaalert />
      </div>
    </div>
    <div class="ToyamaAlert-content">
      <div class="ToyamaAlert-block ToyamaAlert-block-description">
        <p>
          {{
            $t(
              '今後さらに感染が拡大すると、夜間の外出自粛や感染拡大地域への移動自粛などをお願いせざるを得ない状況となります。以下、改めてのお願いです。'
            )
          }}
        </p>
      </div>
      <div class="ToyamaAlert-block ToyamaAlert-block-detail">
        <ul>
          <li>{{ $t('他都道府県との移動は、慎重に検討') }}</li>
          <li>{{ $t('「新しい生活様式」の徹底、「5つの場面」を回避、「ますずし」の実践') }}</li>
          <li>{{ $t('家庭内でもマスクを着用するなど、感染予防行動を徹底') }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import LinkToInformationAboutToyamaalert from '@/components/LinkToInformationAboutToyamaalert.vue'
export default Vue.extend({
  components: {
    LinkToInformationAboutToyamaalert
  }
})
</script>

<style lang="scss">
$mediumLarge: 900;
$tinySmall: 420;
@function px2vw($px, $vw: $mediumLarge) {
  @return $px / $vw * 100vw;
}
.ToyamaAlert {
  @include card-container();
  padding: 22px;
  margin-bottom: 20px;
  .ToyamaAlert-heading {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    .ToyamaAlert-title {
      display: flex;
      align-items: center;
      padding: 12px;
      color: $gray-2;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }
    .ToyamaAlert-link {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: flex-end;
      padding-left: 12px;
      @include lessThan($medium) {
        justify-content: flex-start;
      }
    }
  }
  .ToyamaAlert-content {
    @include font-size(14);
    display: flex;
    flex-wrap: wrap;
    .ToyamaAlert-block {
      flex: 1 1 100%;
      padding: 12px;
      p {
        margin-bottom: 0;
      }
    }
    .ToyamaAlert-block-detail {
      background-color: #ad2121;
      color: #fff;
      border-radius: 3px;
    }
  }
}
</style>
<template>
  <div class="WhatsNew">
    <div class="WhatsNew-heading">
      <h3 class="WhatsNew-title">
        {{ $t('最新のお知らせ') }}
      </h3>
      <div class="WhatsNew-link">
        <link-to-twitter-account />
      </div>
    </div>
    <div class="WhatsNew-content">
      <div class="WhatsNew-block WhatsNew-block-timeline">
        <a class="twitter-timeline" data-height="300px" data-chrome="noheader nofooter" href="https://twitter.com/covid19_toyama?ref_src=twsrc%5Etfw">Loading...</a>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import LinkToTwitterAccount from '@/components/LinkToTwitterAccount.vue'
export default Vue.extend({
  components: {
    LinkToTwitterAccount
  }
})
</script>

<style lang="scss">
$mediumLarge: 900;
$tinySmall: 420;
@function px2vw($px, $vw: $mediumLarge) {
  @return $px / $vw * 100vw;
}
.WhatsNew {
  @include card-container();
  padding: 10px;
  margin-bottom: 20px;
  .WhatsNew-heading {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    .WhatsNew-title {
      display: flex;
      align-items: center;
      padding: 12px;
      color: $gray-2;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }
    .WhatsNew-link {
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
  .WhatsNew-content {
    @include font-size(14);
    display: flex;
    flex-wrap: wrap;
    .WhatsNew-block-timeline {
      width: 50%;
      margin: auto;
      @include lessThan($medium) {
        width: 100%;
      }
    }
  }
}
</style>
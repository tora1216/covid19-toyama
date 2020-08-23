<template>
  <div class="RelaxationStep">
    <div class="RelaxationStep-heading">
      <h3 class="RelaxationStep-title">
        {{ $t('新型コロナウイルス感染症に打ち克つためのロードマップ') }}
      </h3>
      <div class="RelaxationStep-link">
        <link-to-information-about-roadmap />
      </div>
    </div>
    <div class="RelaxationStep-content">
      <div class="RelaxationStep-block RelaxationStep-block-description">
        <p>
          {{
            $t(
              '富山県では、感染拡大防止のための措置として外出自粛や休業要請を定めた3段階のステージを設定しています。ステージの強化や緩和は、医療体制や感染状況等の判断指標を踏まえて行います。'
            )
          }}
        </p>
      </div>
      <div class="RelaxationStep-block RelaxationStep-block-steps">
        <ul class="RelaxationStep-steps-list">
          <li class="RelaxationStep-steps-item active">
            Stage1
          </li>
          <li class="RelaxationStep-steps-item">
            Stage2
          </li>
          <li class="RelaxationStep-steps-item">
            Stage3
          </li>
        </ul>
        <p class="RelaxationStep-changed-text">
          {{ $t('現在 Stage1 を適用中です') }}
        </p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import LinkToInformationAboutRoadmap from '@/components/LinkToInformationAboutRoadmap.vue'
export default Vue.extend({
  components: {
    LinkToInformationAboutRoadmap
  }
})
</script>

<style lang="scss">
$mediumLarge: 900;
$tinySmall: 420;
@function px2vw($px, $vw: $mediumLarge) {
  @return $px / $vw * 100vw;
}
.RelaxationStep {
  @include card-container();
  padding: 10px;
  margin-bottom: 20px;
  .RelaxationStep-heading {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
    .RelaxationStep-title {
      display: flex;
      align-items: center;
      padding: 12px;
      color: $gray-2;
      @include card-h2();
      &-icon {
        margin: 3px;
      }
    }
    .RelaxationStep-link {
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
  .RelaxationStep-steps {
    position: relative;
    z-index: 3;
    display: block;
    padding: px2vw(5) px2vw(10) px2vw(5) px2vw(25);
    margin-left: px2vw(16);
    font-size: px2vw(14);
    text-align: center;
    &-on {
      color: $white;
      background-color: $green-1;
    }
    &-off {
      color: $gray-2;
      background-color: $gray-4;
    }
    &::after,
    &::before {
      position: absolute;
      top: 50%;
      content: '';
      border-color: transparent;
      border-style: solid;
      border-width: px2vw(15.5) 0 px2vw(15.5) px2vw(15.5);
    }
    &::after {
      right: 0.1rem;
      transform: translate(100%, -50%);
    }
    &-on::after {
      border-left-color: $green-1;
    }
    &-off::after {
      border-left-color: $gray-4;
    }
    &::before {
      left: px2vw(15);
      border-left-color: $white;
      transform: translate(-100%, -50%);
    }
  }
  @include lessThan($small) {
    .RelaxationStep-steps {
      padding: 0.5rem 0.5rem 0.5rem 2rem;
      margin-left: 1.4rem;
      font-size: 1rem;
      &::after,
      &::before {
        border-width: 1.3rem 0 1.3rem 1.3rem;
      }
      &-on::before,
      &-off::before {
        left: 1.2rem;
      }
    }
  }
  @include lessThan($tinySmall) {
    .RelaxationStep-steps {
      padding: 0.32rem 0.32rem 0.32rem 1rem;
      margin-left: 1rem;
      font-size: 0.8rem;
      &::after,
      &::before {
        border-width: 1rem 0 1rem 0.8rem;
      }
      &-on::before,
      &-off::before {
        left: 0.8rem;
      }
    }
  }
  @include largerThan($mediumLarge) {
    .RelaxationStep-steps {
      padding: 0.5rem 0.5rem 0.5rem 2rem;
      margin-left: 1.6rem;
      font-size: 1.4rem;
      &::after,
      &::before {
        border-width: 1.55rem 0 1.55rem 1.55rem;
      }
      &-on::before,
      &-off::before {
        left: 1.45rem;
      }
    }
  }
  .RelaxationStep-content {
    @include font-size(14);
    display: flex;
    flex-wrap: wrap;
    .RelaxationStep-block {
      flex: 1 1 100%;
      padding: 12px;
      @include largerThan($large) {
        &-description {
          flex-basis: 40%;
        }
        &-steps {
          flex-basis: auto;
        }
      }
      @include lessThan($tinySmall) {
        &-steps {
          margin: 0 -8px;
        }
      }
    }

        .RelaxationStep-steps-list {
            list-style-type: none;
            display: table;
            width: 100%;
            padding: 0 !important;
            margin: 0;
            margin-bottom: 16px;
            overflow: hidden;
        }

        .RelaxationStep-steps-list li {
            display: table-cell;
            position: relative;
            background: #d9d9d9;
            padding: 0.5em 0.5em 0.5em 2em;
            color: #4d4d4d;
            font-weight: bold;
            text-align: center;
        }

        .RelaxationStep-steps-list li:last-child {
            padding-right: 1em;
        }

        .RelaxationStep-steps-list li:last-child:before,
        .RelaxationStep-steps-list li:last-child:after {
            display: none;
        }

        .RelaxationStep-steps-list li:before,
        .RelaxationStep-steps-list li:after {
            content: "";
            position: absolute;
            width: 0;
            height: 0;
            margin: auto;
        }

        .RelaxationStep-steps-list li:before {
            top: -16px;
            right: -1em;
            border-style: solid;
            border-color: transparent transparent transparent #fff;
            border-width: 35px 0 35px 1em;
            z-index: 10;
        }

        .RelaxationStep-steps-list li:after {
            top: -16px;
            right: -.8em;
            border-style: solid;
            border-color: transparent transparent transparent #d9d9d9;
            border-width: 35px 0 35px 1em;
            z-index: 10;
        }

        .RelaxationStep-steps-list li.active {
            color: #fff !important;
            background: #00a040 !important;
        }
        
        .RelaxationStep-steps-list li.active:after {
            border-color: transparent transparent transparent #00a040;
        }

    .RelaxationStep-changed-text {
      font-weight: bold;
      color: $green-1;
      text-align: center;
      @include font-size(16);
    }
  }
}
</style>
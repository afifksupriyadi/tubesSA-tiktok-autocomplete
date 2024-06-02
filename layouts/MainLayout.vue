<template>
  <TopNav />
  <div :class="route.fullPath === '/' ? 'max-w-[1280px]' : ''" class="flex justify-between mx-auto w-full lg:px-2.5 px-0 mt-5">
    <div>
      <SideNavMain />
    </div>
    <div class="flex-1 mx-4">
      <slot />
    </div>
  </div>
</template>

<script setup>
import TopNav from '~/components/TopNav.vue'
import SideNavMain from '~/components/SideNavMain.vue'
const route = useRoute()
</script>

<style scoped>
.flex-1 {
  flex: 1;
}
</style>

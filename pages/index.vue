<template>
  <MainLayout>
    <div class="container mx-auto mt-20">
      <Autocomplete />
    </div>
  </MainLayout>
</template>

<script setup>
import MainLayout from '~/layouts/MainLayout.vue';
import Autocomplete from '~/components/Autocomplete.vue';
</script>

<style scoped>
.container {
  max-width: 500px; /* Sesuaikan dengan kebutuhan Anda */
  margin-left: auto;
  margin-right: auto;
}
</style>

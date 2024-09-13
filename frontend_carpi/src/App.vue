<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    

    <div>
      <HelloWorld/>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
</style>

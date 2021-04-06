<template>
  <v-app>
    <v-main>
      <dashboard/>
    </v-main>
  </v-app>
</template>

<script>
import dashboard from './components/dashboard';

export default {
  name: 'App',

  components: {
    dashboard,
  },

};
</script>

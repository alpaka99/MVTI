<template>
  <div id="">
    <v-footer
      dark
      padless
    >
      <v-card
        flat
        tile
        class="black lighten-2 white--text text-center"
      >
        <v-card-text>
          <v-btn
            v-for="icon in icons"
            :key="icon"
            class="mx-4 white--text"
            icon
          >
            <v-icon size="24px" style="color: rgb(180, 2, 12);">
              {{ icon }}
            </v-icon>
          </v-btn>
        </v-card-text>
  
        <v-card-text class="white--text p-0">
          Smooth like butter
Like a criminal undercover
Gon' pop like trouble
Breakin' into your heart like that
Cool shade stunner
Yeah I owe it all to my mother
Hot like summer
Yeah I'm makin' you sweat like that
Break it down
Oh when I look in the mirror
I'll melt your heart into 2
I got that superstar glow so
Do the boogie like
Side step right left to my beat (heartbeat)
High like the moon rock with me baby
Know that I got that heat
Let me show you 'cause talk is cheap
Side step right left to my beat (heartbeat)
Get it, let it roll
        </v-card-text>
  
        <v-divider></v-divider>
  
        <v-card-text class="white--text m-0 pt-0">
          {{ new Date().getFullYear() }} — <strong>대전 3반 1조</strong>
        </v-card-text>
      </v-card>
    </v-footer>
</div>
</template>

<script>
export default {
   data: () => ({
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
  }),
}
</script>

<style>

.theme--dark.v-footer {
  background-color: rgb(30, 30, 30);
}
</style>
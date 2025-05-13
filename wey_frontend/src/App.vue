<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const username = ref('Muzaffer Nergiz')
</script>

<template>
  <div>
    <!-- Navbar -->
    <header class="bg-white shadow-md p-4 flex justify-between items-center container mx-auto">
      <!-- Sol: Kullanıcı adı -->
      <div class="text-2xl font-bold text-blue-600">
        {{ username }}
      </div>

      <!-- Orta: Menü (RouterLink ile) -->
      <nav class="flex gap-6 text-gray-700 text-lg">
        <RouterLink to="/" class="hover:text-blue-500">Ana Sayfa</RouterLink>
        <RouterLink to="/messages" class="hover:text-blue-500">Mesaj</RouterLink>
        <RouterLink to="/notification" class="hover:text-blue-500">Bildirim</RouterLink>
        <RouterLink to="/search" class="hover:text-blue-500">Arama</RouterLink>
      </nav>

      <!-- Sağ: Avatar -->
      <div>
        <img src="https://ui-avatars.com/api/?name=Muzaffer+Nergiz" alt="Avatar" class="w-10 h-10 rounded-full" />
      </div>
    </header>

    <!-- Sayfa İçeriği -->
    <main class="p-6">
      <RouterView />
    </main>
  </div>

</template>

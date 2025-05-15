<script setup>
import { ref, onBeforeMount, onMounted, onBeforeUnmount } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user.js'
import Toast from '@/components/Toast.vue'
import axios from 'axios'
import { storeToRefs } from 'pinia'

const userStore = useUserStore()
const { isAuthenticated } = storeToRefs(userStore)

const dropdownOpen = ref(false)
const dropdownRef = ref(null)
const username = ref('Muzaffer Nergiz')

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value
}

const logout = () => {
  userStore.logout()
  dropdownOpen.value = false
}

// Dışarı tıklamayı algıla
const handleClickOutside = (event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    dropdownOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})

onBeforeMount(() => {
  userStore.initStore()
  const token = userStore.access
  axios.defaults.headers.common["Authorization"] = token
    ? "Bearer " + token
    : ""
})
</script>

<template>
  <div>
    <!-- Navbar -->
    <header class="bg-white shadow-md p-4 flex justify-between items-center">
      <!-- Sol: Kullanıcı adı -->
      <div class="text-2xl font-bold text-blue-600">
        {{ username }}
      </div>

      <!-- Orta Menü -->
      <nav class="flex gap-6 text-gray-700 text-lg" v-if="isAuthenticated">
        <RouterLink to="/feed" class="hover:text-blue-500">Ana Sayfa</RouterLink>
        <RouterLink to="/messages" class="hover:text-blue-500">Mesaj</RouterLink>
        <RouterLink to="/notification" class="hover:text-blue-500">Bildirim</RouterLink>
        <RouterLink to="/search" class="hover:text-blue-500">Arama</RouterLink>
      </nav>

      <!-- Sağ Menü -->
      <div class="relative" ref="dropdownRef">
        <template v-if="isAuthenticated">
          <!-- Avatar -->
          <img
            @click.stop="toggleDropdown"
            src="https://ui-avatars.com/api/?name=Muzaffer+Nergiz"
            alt="Avatar"
            class="w-10 h-10 rounded-full cursor-pointer"
          />

          <!-- Dropdown -->
          <transition name="fade">
            <div
              v-if="dropdownOpen"
              class="absolute right-0 mt-2 w-40 bg-white border border-gray-200 rounded-lg shadow-lg z-50"
            >
              <button
                @click="logout"
                class="block w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-gray-100"
              >
                Çıkış Yap
              </button>
            </div>
          </transition>
        </template>

        <template v-else>
          <RouterLink to="/login" class="py-2 px-4 bg-gray-600 text-white rounded-lg mr-2">
            Giriş Yap
          </RouterLink>
          <RouterLink to="/signup" class="py-2 px-4 bg-purple-600 text-white rounded-lg">
            Kayıt Ol
          </RouterLink>
        </template>
      </div>
    </header>

    <!-- Sayfa İçeriği -->
    <main class="py-6 px-8 bg-gray-100">
      <RouterView />
    </main>

    <Toast />
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.15s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>

<template>
    <div>
        <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center space-x-6">
                <img src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=300&h=300&q=80"
                    class="w-[40px] rounded-full">
                <p><strong>
                        <router-link :to="{ name: 'profile', params: { 'id': post.created_by.id } }">{{
                            post.created_by.name }}</router-link>
                    </strong></p>
            </div>
            <p class="text-gray-600">{{ post.created_at_formatted }}</p>
        </div>
        <p class="text-2xl">{{ post.body }}</p>
        <div class="my-6 flex justify-between relative">
            <div class="flex space-x-6">
                <div class="flex items-center space-x-6">
                    <div class="flex space-x-2">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 48 48">
                            <path fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round"
                                stroke-width="4"
                                d="M15 8C8.925 8 4 12.925 4 19c0 11 13 21 20 23.326C31 40 44 30 44 19c0-6.075-4.925-11-11-11c-3.72 0-7.01 1.847-9 4.674A10.99 10.99 0 0 0 15 8" />
                            <span>32 Beğeni</span>
                        </svg>
                    </div>
                    <div class="flex space-x-2">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path fill="#000"
                                d="M5 21v-4.157c-1.25-1.46-2-3.319-2-5.343C3 6.806 7.03 3 12 3s9 3.806 9 8.5s-4.03 8.5-9 8.5a9.35 9.35 0 0 1-4.732-1.268zm7-3c3.866 0 7-2.91 7-6.5S15.866 5 12 5s-7 2.91-7 6.5S8.134 18 12 18" />
                            <span>12 Yorum </span>
                        </svg>
                    </div>
                    <div class="absolute right-0">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <g fill="none">
                                <path
                                    d="m12.593 23.258l-.011.002l-.071.035l-.02.004l-.014-.004l-.071-.035q-.016-.005-.024.005l-.004.01l-.017.428l.005.02l.01.013l.104.074l.015.004l.012-.004l.104-.074l.012-.016l.004-.017l-.017-.427q-.004-.016-.017-.018m.265-.113l-.013.002l-.185.093l-.01.01l-.003.011l.018.43l.005.012l.008.007l.201.093q.019.005.029-.008l.004-.014l-.034-.614q-.005-.018-.02-.022m-.715.002a.02.02 0 0 0-.027.006l-.006.014l-.034.614q.001.018.017.024l.015-.002l.201-.093l.01-.008l.004-.011l.017-.43l-.003-.012l-.01-.01z" />
                                <path fill="#000"
                                    d="M12 16.5a1.5 1.5 0 1 1 0 3a1.5 1.5 0 0 1 0-3m0-6a1.5 1.5 0 1 1 0 3a1.5 1.5 0 0 1 0-3m0-6a1.5 1.5 0 1 1 0 3a1.5 1.5 0 0 1 0-3" />
                            </g>
                        </svg>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import {defineProps} from 'vue'

const props = defineProps({
    post:{
        type:Object,
        required:true
    }
})
</script>
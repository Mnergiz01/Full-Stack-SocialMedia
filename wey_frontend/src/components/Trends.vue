<template>
    <div>
        <div class="p-4 bg-white border border-gray-200 rounded-lg">
            <h3 class="mb-6 text-xl">Trendler</h3>
            <div class="space-y-4">
                <div class="flex items-center justify-between" v-for="i in 5" :key="i">
                    <p class="text-xs">
                        <strong>#mnergiz01</strong> <br>
                        <span class="text-gray-500">180 post</span>
                    </p>
                    <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Keşfet</a>
                </div>
            </div>
        </div>
    </div>
</template>
<template>
    <div>
        <div class="main-right col-span-1 space-y-4">
            <div class="p-4 bg-white border border-gray-200 rounded-lg flex flex-col gap-5">
                <h3 class="mb-6 text-xl ">Tanıyor Olabilirsin</h3>
                <div class="flex items-center justify-between" v-for="i in 5" :key="i">
                    <div class="flex items-center space-x-2">
                        <img src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=300&h=300&q=80"
                            class="w-[40px] rounded-full">
                        <p class="text-xs"><strong>Muzaffer Nergiz</strong></p>
                    </div>
                    <a href="#" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Göster</a>
                </div>
            </div>
        </div>
    </div>
</template>
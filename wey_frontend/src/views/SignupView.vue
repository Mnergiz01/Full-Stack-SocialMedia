<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">
                    Kayıt Ol
                </h1>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus, reiciendis quasi dolor eveniet
                    incidunt, hic sit beatae fuga deleniti harum enim quaerat facere voluptatibus quam dicta, libero
                    magnam neque nesciunt.
                </p>
                <p class="fone-bold">
                    Hesabınız Var Mı ? <a href="/login" class="text-blue-500 hover:text-blue-700 underline">Giriş
                        Yap</a>
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6">
                    <div>
                        <label>E-Mail</label><br>
                        <input type="email" placeholder="E-Mail Adresinizi Girin" class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>Şifre</label><br>
                        <input type="password" placeholder="Şifrenizi Girin" class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <label>Şifre Tekrar</label><br>
                        <input type="password" placeholder="Şifrenizi Tekrar Girin" class="w-full mt-2 py-4 px-6 border border-gray-300 rounded-lg">
                    </div>
                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Kayıt Ol</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>
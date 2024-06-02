<template>
    <div
        id="TopNav"
        class="fixed bg-white z-30 flex items-center w-full border-b h-[61px] -mt-2"
    >
        <div 
            :class="route.fullPath === '/' ? 'max-w-[1270px]' : ''"
            class="flex items-center justify-between w-full px-6 mx-auto"
        >
            <div  :class="route.fullPath === '/' ? 'w-[80%]' : 'lg:w-[20%] w-[70%]'"> 
                <NuxtLink to="/">
                    <img width="115" src="~/assets/images/tiktok-logo.png">
                </NuxtLink>
            </div>
  
            <div class="flex items-center justify-end gap-3 min-w-[275px] max-w-[320px] w-full">
                <button class="flex items-center border rounded-sm px-3 py-[6px] hover:bg-gray-100">
                    <Icon name="mdi:plus" color="#000000" size="22"/>
                    <span class="px-2 font-medium text-[15px]">Upload</span>
                </button>
  
                <!-- Menghapus elemen yang tidak diperlukan -->
                <div class="flex items-center">
                    <Icon class="ml-1 mr-4" name="carbon:send-alt" color="#161724" size="30"/>
                    <Icon class="mr-5" name="bx:message-detail" color="#161724" size="27"/>
                    <div>
                        <button 
                            @click="showMenu = !showMenu"
                            class="mt-1"
                        >
                            <img 
                                class="rounded-full" 
                                width="33" 
                                src="https://picsum.photos/id/83/300/320"
                            >
                        </button>
  
                        <div
                            v-if="showMenu" 
                            id="PopupMenu"
                            class="absolute bg-white rounded-lg py-1.5 w-[200px] shadow-xl border top-[43px] -right-2"
                        >
                            <NuxtLink
                                @click="showMenu = false"
                                class="flex items-center justify-start py-3 px-2 hover:bg-gray-100 cursor-pointer"
                            >
                                <Icon name="ic:outline-login" size="20"/>
                                <span class="pl-2 font-semibold text-sm">Profile</span>
                            </NuxtLink>
                            <div 
                                class="flex items-center justify-start py-3 px-1.5 hover:bg-gray-100 border-t cursor-pointer"
                            >
                                <Icon name="ic:outline-login" size="20"/>
                                <span class="pl-2 font-semibold text-sm">Log out</span>
                            </div>
  
                        </div>
  
                    </div>
  
                </div>
  
            </div>
        </div>
  
    </div>
  </template>
  
  <script setup>
  const route = useRoute()
  let showMenu = ref(false)
  </script>
  
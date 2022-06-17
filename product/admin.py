from django.contrib import admin
from product.models import Event


class EventAdmin(admin.ModelAdmin):
    # 데이터 베이스 처음 보여줄 필드들
    list_display = ('title', 'desc', 'activate', 'thumbnail')
    # 상세페이지에서 어디서 눌러갈 것인가?
    list_display_links = ('title', 'desc')
    # 필터 목록 만들기
    list_filter = ('title',)
    # 검색할 수 있는 필드
    search_fields = ('title',)
    # 수정이 불가한 필드 ( auto now로 보이지 않을때 씀 )
    readonly_fields = ('created_at',)
    # 상세 페이지 정렬
    fieldsets = (
        ('info', {
            'fields': ('title', 'desc', 'thumbnail'
                      )}),
        ('Date', {
             'fields': ('start_at', 'end_at',)
        }),
        ('cf', {
             'fields': ('created_at', 'activate')
        })
    )
    # inlines / tabulainline -> 다른 DB를 같이 보고 싶을 때
    # inlines : 가로로

    # tabulainline : 세로로


admin.site.register(Event, EventAdmin)

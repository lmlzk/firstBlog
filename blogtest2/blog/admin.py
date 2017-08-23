from django.contrib import admin
from blog.models import User,Catagory,Tag,Article,Ad,Links,Comment
# Register your models here.
admin.site.site_header = "lml个人blog管理后台"


class UserAdmin(admin.ModelAdmin):
    # list_display = ["id", "username", "avatar", "qq", "mobile"]
    exclude = ["password"]
    actions_on_bottom = True
    search_fields = ["username", "id",]
    list_per_page = 10


class CatagoryAdmin(admin.ModelAdmin):
    list_display = ["index", "name", ]
    actions_on_bottom = True
    search_fields = ["index", "name", ]
    list_per_page = 10


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ["id", "name"]


class ArticleAdmin(admin.ModelAdmin):
    exclude = ["desc", "user_id", "catagory_id", "tag_id"]
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ["id", "title", "is_recommend", "date_publish"]


class AdAdmin(admin.ModelAdmin):
    exclude = ["desc"]
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ["id", "title", "image", "index", "date_publish"]


class LinksAdmin(admin.ModelAdmin):
    exclude = ["desc", ]
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ["id", "title", "index"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "date_publish"]
    actions_on_bottom = True
    list_per_page = 10
    search_fields = ["id", "content", "date_publish"]


admin.site.register(User, UserAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Ad, AdAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Comment, CommentAdmin)

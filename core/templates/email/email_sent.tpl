{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock subject %}

{% block html %}
<img alt="hello" src="https://media.licdn.com/dms/image/v2/D4E12AQFgHEkq7imwfQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1703217946978?e=2147483647&v=beta&t=u1aaj4MGzGVeqCWdS3T_ANMal7SzWCRb0u_fJ1jdjio">
<div style="color:#2b2b2b">
    The email were <strong style="color:green">SUCCESSFULLY</strong> sent.  
</div>
{% endblock html %}
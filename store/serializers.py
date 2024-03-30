from rest_framework import serializers, exceptions
from .models import Store, Category, Product
from django.contrib.auth.models import User



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'location')


class CreateStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('name', 'location')


class CategorySerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=50, min_length=4)
    
    def validate(self, attrs):
            product_name=attrs.get('name')
            if product_name == 'rice':
                  raise exceptions.ValidationError("please rice is not accepted category")
            return attrs

    def create(self, validated_data):
            return Category.objects.create(product_name=validated_data['name'])

    def update(self, instance, validated_data):
            instance.name=validated_data.get('name', instance.name)
            instance.save()
            return instance

class CreateProductSerializer(serializers.ModelSerializer):
      class Meta:
            model=Product
            fields=['product_name', 'description', 'price', 'category']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'price', 'category']

class UserCreateSerializer(serializers.ModelSerializer):
      password=serializers.CharField(max_length=68, min_length=3, write_only=True)
      password2=serializers.CharField(max_length=68, min_length=3, write_only=True)
      class Meta:
            model=User
            fields=['username', 'email', 'password', 'password2']

      def validate(self, attrs):
            user=User.objects.filter(username=attrs.get('username'))
            if user.exists():
                  raise exceptions.ValidationError('user already exist try a different username')
            password1=attrs.get('password')
            password2=attrs.get('password2')
            if password1 != password2:
                  raise exceptions.ValidationError('password does not match')
            
            return attrs
      def create(self, validated_data):

            return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
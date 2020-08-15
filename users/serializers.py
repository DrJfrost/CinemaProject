from users.models import User, Contract, ClientProfile
from rest_framework import serializers

class ContractSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contract
        fields = ['salary', 'join_date', 'end_date', 'is_active', 'position']

class EmployeeSerializer(serializers.ModelSerializer):

    contract = ContractSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone', 'last_login', 'date_joined', 'is_staff', 'is_active', 'identification', 'contract']
        read_only_fields = ['is_active', 'is_staff', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        
        contract_data = validated_data.pop('contract')
        user = User.objects.create(**validated_data)
        
        #hash password instead of saving it in plain text
        user.set_password(user.password)

        contract = Contract.objects.create(user=user, **contract_data)
        contract.save()
        
        user.save()
        return user

    def update(self, instance, validated_data):
        
        #get contract of user
        contract = instance.contract
        contract_data = validated_data.pop('contract')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        #update password if it axists on the request
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        #update contract data
        if contract_data is not None:
            contract.salary = contract_data.get('salary', contract.salary)
            contract.join_date = contract_data.get('join_date', contract.join_date)
            contract.end_date = contract_data.get('end_date', contract.end_date)
            contract.is_active = contract_data.get('is-active', contract.is_active)
            contract.position = contract_data.get('position', contract.position)

            contract.save()
        
        instance.save()

        return instance

class ClientProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ClientProfile
        fields = ['score', 'address']

class ClientSerializer(serializers.ModelSerializer):

    client_profile = ClientProfileSerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone', 'last_login', 'date_joined', 'is_staff', 'is_active', 'identification', 'client_profile']
        read_only_fields = ['is_active', 'is_staff', 'date_joined', 'last_login']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        
        profile_data = validated_data.pop('client_profile')
        user = User.objects.create(**validated_data)
        
        #hash password instead of saving it in plain text
        user.set_password(user.password)

        profile = ClientProfile.objects.create(user=user, **profile_data)
        profile.save()
        
        user.save()
        return user

    def update(self, instance, validated_data):
        
        #get profile of user
        profile = instance.client_profile
        profile_data = validated_data.pop('client_profile')

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        #update password if it axists on the request
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        
        #update profile data
        if profile is not None:
            profile.score = profile_data.get('score', profile.score)
            profile.address = profile_data.get('address', profile.address)

            profile.save()
        
        instance.save()

        return instance

